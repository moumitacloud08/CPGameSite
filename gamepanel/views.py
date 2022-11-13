from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import NumberMaster
from django.contrib.auth import  logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect




# Create your views here.

def loginpage(request):
    return render(request, 'login/login.html')

def game(request):
    numberList= NumberMaster.objects.all()
    return render(request, 'gpanel/panel.html' ,{'numberList':numberList})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginpage')
       # return HttpResponseRedirect("")

