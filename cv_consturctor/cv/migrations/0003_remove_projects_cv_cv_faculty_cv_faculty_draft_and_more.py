# Generated by Django 4.1.3 on 2022-11-30 07:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cv', '0002_remove_experiencedescriptionpoints_experience_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='cv',
        ),
        migrations.AddField(
            model_name='cv',
            name='faculty',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='faculty_draft',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='gpa',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='gpa_draft',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='graduation_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='graduation_date_draft',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='university_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cv',
            name='university_name_draft',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cv',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='email_draft',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='first_name_draft',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='languages',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='languages_draft',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='last_name_draft',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='technologies',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='technologies_draft',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Graduation',
        ),
    ]
