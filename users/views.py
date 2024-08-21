from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import login

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(req):
        if req.method =="POST":
            form = NewUserForm(req.POST)
            if form.is_valid():
                user = form.save()
                login(req,user)
                return HttpResponseRedirect('http://127.0.0.1:8000/')
        form = NewUserForm()
        return render(req,"users/register.html",context={"form":form})



def logout_user(req):
    logout(req)
    return HttpResponseRedirect("http://127.0.0.1:8000/")



def profile(req):
    image = "mysite/images/Noname.jpg"
    return render(req,"users/profile.html",context={"image":image})