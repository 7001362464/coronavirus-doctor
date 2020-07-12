from corona import views
from django.conf.urls import url

urlpatterns=[
    url('welcome',views.welcome),
url('register',views.registration),
url('home',views.home),
url('own',views.ownhome),
url('give',views.give),
url('insert',views.insert),
url('login',views.login),
url('dao',views.feed),
url('save',views.save),


]