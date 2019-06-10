from django.shortcuts import render

# Create your views here.

# 會員登入 login_action、redirect to main if member exist
def member_login(request):
	test = "hahah"
	content = {}
	if request.method=='POST':
		content['member_username']=request.POST.get('username')
		content['member_pwd']=request.POST.get('pwd')
		return render(request,'login/memberlogin.html',content)

	return render(request,'login/memberlogin.html')  
    

def company_login(request):
	content = {}
	if request.method=='POST':
		content['company_id']=request.POST.get('id')
		content['company_pwd']=request.POST.get('pwd')
		return render(request,'login/companylogin.html',content)

	return render(request,'login/companylogin.html') 
