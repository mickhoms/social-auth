from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client


def account_confirm_email(request, key):
    return HttpResponseRedirect("http://localhost:4200/confirm?key=" + key)


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = "http://localhost:4200/confirm/"
    client_class = OAuth2Client


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    callback_url = "http://localhost:4200/confirm/"
    client_class = OAuth2Client
