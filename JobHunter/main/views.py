from django.shortcuts import render,render_to_response
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,JsonResponse
from main.models import Post,Entrepreneur_content,Student_content,LikeList,ViewList
from django.contrib.auth.models import User
from django.contrib import auth
import json
from django.core.validators import validate_email
from django.db.models import Sum


""" 以後新建新的view都用這個

def CustomFunction(request):
    content = {}
    content['currentUser'] = request.session.get('as',None)
    content['id'] = request.session.get('user',None)

    return render(request,'main/',content)

"""


# Create your views here.
def index(request):
    content = {}
    content['currentUser'] = request.session.get('as',None)
    content['id'] = request.session.get('user',None)
    titles={}
    titles['品管工程師']=Post.objects.filter(title='品管工程師').aggregate(Sum('like'))['like__sum']
    titles['資安工程師']=Post.objects.filter(title='資安工程師').aggregate(Sum('like'))['like__sum']
    titles['軟體測試工程師']=Post.objects.filter(title='軟體測試工程師').aggregate(Sum('like'))['like__sum']
    titles['數據分析師']=Post.objects.filter(title='數據分析師').aggregate(Sum('like'))['like__sum']

    
    titles_title=sort_by_value(titles)
    title_value=[i for i in sorted(titles.values(),reverse=True)]
    content['job_like_rank']={'title':titles_title,'like':title_value}
    first_title=titles_title[0]
    post_list=Post.objects.filter(title=first_title)
    entrepreneur_list=list(set([ent.entrepreneur for ent in post_list]))
    content_list=[]
    for ent in entrepreneur_list:
        content_list.append(Entrepreneur_content.objects.get(entrepreneur=ent))
    content['first_title_list']=[ con.companytitle for con in content_list][:5]
    
    second_title=titles_title[1]
    post_list=Post.objects.filter(title=second_title)
    entrepreneur_list=list(set([ent.entrepreneur for ent in post_list]))
    content_list=[]
    for ent in entrepreneur_list:
        content_list.append(Entrepreneur_content.objects.get(entrepreneur=ent))
    content['second_title_list']=[ con.companytitle for con in content_list][:5]
    
    third_title=titles_title[2]
    post_list=Post.objects.filter(title=third_title)
    entrepreneur_list=list(set([ent.entrepreneur for ent in post_list]))
    content_list=[]
    for ent in entrepreneur_list:
        content_list.append(Entrepreneur_content.objects.get(entrepreneur=ent))
    content['third_title_list']=[ con.companytitle for con in content_list][:5]
    
    return render(request, 'main/main.html',content)

def about(request):
    content = {}
    content['currentUser'] = request.session.get('as',None)
    content['id'] = request.session.get('user',None)
    return render(request, 'main/about.html',content)

def joinus(request):
    content = {}
    content['currentUser'] = request.session.get('as',None)
    content['id'] = request.session.get('user',None)
    return render(request, 'main/joinus.html',content)

def jobs(request,page=1):  #

    content = {}

    content['currentUser'] = request.session.get('as',None)
    content['id'] = request.session.get('user',None)
    
    if request.is_ajax():
        postid = request.POST.get('postid')
        post_detail = Post.objects.get(postid=postid)
        companytitle = Entrepreneur_content.objects.get(
            entrepreneur=post_detail.entrepreneur
        ).companytitle
        post_content = {
            "postid": post_detail.postid,
            "companytitle": companytitle,
            "jobtype": post_detail.jobtype,
            "title": post_detail.title,
            "detail": post_detail.detail,
            "condition": post_detail.condition,
            "benefit": post_detail.benefit,
            "contact": post_detail.contact,
            "min_salary": post_detail.min_salary,
            "viewed": post_detail.viewed,
            "like": post_detail.like,
            "post_date": post_detail.post_date,
        }


        current_post=Post.objects.get(postid=postid)
        current_student=User.objects.get(username=request.session.get('user',None))
        if not ViewList.objects.filter(student=current_student,post=current_post).exists():
            ViewList.objects.create(student=current_student,
                post=current_post)
            current_post.viewed+=1
            current_post.save()

        return JsonResponse(post_content)

    # 需要事先取得最大頁數
    max_page = 99


    content['page'] = page
    content['pagehtml'] = ''

    # 控制上一頁、下一頁按鈕 #
    if page==1:
        content['previouspage_href'] = '#'
        content['previouspage_li_class'] = ' class=\"disabled\"'
    else:
        content['previouspage_href'] = '/main/jobs/' + str(page-1)

    if page<99:
        content['nextpage_href'] = '/main/jobs/' + str(page+1)
    else:
        content['nextpage_href'] = '#'
        content['nextpage_li_class'] = ' class=\"disabled\"'
    
    # 依照目前頁數做出合理的頁數按鈕  ex. 目前第3頁 < 1 2 '3' 4 5 > 目前第15頁 < 11 12 13 14 '15' >
    if page<=5:
        for i in range(1,6):
            if i==page:
                content['pagehtml'] += '<li class="active"><a href="#">{0}</a></li>\n'.format(page)
            else:
                content['pagehtml'] += '<li><a href="/main/jobs/{0}/">{0}</a></li>\n'.format(i)
    elif page>=6:
        for i in range(page-4,page+1):
            if page==i:
                content['pagehtml'] += '<li class="active"><a href="#">{0}</a></li>\n'.format(page)
            else:
                content['pagehtml'] += '<li><a href="/main/jobs/{0}">{0}</a></li>\n'.format(i)


    # Get All post
    post_list = Post.objects.all().order_by('-postid')
    companytitleList = [
        Entrepreneur_content.objects.get(
            entrepreneur=single.entrepreneur
        ).companytitle
        for single in post_list
    ]
    for p, t in zip(post_list, companytitleList):
        p.comTitle = t

    
    content['posts']=post_list[page*20-20:page*20]
    
    return render(request, 'main/jobs.html', content)



