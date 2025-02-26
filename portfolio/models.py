from django.db import models
from django.utils.text import slugify
from django.conf import settings

class Project(models.Model):

	title = models.CharField(
		max_length=200,
		null=False,
		unique=True,
		blank=False
		)

	description = models.TextField(
		max_length=500,
		null=False,
		blank=False
		)

	link = models.URLField(
		null=False,
		blank=False
		)

	image = models.ImageField(
		upload_to='project_images/',
		null=True,
		blank=True,
		default=None
	)

	slug = models.SlugField(
		unique=True,
		blank=True
		)

	added = models.DateTimeField(
		auto_now_add=True
		)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["title"]