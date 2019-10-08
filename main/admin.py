from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission, User

from main.models import (
    QA,
    EntrepreneurContent,
    LikeList,
    Post,
    StudentContent,
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


class EntrepreneurContentAdmin(admin.ModelAdmin):
    list_display = (
        "entrepreneur",
        "companytitle",
        "introduction",
        "address",
        "phone",
    )


class StudentContentAdmin(admin.ModelAdmin):
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
admin.site.register(StudentContent, StudentContentAdmin)
admin.site.register(EntrepreneurContent, EntrepreneurContentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(LikeList, LikeListAdmin)
admin.site.register(ViewList, ViewListAdmin)
