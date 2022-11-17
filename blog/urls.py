from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index,name='index blog'),
    # path('index/',views.index,name='index blog'),
    path('Contact/',views.contact,name='Contact'),
    path('Intro/',views.intro,name='Intro'),
    path('Service/',views.service,name='Service'),
    path('blog/',views.blog,name='Blog'),
]

