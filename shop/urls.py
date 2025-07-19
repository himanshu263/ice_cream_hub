from django.contrib import admin
from django.urls import path
from shop import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('icecream/', views.icecream, name='icecream'),
    path('blog/', views.blog, name='blog'),

]



