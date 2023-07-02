from django.urls import path, re_path
from dj_rest_auth.registration.views import (
    RegisterView,
    VerifyEmailView,
    ResendEmailVerificationView,
)
from dj_rest_auth.views import (
    LoginView,
    LogoutView,
    UserDetailsView,
)

from allauth.socialaccount.views import signup

from . import views

urlpatterns = [
    path(
        "account-confirm-email/<str:key>",
        views.account_confirm_email,
        name="account_confirm_email",
    ),
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    # For Email Verification
    path(
        "account-confirm-email/",
        VerifyEmailView.as_view(),
        name="account_email_verification_sent",
    ),
    path("register/verify-email/", VerifyEmailView.as_view(), name="rest_verify_email"),
    path("signup/", signup, name="socialaccount_signup"),
    path("google/", views.GoogleLogin.as_view(), name="google_login"),
    path("facebook/", views.FacebookLogin.as_view(), name="facebook_login"),
]
