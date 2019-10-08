from django.urls import path

from sign_up.views import (
    company_sign_up,
    company_sign_up_action,
    member_sign_up,
    member_sign_up_action,
)

urlpatterns = [
    path("", member_sign_up),
    path("member/", member_sign_up),
    path("member/action/", member_sign_up_action),
    path("company/", company_sign_up),
    path("company/action/", company_sign_up_action),
]
