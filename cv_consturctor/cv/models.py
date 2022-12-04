from django.db import models
from django.utils.datetime_safe import datetime
from django.contrib.auth.models import User


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    image_draft = models.ImageField(blank=True, null=True, upload_to='images/')

    first_name = models.CharField(max_length=50, blank=True, null=True)
    first_name_draft = models.CharField(max_length=50, blank=True, null=True)

    last_name = models.CharField(max_length=50, blank=True, null=True)
    last_name_draft = models.CharField(max_length=50, blank=True, null=True)

    phone_number = models.CharField(max_length=12, blank=True, null=True)
    phone_number_draft = models.CharField(max_length=12, blank=True, null=True)

    email = models.EmailField(blank=True, null=True)
    email_draft = models.EmailField(blank=True, null=True)

    languages = models.CharField(max_length=255, blank=True, null=True)
    languages_draft = models.CharField(max_length=255, blank=True, null=True)

    technologies = models.CharField(max_length=255, blank=True, null=True)
    technologies_draft = models.CharField(max_length=255, blank=True, null=True)

    university_name = models.CharField(max_length=255, default=datetime.now())
    university_name_draft = models.CharField(max_length=255, blank=True, null=True)

    graduation_date = models.DateField(blank=True, null=True)
    graduation_date_draft = models.DateField(blank=True, null=True)

    faculty = models.CharField(max_length=255, blank=True, null=True)
    faculty_draft = models.CharField(max_length=255, blank=True, null=True)

    gpa = models.FloatField(blank=True, null=True)
    gpa_draft = models.FloatField(blank=True, null=True)

    # photo = models.FileField()


class Projects(models.Model):
    project_name = models.CharField(max_length=60)
    project_name_draft = models.CharField(max_length=60)

    project_description = models.CharField(max_length=255, null=True)
    project_description_draft = models.CharField(max_length=255, null=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
