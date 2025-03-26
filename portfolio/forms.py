from django import forms
from .models import Project, Language

class AddProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ['title', 'description','languages', 'link', 'image']


class UpdateProjectForm(forms.ModelForm):
	
	class Meta:
		model = Project
		fields = ['title', 'description', 'languages', 'link', 'image']


class AddLanguageForm(forms.ModelForm):
	
	class Meta:
		model = Language
		fields = ['title', 'link', 'logo']


class UpdateLanguageForm(forms.ModelForm):
	
	class Meta:
		model = Language
		fields = ['title', 'link', 'logo']


