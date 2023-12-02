from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from datetime import date

@login_required(login_url='/login')
def index(request):
    if request.method == "POST":
        query2 = TodoList.objects.create(
            user=request.user, description=request.POST['task-description'], enddate=request.POST['task-date'])
        query2.save()
    query = Profile.objects.filter(user=request.user)
    query3 = TodoList.objects.filter(user=request.user).filter(status="pending").filter(is_imp=False)

    for val in query:
        dp = val.profilepicture

    return render(request, 'index.html', {"dp": dp, "query3": query3})


def register_user(request):

    if request.method == "POST":
        print("yes")
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        userprofile = request.FILES['userprofile']

        if password == cpassword:
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                messages.info(request, "User Name Or E-mail Exists")
                return redirect(register_user)
            else:

                query = User.objects.create(
                    username=username, email=email, password=password)
                query2 = Profile(user=query, profilepicture=userprofile)
                query.set_password(password)
                query2.save()
                query.save()
                messages.success(request, 'Successfully  Registered')
                return redirect(login_user)

        else:
            messages.info(request, "Both password dont match")
            return redirect(register_user)

    return render(request, 'register.html')


def login_user(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if username or password != "":
            query = authenticate(request, username=username, password=password)
            if query is None:
                messages.info(request, "Invalid Credentials")
            else:
                login(request, query)
                return redirect(index)
    return render(request, 'login.html')


def logout_user(request):

    logout(request)
    return redirect(login_user)

def completed(request,id):
    TodoList.objects.filter(id=id).update(status="completed",is_imp=False)
    return redirect(index)
def deleted(request,id):
    TodoList.objects.filter(id=id).update(status="deleted")
    return redirect(index)
def important(request,id):
    TodoList.objects.filter(id=id).update(is_imp=True)
    return redirect(index)
@login_required(login_url='/login')
def satus_load(request,status):
    query = Profile.objects.filter(user=request.user)

    for val in query:
        dp = val.profilepicture
    if status=="completed":
        query=TodoList.objects.filter(user=request.user).filter(status="completed")
        return render(request,'completed.html',{'query':query,"dp":dp})
    elif status=="deleted":
        query=TodoList.objects.filter(user=request.user).filter(status="deleted")
        return render(request,'deleted.html',{'query':query,"dp":dp})
    elif status=="important":
        query=TodoList.objects.filter(user=request.user).filter(is_imp=True)
        return render(request,'important.html',{'query':query,"dp":dp})
    else:
        return redirect(index)


def delete_task(request,id):
 query=TodoList.objects.filter(id=id).delete()

 return redirect(index)
def today(request):
    query = Profile.objects.filter(user=request.user)
    description=[]
    query2=TodoList.objects.filter(user=request.user).filter(status='pending')
    for val in query:
        dp = val.profilepicture
    for val in query2:
        if val.enddate==date.today():
           description.append(val.description)
   
   
    print(dict)
    return render (request,'today.html',{"description":description,"dp":dp})