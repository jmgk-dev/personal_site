from django import forms
from .models import Project

class AddProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ['title', 'description', 'link', 'image']


class UpdateProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ['title', 'description', 'link', 'image']



