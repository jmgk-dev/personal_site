from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
	path("", views.Home.as_view(), name="home"),
	path("project/<slug:slug>", views.ProjectDetail.as_view(), name="project_detail"),
	path("add-project/", views.AddProject.as_view(), name="add_project"),
	path("update-project/<slug:slug>", views.UpdateProject.as_view(), name="update_project"),
	path("contact/", views.contact_page, name="contact"),
	path("about/", views.about_page, name="about"),
	path("success/", views.success_page, name="success_page"),
	path("login/", views.SiteLogin.as_view(), name="login"),
    path("logout/", views.SiteLogout.as_view(), name="logout"),
]
