from django.shortcuts import  render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import LoginForm, SignupForm



def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/tontines/")
    return render(request, "utilisateurs/login.html", {"form": form})

def register_user(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get("username")
           raw_password = form.cleaned_data.get("password1")
           user = authenticate(username=username, password=raw_password)
           return redirect("/login/")
    else:
        form = SignupForm()
        return render(request, "utilisateurs/register.html",{"form": form})