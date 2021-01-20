from django.contrib.auth.models import User
from rest_framework import authentication


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        token = request.META.get("Authorization")
        if token != "Bearer: 123":
            return None

        return User(), None
