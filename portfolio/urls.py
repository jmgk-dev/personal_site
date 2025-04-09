from django.urls import path

from . import views

app_name = "portfolio"
urlpatterns = [
	path("", views.Home.as_view(), name="home"),
	path("project/<slug:slug>", views.ProjectDetail.as_view(), name="project_detail"),
	path("add-project/", views.AddProject.as_view(), name="add_project"),
	path("update-project/<slug:slug>", views.UpdateProject.as_view(), name="update_project"),
	path("add-language/", views.AddLanguage.as_view(), name="add_language"),
	path("update-language/<slug:slug>", views.UpdateLanguage.as_view(), name="update_language"),
	path("contact/", views.contact_page, name="contact"),
	path("about/", views.about_page, name="about"),
	path("success/", views.success_page, name="success_page"),
	path("login/", views.SiteLogin.as_view(), name="login"),
    path("logout/", views.SiteLogout.as_view(), name="logout"),
]
