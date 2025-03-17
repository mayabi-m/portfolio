from django.contrib import admin
from .models import Project, Certification, Testimonial

# Register your models here.
admin.site.register(Project)
admin.site.register(Certification)
admin.site.register(Testimonial)