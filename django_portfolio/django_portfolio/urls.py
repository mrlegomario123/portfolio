"""django_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# paths for whole project

from django.contrib import admin
from django.urls import path, include 
urlpatterns = [
    path('admin/', admin.site.urls),
    # when navigate to /blog, include points that to blog.urls file.
    # That then points to the html content
    # include only sends remaining url afer .../blog
    # if path contaions "blog/" in, still runs, e.g. url: ".../blog/about" runs
    # leave trailing / after path as will run with or without /
    path('blog/', include('blog.urls')),
    
]
