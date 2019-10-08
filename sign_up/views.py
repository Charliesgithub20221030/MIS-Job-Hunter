from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect


def member_sign_up(request):  # name studentId email pwd
    return render(request, "sign_up/membersign_up.html")


def company_sign_up(request):
    return render(request, "sign_up/companysign_up.html")


#     公司介紹
# 產業類別：
# 電腦軟體服務業
# 產業描述：
# 資訊服務業
# 員　　工：
# 暫不提供
# 資 本 額：
# 10億
# 聯 絡 人：
# 總管理處
# 公司地址：
# 台北市中正區杭州南路一段26號8樓地圖
# 電　　話：
# 暫不提供
# 傳　　真：
# 暫不提供
# 公司網址：
# https://www.chtsecurity.com
# 相關連結：
# 更多


def member_sign_up_action(request):
    uid = request.POST.get("username")
    email = request.POST.get("email")
    lastn = request.POST.get("lastname")
    firstn = request.POST.get("firstname")
    pwd = request.POST.get("pwd")
    cpwd = request.POST.get("confirm-pwd")
    if User.objects.filter(username=uid).exists():
        return render(request, "sign_up/membersign_up.html", {"msg": "帳號已經被使用"})
    if pwd != cpwd:
        return render(request, "sign_up/membersign_up.html", {"msg": "密碼確認錯誤"})
    group = Group.objects.get(name="student")
    User.objects.create(
        username=uid, email=email, first_name=firstn, last_name=lastn
    )
    user = User.objects.get(username=uid)
    user.set_password(pwd)
    user.save()
    group.user_set.add(user)
    return HttpResponseRedirect("/login/member/")


def company_sign_up_action(request):
    uid = request.POST.get("id")
    email = request.POST.get("email")
    name = request.POST.get("managername")
    lastn = name[0]
    firstn = name.replace(lastn, "")
    pwd = request.POST.get("pwd")
    cpwd = request.POST.get("confirm-pwd")
    if User.objects.filter(username=uid).exists():
        return render(request, "sign_up/membersign_up.html", {"msg": "帳號已經被使用"})
    if pwd != cpwd:
        return render(request, "sign_up/membersign_up.html", {"msg": "密碼確認錯誤"})
    # user content
    group = Group.objects.get(name="entrepreneur")
    User.objects.create(
        username=uid, email=email, first_name=firstn, last_name=lastn
    )
    user = User.objects.get(username=uid)
    user.set_password(pwd)
    user.save()
    group.user_set.add(user)
    return HttpResponseRedirect("/login/company/")
