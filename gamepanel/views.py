from django.shortcuts import render
from django.http import HttpResponse
from .models import NumberMaster

# Create your views here.



def game(request):
    numberList= NumberMaster.objects.all()
    return render(request, 'gpanel/panel.html' ,{'numberList':numberList})

