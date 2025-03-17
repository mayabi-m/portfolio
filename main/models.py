from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link =  models.URLField(blank = True)
    live_link = models.URLField(blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Certification(models.Model):
    name = models.CharField(max_length=255) 
    issuing_organization = models.CharField(max_length=255)  
    issue_date = models.DateField()
    credential_link = models.URLField(blank = True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    role = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Testimonial by {self.name}"     