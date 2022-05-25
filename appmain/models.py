from django.db import models
from categories.models import Category
# Create your models here.


class Project(models.Model):
    project_name    = models.CharField(max_length=200, unique=True)
    github_link     = models.CharField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    images          = models.ImageField(upload_to='photos/projects')
    category        = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)


    


    def __str__(self):
        return self.project_name


class MailingList(models.Model):
    email = models.CharField(max_length=250, blank=False)
    isSubscribed = models.BooleanField(default=True)

    def __str__(self):
        return self.email