from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import *
from django.contrib import messages

from store.forms import CustomUserForm


def register(request):
    form = CustomUserForm()
    if request.method == 'POST' :
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registered User Successfully Login to continue")
            return redirect('/login')

    context ={
        'form':form,
    }
    return render(request,'store/auth/register.html',context)

def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request,"You are already Logged In")
        return redirect('/')
    else:
        if request.method == "POST":
            p_email = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=p_email, password= passwd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged In successfully")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or password")
                return redirect("/register")
    return render(request,'store/auth/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged out successfully")
    return redirect("/")