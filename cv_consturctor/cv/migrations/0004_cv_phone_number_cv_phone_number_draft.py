# Generated by Django 4.1.3 on 2022-11-30 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_remove_projects_cv_cv_faculty_cv_faculty_draft_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='phone_number_draft',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
