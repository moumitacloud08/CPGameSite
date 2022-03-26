from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def game(request):
    return render(request, 'gpanel/panel.html')
