from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from signup.forms import SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('homepage:news_list')

    else:
        form=SignupForm()
    return render(request,'signup/signup.html',{'form':form})

def change_password(request):
    if request.method == 'POST':
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,'Your Password was Successfully Updated')
            return redirect('homepage:news_list')
        else:
            messages.error(request,'Please correct the error below')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'signup/change_password.html',{'form':form})

@login_required
def home(request):
    return render(request,'signup/home.html')

