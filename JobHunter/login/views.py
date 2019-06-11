from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
# Create your views here.

# 會員登入 login_action、redirect to main if member exist
def member_login(request):
	if request.user.is_authenticated and request.session.get('as',None)=='student':
		return  HttpResponseRedirect('/main/member/')
	elif request.user.is_authenticated and request.session.get('as',None)=='entrepreneur':
		return HttpResponseRedirect('/main/company/')
	else:
		return render(request,'login/memberlogin.html')

def company_login(request):
	if request.user.is_authenticated and request.session.get('as',None)=='entrepreneur':
		return HttpResponseRedirect('/main/company/')
	elif request.user.is_authenticated and request.session.get('as',None)=='student':
		return HttpResponseRedirect('/main/member/')
	else:
		return render(request,'login/companylogin.html')


#登入行為檢查
def member_login_action(request):
	content = {}
	if request.method=='POST':
		uid=request.POST.get('id')
		pwd=request.POST.get('pwd')
		user =auth.authenticate(username=uid,password=pwd)
		if (user is not None) :
			if user.groups.filter(name='student').exists():
				auth.login(request,user)
				request.session['user']=uid
				request.session['as']='student'
				return HttpResponseRedirect('/main/')
			else:
				return render(request,'login/memberlogin.html',{'msg':"User has no permission to log in"})
		else:
			return render(request,'login/memberlogin.html',{'msg':"username or password error"})
	else:
		return render(request,'login/memberlogin.html',{'msg':"not a valid login method"})





def company_login_action(request):
	content = {}
	if request.method=='POST':
		uid=request.POST.get('id')
		pwd=request.POST.get('pwd')
		user =auth.authenticate(username=uid,password=pwd)
		if (user is not None):
			if user.groups.filter(name='entrepreneur').exists():
				auth.login(request,user)
				request.session['user']=uid
				request.session['as']='entrepreneur'
				return HttpResponseRedirect('/main/')
			else:
				return render(request,'login/companylogin.html',{'msg':"User has no permission user to log in"})
		else:
			return render(request,'login/companylogin.html',{'msg':"username or password error"})
	else:
		return render(request,'login/companylogin.html',{'msg':"not a valid login method"})

