from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def loginuser(request):
    if request.method=='POST':
      user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
      if user is None:
            return render(request, 'login/login.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
      else:
            login(request, user)
            return HttpResponseRedirect("/home/")
    else:
      return render(request, 'login/login.html' )