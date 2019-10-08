from django.urls import path

from main.views import (
    about,
    company,
    company_update,
    company_update_pwd,
    dislike,
    index,
    jobs,
    join_us,
    like,
    liked_list,
    logout,
    member,
    member_update,
    member_update_pwd,
    post,
    post_action,
)

urlpatterns = [
    path("", index),
    path("about/", about),
    path("join-us/", join_us),
    path("jobs/", jobs),
    path("jobs/<int:page>/", jobs),
    path("jobs/like/<int:postid>/", like),
    # 會員中心
    path("company/", company),
    path("member/", member),
    path("company/update/", company_update),
    path("member/update/", member_update),
    # 我的最愛
    path("liked/", liked_list),
    path("dislike/", dislike),
    # 登出
    path("logout/", logout),
    # 新增職缺
    path("post/", post),
    path("post/action/", post_action),
    # 改密碼
    path("company/update_pwd/", company_update_pwd),
    path("member/update_pwd/", member_update_pwd),
]
