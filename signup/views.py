from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login,authenticate
from signup.forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            raw_password=form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
           # return redirect('homepage:news_list')
            return HttpResponseRedirect(reverse('homepage:news_list1', kwargs={'username': user.username}))
    else:
        form=SignupForm()
    return render(request,'signup/signup.html',{'form':form})




