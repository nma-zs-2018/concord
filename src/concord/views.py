from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'index.html')

def chat(request):
    return render(request, 'chat.html')


def login(request):
    return render(request, 'login.html')


def login_verification(request, payload = None):
    return render(request, 'is_logged_in.html', payload)


def login_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    return login_verification(request, {"user" : user})