@login_required
def member(request):
    if request.session.get('as',None) != 'student':
        return HttpResponseRedirect('/login/member/')
    else:
        uid=request.session.get('user',None)
        user=User.objects.get(username=uid)
        info=Student_content.objects.get(student=user)
        
        content = {}
        content['currentUser'] = request.session.get('as',None)
        content['id'] = request.session.get('user',None)
        content['user_detail'] = {'username':user.username,
                    'email':user.email,
                    'lastname':user.last_name,
                    'firstname':user.first_name,
                    'ntust_id':info.mis_id,
                    'resume':info.resume }
        content['msg_status'] = 'none'

        return render(request,'main/member.html',content)

@login_required
def company(request):
    if request.session.get('as',None)!= 'entrepreneur':
        return HttpResponseRedirect('/login/company/')
    else:
        uid=request.session.get('user',None)
        user=User.objects.get(username=uid)
        posts=Post.objects.filter(entrepreneur=user)
        info=Entrepreneur_content.objects.get(entrepreneur=user)
        content = {}
        content['currentUser'] = request.session.get('as',None)
        content['id'] = request.session.get('user',None)
        content['company_detail']={
            "id":user.username,
            'companytitle':info.companytitle,
            'email':user.email,
            'lastname':user.last_name,
            'firstname':user.first_name,
            "title":info.companytitle,
            "phone":info.phone,
            "address":info.address,
            "intro":info.introduction
        }
        content['msg_status'] = 'none'

        return render(request,'main/company.html',content)

@login_required
def like(request,postid):
  
    current_post=Post.objects.get(postid=postid)
    current_student=User.objects.get(username=request.session.get('user',None))
    if not LikeList.objects.filter(student=current_student,post=current_post).exists():
        LikeList.objects.create(student=current_student,
            post=current_post)
        current_post.like+=1
        current_post.save()
        return JsonResponse({'likestatus':True})
    else:
        return JsonResponse({'likestatus':False})

        
@login_required
def logout(request):
    auth.logout(request)
    return render(request,'main/main.html')

def post(request):
    if request.session.get('as',None)!= 'entrepreneur':
        return HttpResponseRedirect('/main/')
    else:
        content = {}
        content['currentUser'] = request.session.get('as',None)
        content['id'] = request.session.get('user',None)

        uid=request.session.get('user',None)
        user=User.objects.get(username=uid)
        info=Entrepreneur_content.objects.get(entrepreneur=user)

        content['companytitle']=info.companytitle

        return render(request,'main/post.html',content)


def post_action(request):
    if ((request.session.get('user',None) is not None) and
    (request.session.get('as',None)=='entrepreneur')):
        uid=request.session.get('user',None)
        company=User.objects.get(username=uid)
        numOfPost=len(Post.objects.all())
        companytitle=request.POST.get('companytitle')
        jobtype=request.POST.get('jobtype')
        title=request.POST.get('title')
        detail=request.POST.get('detail')
        condition=request.POST.get('condition')
        benefit=request.POST.get('benefit')
        phone=request.POST.get('contact')
        min_salary=request.POST.get('min_salary')
        Post.objects.create(postid=(numOfPost+1),
        entrepreneur=company,
        jobtype=jobtype,
        title=title,
        detail=detail,
        condition=condition,
        benefit=benefit,
        contact=contact,
        min_salary=min_salary,
        viewed=0,
        like=0,
        )
        return HttpResponseRedirect('/main/')
    else:
        return HttpResponseRedirect('/main/')


    
