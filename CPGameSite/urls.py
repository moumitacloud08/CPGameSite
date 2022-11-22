"""CPGameSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from gamepanel import views as gpanelview
from home import views as homeviews
from login import views as loginviews
from myaccount import views as accountviews


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginviews.loginuser , name='loginuser'),
    path('home/', homeviews.home, name='home'),
    path('game/', gpanelview.game , name='panel'),
    path('logout/', gpanelview.logoutuser, name='logoutuser'),
    path('', gpanelview.loginpage, name='loginpage'),
    path('myaccount/', accountviews.myaccount, name='myaccount'),
    path('recharge/', accountviews.recharge, name='recharge'),
    path('transaction/', accountviews.transaction, name='transaction'),
]
