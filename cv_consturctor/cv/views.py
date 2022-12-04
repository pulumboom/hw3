from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, FileResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from pdfkit import from_string

from .models import CV, Projects


@login_required(login_url='signin')
def get_cv(request):
    try:
        cv = CV.objects.filter(user=request.user.id).values()[0]

        context = {
            'cv': cv
        }

        if cv:
            try:
                projects = Projects.objects.filter(user=request.user)
                context['projects'] = projects
            except:
                pass
    except:
        context = {}

    return render(request, 'cv.html', context)


@login_required(login_url='signin')
def projects(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('tel')
        email = request.POST.get('email')
        languages = request.POST.get('languages')
        technologies = request.POST.get('technologies')
        university_name = request.POST.get('university_name')
        graduation_date = request.POST.get('graduation_date')
        faculty = request.POST.get('faculty')
        gpa = request.POST.get('gpa')

        cv, created = CV.objects.update_or_create(
            user=user,
            defaults=dict(
                first_name_draft=first_name,

                last_name_draft=last_name,

                phone_number_draft=phone_number,

                email_draft=email,

                languages_draft=languages,

                technologies_draft=technologies,

                university_name_draft=university_name,

                graduation_date_draft=graduation_date,

                faculty_draft=faculty,

                gpa_draft=gpa),
        )

    context = {
        'projects': Projects.objects.filter(user=request.user)
    }

    return render(request, 'projects.html', context)


@login_required(login_url='signin')
def create(request):
    try:
        cv = CV.objects.filter(user=request.user).values()[0]
        context = {
            'cv': cv
        }
    except:
        context = {}

    return render(request, 'create.html', context)


@login_required(login_url='signin')
def save(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('tel')
        email = request.POST.get('email')
        languages = request.POST.get('languages')
        technologies = request.POST.get('technologies')
        university_name = request.POST.get('university_name')
        graduation_date = request.POST.get('graduation_date')
        faculty = request.POST.get('faculty')
        gpa = request.POST.get('gpa')
        image = request.FILES['image']

        cv, created = CV.objects.update_or_create(
            user=user,
            defaults=dict(
                image=image,
                image_draft=image,

                first_name=first_name,
                first_name_draft=first_name,

                last_name=last_name,
                last_name_draft=last_name,

                phone_number=phone_number,
                phone_number_draft=phone_number,

                email=email,
                email_draft=email,

                languages=languages,
                languages_draft=languages,

                technologies=technologies,
                technologies_draft=technologies,

                university_name=university_name,
                university_name_draft=university_name,

                graduation_date=graduation_date,
                graduation_date_draft=graduation_date,

                faculty=faculty,
                faculty_draft=faculty,

                gpa=gpa,
                gpa_draft=gpa),
        )

    return redirect('cv')


@login_required(login_url='signin')
def draft(request):
    if request.method == "POST":
        user = request.user
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('tel')
        email = request.POST.get('email')
        languages = request.POST.get('languages')
        technologies = request.POST.get('technologies')
        university_name = request.POST.get('university_name')
        graduation_date = request.POST.get('graduation_date')
        faculty = request.POST.get('faculty')
        gpa = request.POST.get('gpa')

        cv, created = CV.objects.update_or_create(
            user=user,
            defaults=dict(
                first_name_draft=first_name,

                last_name_draft=last_name,

                phone_number_draft=phone_number,

                email_draft=email,

                languages_draft=languages,

                technologies_draft=technologies,

                university_name_draft=university_name,

                graduation_date_draft=graduation_date,

                faculty_draft=faculty,

                gpa_draft=gpa),
        )

    return redirect('cv')


@login_required(login_url='signin')
def add_project(request):
    if request.method == 'POST':
        user = request.user
        project_name = request.POST.get('project_name')
        project_description = request.POST.get('project_description')

        project = Projects(
            user=user,
            project_name=project_name,
            project_name_draft=project_name,
            project_description=project_description,
            project_description_draft=project_description
        )
        project.save()
        return redirect('projects')

    return render(request, 'add_project.html')


@login_required(login_url='singin')
def delete(request, id):
    project = Projects.objects.filter(user=request.user, id=id)
    project.delete()
    return redirect('projects')


@login_required(login_url='signin')
def pdf(request):
    cv = CV.objects.filter(user=request.user.id).values()[0]

    context = {
        'cv': cv
    }
    template = get_template('pdf.html')
    html = template.render(context)
    pdf_file = from_string(html, False)

    return HttpResponse(pdf_file, content_type='application/pdf')


def view_404(request, exception=None):
    return redirect('cv')
