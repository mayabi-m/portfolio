from django.shortcuts import render
from .models import Project, Certification, Testimonial
# Create your views here.
def home(request):
    testimonials = Testimonial.objects.all()
    return render(request, "main/home.html", {"testimonials":testimonials})

def projects(request):
    projects = Project.objects.all()
    return render(request, "main/projects.html", {"projects":projects})

def contact(request):
    return render(request, "main/contact.html")