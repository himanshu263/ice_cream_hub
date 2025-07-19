from django.shortcuts import render
from .models import Contact
from django.contrib import messages
from .models import IceCream
from .models import Testimonial
from .models import Service
# Create your views here.

def index(request):
    icecreams = IceCream.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    context = {
        'icecreams': icecreams,
        'services': services,
        'testimonials': testimonials,
    }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')  

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        contact_obj = Contact(name=name, email=email, phone=phone, message=message)
        contact_obj.save()

        messages.success(request, "Your message has been sent successfully!")
        return render(request, 'contact.html')
    
    return render(request, 'contact.html')


def icecream(request):
    icecreams = IceCream.objects.all()
    return render(request, 'icecream.html', {'icecreams': icecreams})

def blog(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'blog.html', {'testimonials': testimonials})