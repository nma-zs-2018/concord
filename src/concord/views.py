from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import login as djangoLogin
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def login_verification(request, payload = None):
    return render(request, 'is_logged_in.html', payload)

def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     return index(request, {"username" : user.username + str()})
    # else:
    #     return login(request)
    return login_verification(request, {"user" : user})
