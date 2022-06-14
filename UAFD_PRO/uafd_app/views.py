from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from .models import *

def index(request):
    return render(request, 'index.html')

def about(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'about.html')

def management(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'management.html')

def aboutsociety(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'aboutsociety.html')

def vision(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'vision.html')

def services(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'services.html')

def activities(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'activities.html')

def recent_activities(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'recent_activities.html')

def upcoming_activities(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'upcoming_activities.html')

def members(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'members.html')

def terms(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'terms.html')

def notifications(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'notifications.html')

def contact(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'contact.html')

def login_view(request):
    if request.method=="POST":
        username=request.POST['name']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('applicationform')
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        aadhar = request.POST['number']
        name = request.POST['name']
        userid = request.POST['userid']
        password = request.POST['password']
        phone = request.POST['phone']
      
        user = User.objects.create_user(username=name,password=password)
        Register.objects.create(user=user, aadhar=aadhar,userid=userid,phone=phone)
        return redirect('login') 
    return render(request,'signup.html', locals())


def logout_view(request):
    logout(request)
    return redirect('login')

def applicationform(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method=="POST":
        name = request.POST['name']
        fname = request.POST['fathername']
        aadharno = request.POST['aadharno']
        email= request.POST['email']
        tel = request.POST['tel']
        tel1 = request.POST['tel1']
        date = request.POST['date']
        caste= request.POST['caste']
        address= request.POST['address']
        state = request.POST['state']
        district = request.POST['district']
        pincode = request.POST['pincode']
        education = request.POST['education']
        tech = request.POST['tech']
        work = request.POST['work']
        job_applying = request.POST['job_apply']
        job_state = request.POST['job_state']
        job_district = request.POST['job_district']
        job_mandal = request.POST['job_mandal']
        image1 = request.FILES['photo1']
        image2 = request.FILES['photo2']
        fee = request.POST['fee']
        u = User.objects.filter(username=request.user.username).first()

        Application_Form.objects.create(user=u,name=name,father_name=fname,aadhar_number=aadharno,email=email,mobile=tel,phone=tel1,date=date,caste=caste,address=address,state=state,district=district,pincode=pincode,education=education,technical=tech,work_experiance=work,job_applying=job_applying,job_state=job_state,job_district=job_district,job_mandal=job_mandal,photo=image1,signature=image2,fee=fee)
        return redirect('dashboard')

    return render(request, 'application_form.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def dashboardqr(request):
    return render(request, 'dashboardqr.html')

def dashboard_card(request):
    return render(request, 'dashboard_card.html')

def aplicantdetails(request):
    if request.method=="POST":
        tid = request.POST['tid']
        u = User.objects.filter(username=request.user.username).first()
        Transaction_Id.objects.create(user=u,Transaction_Id=tid)
        return redirect('aplicantdetails1')
    return render(request,'aplicantdetails.html')
    
def aplicantdetails1(request):
    user = User.objects.get(username=request.user.username)
    data = Application_Form.objects.get(user = user)
    transaction=Transaction_Id.objects.get(user=user)
    context={'data':data,'transaction':transaction}
    return render(request,'aplicantdetails1.html',context)