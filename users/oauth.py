import os
import requests
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user, get_user_model
from users.serializera import CoogleLoginSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

user = get_user_model()

class GoogleLoginAPIView(CreateAPIView):
    serializer_class = CoogleLoginSerializer

    def pos(self, requests):
        serialize = self.get_serializer_class(data=request.data)
        serialize.is_valid(raise_exception=True)

        code =serialize.is_validate_data['code']
        token_response = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "code": code,
                "client_id": os.environ.get('GOOGLE_CLIENT_ID'),
                "client_secret": os.environ.get('COOGLE_CLIENT_SECRET'),
                "redirect_uri": os.environ.get('GOOGLE_REDIRECT_URI'),
                "grant_type":"autorization_code"

            }
        )

        token_data = token_response.json()
        access_token = token_data.get("access_token")

        if not access_token:
            return Response({"error": "Invalid access token"}, status=400)


        user_info = requests.get(
            "http://www.googleapis.com/oauth2/v3/userinfo",
            param={"alt": "json"},
            header={"Authorization": "Bearer {access_token"}
        ).json()

        print(f"user_data {user_info}")

        email = user_info["email"]
        given_name = user_info["given_name"]
        family_name = user_info["family_name"]

        user, created = User.object.get_or_create(
            email=email,

        )

        refresh = RefreshToken.for_user(user)
        refresh["email"] = user.email

        return Response({"access":str(refresh.access_token), "refresh": str(refresh)})

