#url patterns for blog app

from django.urls import path
from . import views

urlpatterns = [
    # creating path for / i.e. homepage route, specify what to run
    # views.home: function called from views, return html of what to display
    # name path, specific blog home to avoid ambiguity later
    path('',views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')

]