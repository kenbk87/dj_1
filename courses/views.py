from django.shortcuts import render, redirect
from courses.models import Course
from django.conf import settings


def software_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    else:
        object_list = Course.objects.all()
        return render(request, 'software.html', {
            'object_list': object_list,
            'nav': 'software'
        })


def home_view(request):
    return render(request, 'home.html', {
        'nav': 'home'
    })


def about_view(request):
    return render(request, 'about.html', {
        'nav': 'about'
    })
