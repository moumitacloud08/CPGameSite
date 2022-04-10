from django.shortcuts import render
from django.http import HttpResponseRedirect


# Create your views here.

def login(request):
    if request.method=='POST':
      print('Login Submit')
      return HttpResponseRedirect("/home/")
    else:
      return render(request, 'login/login.html' )