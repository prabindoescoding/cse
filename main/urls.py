from django.conf import settings                   #user added to deploy static files
from django.conf.urls.static import static

from main import views
from django.urls import path

urlpatterns = [
    path('',views.landingPage,name="landing page"),
    path('index',views.landingPage,name='landingPage'),
    path('courses',views.courses,name="courses"),
    path('about',views.about,name="About page"),
    path('admissionForm',views.admissionForm,name="admission page"),
    path('contactus',views.contact,name="contact page"),
    path('plans',views.plans,name="plans page"),
    path('patners',views.patners,name="patners page"),
    path('mail',views.mailtest,name='mail page')

]
