# from django.shortcuts import render
from urllib import request

from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from .forms import activate_user
from help_app.models import *
from django.http import HttpResponse, HttpRequest

from django.shortcuts import render
from django.contrib.auth.models import User

from .forms import SignUpForm, AddChild, AddWork




from django.shortcuts import render
from django.views import generic


# Create your views here.
"""
class IndexView(generic.TemplateView):
    form = AddChild
    template_name = "registration/index.html"
    child = Children.objects.all()
"""



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ActivateView(TemplateView):
    template_name = "registration/activate.html"

    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)

def index(request):
    params = {'name': '', 'on_user': request.user, 'children': Children.objects.filter(parent=request.user).all(), 'form': None}
    if request.method == 'POST':
        form = AddChild(request.POST)
        params['name'] = request.POST['name']
        params['form'] = form
        if params['name'] != '':
            child = Children()
            child.name = params['name']
            child.parent = params['on_user']
            child.save()
    else:
        params['form'] = AddChild()
    return render(request, 'registration/index.html', params)

def addwork(request):
    if Houseworks.objects.filter(parent=request.user).all().count() == 0:
        default_work1 = Houseworks()
        default_work1.job_name = 'お皿洗い'
        default_work1.point = 3
        default_work1.parent = request.user
        default_work1.save()

        default_work2 = Houseworks()
        default_work2.job_name = 'お片付け'
        default_work2.point = 3
        default_work2.parent = request.user
        default_work2.save()

    params = {'name': '', 'on_user': request.user, 'works': Houseworks.objects.filter(parent=request.user).all(), 'point': '',
              'form': None}
    if request.method == 'POST':
        form = AddChild(request.POST)
        params['name'] = request.POST['name']
        params['point'] = request.POST['point']
        params['form'] = form
        if params['name'] != '':
            new_work = Houseworks()
            new_work.job_name = params['name']
            new_work.parent = params['on_user']
            new_work.point = params['point']
            new_work.save()
    else:
        params['form'] = AddWork()
    return render(request, 'registration/addwork.html', params)
############

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"


def top(request):
    return render(request, 'help_app/top.html', {})

def login(request):
    return render(request, 'help_app/login.html', {})

def register(request):
    return render(request, 'help_app/register.html', {})


# def parent_top(request):
#     return render(request, 'help_app/parent_usersmanage.html', {})

def parent_tasklist(request):
    return render(request, 'help_app/parent_tasklist.html', {})

def parent_assign(request):
    return render(request, 'help_app/parent_assign.html', {})

def parent_taskregister(request):
    return render(request, 'help_app/parent_taskregister.html', {})

def parent_complete(request):
    return render(request, 'help_app/parent_complete.html', {})


# def child_top(request):
#     return render(request, 'help_app/child_top.html', {})

def child_tasklist(request):
    return render(request, 'help_app/child_tasklist.html', {})

def child_complete(request):
    return render(request, 'help_app/child_complete.html', {})

def child_history(request):
    return render(request, 'help_app/child_history.html', {})


def certification(request):
    return render(request, 'help_app/certification.html', {})

def parent_usersmanage(request):
    return render(request, 'help_app/parent_usersmanage.html', {})
#
# def (request):
#     return render(request, 'help_app/.html', {})




