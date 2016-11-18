from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.http import Http404
from .forms import MyRegistrationForm

# Create your views here.
def login_page(request):
    return render(request, "userManagementApp/index.html", {})

def login(request):
    if request.method == 'POST':
        username = request.POST.get("login")
        password = request.POST.get("password")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            return render(request, "userManagementApp/index.html", {'username':username, 'errors': True})
    raise Http404

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def reg_page(request):
    return render(request, "userManagementApp/registration.html", {"form": MyRegistrationForm})

def registration(request):
    if request.method=="POST":
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/user/")
        context = {"form": form}
        return render(request, 'userManagementApp/registration.html', context)
    context = {"form": form}
    return render(request, 'userManagementApp/registration.html', context)
