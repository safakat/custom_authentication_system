# from django.conf import settings
# from django.contrib.auth.models import User

# from django.contrib.auth.backends import ModelBackend

# class EmailOrUsernameModelBackend(ModelBackend):
#     def authenticate(self, username=None, password=None):
#         print("1")
#         if '@' in username:
#             kwargs = {'email': username}
#         else:
#             kwargs = {'username': username}
#         try:
#             user = User.objects.get(**kwargs)
#             if user.check_password(password):
#                 return user
#         except User.DoesNotExist:
#             return None

#     def get_user(self, user_id):
#         print("2")
#         try:
#             return User.objects.get(pk=user_id)
#         except User.DoesNotExist:
#             return None

from core.helpers import api_response
from rest_framework import generics
from core.serializers.auth_serializers import MyTokenObtainPairSerializer

from core.models.users_model import User


class LoginAPIView(generics.GenericAPIView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request):
        try:
            user = User.objects.get(email = request.data['email'])
            credentials = {'username':user.username, 'password':request.data['password']}
            serializer = self.serializer_class(data=credentials)
        except:
            serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            return api_response(200, "Login success", serializer.data["tokens"], status=True)
        else:
            errors_list = [serializer.errors[error][0] for error in serializer.errors]
            return api_response(400, errors_list[0], {}, status=False)