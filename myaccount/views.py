from django.shortcuts import render



# Create your views here.

def myaccount(request):
    return render(request, 'myaccount/myaccount.html' )

def recharge(request):
    return render(request, 'myaccount/payment.html' )
