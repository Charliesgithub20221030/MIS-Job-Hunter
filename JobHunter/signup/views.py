from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.http import HttpResponseRedirect
from main.models import Entrepreneur_content,Student_content

# Create your views here.
def member_signup(request): #name studentId email pwd
    return render(request, 'signup/membersignup.html')
def company_signup(request):
	return render(request, 'signup/companysignup.html')

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


def member_signup_action(request):
	uid=request.POST.get('username')
	email=request.POST.get('email')
	lastn=request.POST.get('lastname')
	firstn=request.POST.get('firstname')
	mis_id=request.POST.get('mis_id')
	resume=request.POST.get('resume')
	pwd=request.POST.get('pwd')
	cpwd=request.POST.get('confirm-pwd')
	if User.objects.filter(username=uid).exists():
		return render(request, 'signup/membersignup.html',{"msg":"帳號已經被使用"})
	elif pwd != cpwd:
		return render(request, 'signup/membersignup.html',{'msg':"密碼確認錯誤"})
	else:
		group=Group.objects.get(name='student')
		User.objects.create(username=uid,email=email,first_name=firstn,last_name=lastn)
		user=User.objects.get(username=uid)
		user.set_password(pwd)
		user.save()
		group.user_set.add(user)

		stu=Student_content.objects.create(student=user,
			resume=resume,
			mis_id=mis_id)
		return HttpResponseRedirect('/login/member/')

	pass
def company_signup_action(request):
	uid=request.POST.get('id')
	email=request.POST.get('email')
	name=request.POST.get('managername')
	lastn=name[0]
	firstn=name.replace(lastn,'')
	title=request.POST.get('title')
	phone=request.POST.get('phone')
	address=request.POST.get('address')
	intro=request.POST.get('intro')
	pwd=request.POST.get('pwd')
	cpwd=request.POST.get('confirm-pwd')
	if User.objects.filter(username=uid).exists():
		return render(request, 'signup/membersignup.html',{"msg":"帳號已經被使用"})
	elif pwd != cpwd:
		return render(request, 'signup/membersignup.html',{'msg':"密碼確認錯誤"})
	else:
		# user content
		group=Group.objects.get(name='entrepreneur')
		User.objects.create(username=uid,email=email,first_name=firstn,last_name=lastn)
		user=User.objects.get(username=uid)
		user.set_password(pwd)
		user.save()
		group.user_set.add(user)

		#entrepreneur_content
		entre=Entrepreneur_content.objects.create(entrepreneur=user,
			companytitle=title,
			phone=phone,
			address=address,
			introduction=intro)


		return HttpResponseRedirect('/login/company/')
	
