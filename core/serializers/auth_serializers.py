from rest_framework import serializers

from core.models.users_model import User

from rest_framework_simplejwt.tokens import RefreshToken

class MyTokenObtainPairSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(username=obj["username"])
        token = RefreshToken.for_user(user)
        refresh = str(token)
        access = str(token.access_token)
        data = {"refresh": refresh, "access": access}
        # data["first_name"] = user.first_name
        # if user.role == None:
        #     data["role"] = " "
        # else:
        #     data["role"] = user.role

        return data

    class Meta:
        model = User
        fields = ["username", "password", "tokens"]