@login_required
def member_update(request):
    if ((request.session.get('user',None) is not None) and
    (request.session.get('as',None)=='student')):
        uid=request.session.get('user',None)
        student=User.objects.get(username=uid)
        content=Student_content.objects.get(student=student)

        student.email=request.POST.get('email')
        student.last_name=request.POST.get('lastname')
        student.first_name=request.POST.get('firstname')

        content.mis_id=request.POST.get('mis_id')
        content.resume=request.POST.get('resume')

        student.save()
        content.save()

        return HttpResponseRedirect('/main/member/')
    else:
        return HttpResponseRedirect('/main/member/')



def company_update(request):
    if ((request.session.get('user',None) is not None) and
    (request.session.get('as',None)=='entrepreneur')):
        uid=request.session.get('user',None)
        company=User.objects.get(username=uid)
        content=Entrepreneur_content.objects.get(entrepreneur=company)

        company.email=request.POST.get('email')
        company.last_name=request.POST.get('lastname')
        company.first_name=request.POST.get('firstname')

        content.title=request.POST.get('username')
        content.phone=request.POST.get('phone')
        content.address=request.POST.get('address')
        content.intro=request.POST.get('intro')

        company.save()
        content.save()
    
        return HttpResponseRedirect('/main/company/')
    return HttpResponseRedirect('/main/company/')

@login_required
def company_update_pwd(request):
    if request.session.get('user',None) is not None:
        uid=request.session.get('user',None)
        pwd=request.POST.get('newpwd')
        cpwd=request.POST.get('confirm_newpwd')
        if pwd!=cpwd:
            request.session['user']=uid
            return render(request,'main/company.html',{'msg':"確認密碼不正確",'msg_status':'block'})
        else:
            user=User.objects.get(username=uid)
            user.set_password(pwd)
            user.save()
            request.session['user']=uid
            auth.login(request,user)
            return HttpResponseRedirect('/main/company/')

    else:
        return HttpResponseRedirect('/main/')

@login_required
def member_update_pwd(request):
    if request.session.get('user',None) is not None:
        uid=request.session.get('user',None)
        pwd=request.POST.get('newpwd')
        cpwd=request.POST.get('confirm_newpwd')
        if pwd!=cpwd:
            request.session['user']=uid
            return render(request,'main/member.html',{'msg':"確認密碼不正確",'msg_status':'block'})
        else:
            user=User.objects.get(username=uid)
            user.set_password(pwd)
            user.save()
            request.session['user']=uid
            auth.login(request,user)
            return HttpResponseRedirect('/main/member/')

    else:
        return HttpResponseRedirect('/main/')    


@login_required
def likedList(request):
    if request.session.get('as',None) == 'student':
        uid=request.session.get('user',None)
        content = {}
        content['currentUser'] = request.session.get('as',None)
        content['id'] = uid

        student=User.objects.get(username=uid)
        like_list=LikeList.objects.filter(student=student).order_by('-id')
        post_list=[like.post for like in like_list]
        
        companytitleList = [
            Entrepreneur_content.objects.get(
                entrepreneur=single.entrepreneur
            ).companytitle
            for single in post_list
        ]
        for p, t in zip(post_list, companytitleList):
            p.comTitle = t

        content['posts']=post_list
        if len(post_list) ==0 :
            content['likelist_null'] = '<tr class="no-result text-center"><td colspan="8">現在還沒有最愛的工作喔！</td></tr>'
        return render(request,'main/liked.html',content)
    else:
        return HttpResponseRedirect('/main/')    



@login_required
def dislike(request):
    if request.session.get('as',None) == 'student':
        uid=request.session.get('user',None)
        post_id=request.POST.get('postid')

        content = {}
        content['currentUser'] = request.session.get('as',None)
        content['id'] = uid

        user=User.objects.get(username=uid)
        p=Post.objects.get(postid=post_id)

        liked=LikeList.objects.get(student=user,post=p)
        liked.delete()

        return JsonResponse({'dislike_status':True})

    else:
        return HttpResponseRedirect('/main/')    
    
























































# algorithm
def sort_by_value(d): 
    items=d.items() 
    backitems=[[v[1],v[0]] for v in items] 
    backitems.sort(reverse=True) 
    return [ backitems[i][1] for i in range(0,len(backitems))] 