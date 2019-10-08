from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission, User

from main.models import (
    QA,
    Entrepreneur_content,
    LikeList,
    Post,
    Student_content,
    ViewList,
)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        "postid",
        "entrepreneur",
        "jobtype",
        "title",
        "detail",
        "condition",
        "contact",
        "benefit",
        "min_salary",
        "post_date",
        "viewed",
        "like",
    )


class Entrepreneur_contentAdmin(admin.ModelAdmin):
    list_display = (
        "entrepreneur",
        "companytitle",
        "introduction",
        "address",
        "phone",
    )


class Student_contentAdmin(admin.ModelAdmin):
    list_display = ("student", "mis_id", "resume")


class QAAdmin(admin.ModelAdmin):
    list_display = (
        "qaid",
        "student",
        "entrepreneur",
        "post",
        "content",
        "post_date",
    )


class LikeListAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "student")


class ViewListAdmin(admin.ModelAdmin):
    list_display = ("id", "post", "student")


admin.site.register(QA, QAAdmin)
admin.site.register(Student_content, Student_contentAdmin)
admin.site.register(Entrepreneur_content, Entrepreneur_contentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(LikeList, LikeListAdmin)
admin.site.register(ViewList, ViewListAdmin)
