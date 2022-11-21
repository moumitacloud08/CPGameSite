from django.shortcuts import render



# Create your views here.

def recharge(request):
    return render(request, 'myaccount/myaccount.html' )
