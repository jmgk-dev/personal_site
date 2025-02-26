from django.urls import path

from . import views

app_name = "main_page"
urlpatterns = [
	path("", views.Home.as_view(), name="home"),
	path("project/<slug:slug>", views.ProjectDetail.as_view(), name="project_detail"),
	path("add-project/", views.AddProject.as_view(), name="add_project"),
	path("success/", views.success_page, name="success_page")
]
