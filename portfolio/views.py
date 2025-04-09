import os

import requests

from django.http import HttpResponse

from .forms import AddProjectForm, UpdateProjectForm, AddLanguageForm, UpdateLanguageForm

from django.shortcuts import render, redirect
# from django.conf import settings
# from django.contrib import messages

# from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy

from .models import Project, Language

from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from PIL import Image



class Home(ListView):

    queryset = Project.objects.all()
    template_name = "portfolio/home_page.html"


class ProjectDetail(DetailView):

    model = Project

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    template_name = 'portfolio/project_detail.html'


class AddProject(LoginRequiredMixin, FormView):

    login_url = "portfolio:login"

    form_class = AddProjectForm
    template_name = 'portfolio/add_project.html'

    def form_valid(self, form):
        image = form.cleaned_data["image"]
        title = form.cleaned_data["title"]
        image_title = f"{title}.png"

        with Image.open(image.file) as img:
            img.thumbnail((1500,1000), Image.LANCZOS)

            with NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                img.save(temp_file, format='PNG', progressive=True, optimize=True)
                form.instance.image = File(temp_file, name=image_title)

                form.save()

        return redirect("portfolio:success_page")


class UpdateProject(LoginRequiredMixin, UpdateView):

    login_url = "portfolio:login"

    model = Project

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    form_class = UpdateProjectForm
    template_name = 'portfolio/update_project.html'

    success_url = reverse_lazy("portfolio:success_page")



class AddLanguage(LoginRequiredMixin, FormView):

    login_url = "portfolio:login"

    form_class = AddLanguageForm
    template_name = 'portfolio/add_language.html'

    def form_valid(self, form):
        logo = form.cleaned_data["logo"]
        title = form.cleaned_data["title"]
        logo_title = f"{title}.png"

        with Image.open(logo.file) as img:
            img.thumbnail((500,500), Image.LANCZOS)

            with NamedTemporaryFile(suffix=".png", delete=False) as temp_file:
                img.save(temp_file, format='PNG', progressive=True, optimize=True)
                form.instance.logo = File(temp_file, name=logo_title)

                form.save()

        return redirect("portfolio:success_page")


class UpdateLanguage(LoginRequiredMixin, UpdateView):

    login_url = "portfolio:login"

    model = Language

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    form_class = UpdateLanguageForm
    template_name = 'portfolio/update_language.html'

    success_url = reverse_lazy("portfolio:success_page")


def contact_page(request):
    return render(request, "portfolio/contact_page.html")


def about_page(request):
    return render(request, "portfolio/about_page.html")


def success_page(request):
    return render(request, "portfolio/success_page.html")


class SiteLogin(LoginView):
    form = AuthenticationForm
    template_name = "portfolio/login.html"
    next_page = "portfolio:home"
    redirect_authenticated_user = True


class SiteLogout(LogoutView):
    next_page = "kinorg:home"