from django.shortcuts import render

# Create your views here.
def member_signup(request): #name studentId email pwd
    return render(request, 'signup/membersignup.html')
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


def company_signup(request):
	return render(request, 'signup/companysignup.html')
