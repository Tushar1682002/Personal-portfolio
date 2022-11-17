from .models import Contact
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request,'index.html')
def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email','')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        contact=Contact(name=name,email=email,phone=phone,subject=subject)
        contact.save()
    return render(request,'contact.html')

def intro(request):
    return render(request,'intro.html') 
def service(request):
    return render(request,'service.html') 
def blog(request):
    return render(request,'blog.html') 
            
