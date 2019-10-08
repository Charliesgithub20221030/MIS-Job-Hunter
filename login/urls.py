from django.urls import path

from login.views import (
    company_login,
    company_login_action,
    member_login,
    member_login_action,
)

urlpatterns = [
    path("", member_login),
    path("member/", member_login),
    path("member/action/", member_login_action),
    path("company/", company_login),
    path("company/action/", company_login_action),
]
