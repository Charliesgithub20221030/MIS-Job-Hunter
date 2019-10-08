from django.urls import path

from signup.views import (
    company_signup,
    company_signup_action,
    member_signup,
    member_signup_action,
)

urlpatterns = [
    path("", member_signup),
    path("member/", member_signup),
    path("member/action/", member_signup_action),
    path("company/", company_signup),
    path("company/action/", company_signup_action),
]
