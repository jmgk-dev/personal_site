from django.test import TestCase
from .models import Language, Project

class ProjectModelTest(TestCase):

    def setUp(self):
        self.language = Language.objects.create(
            title="Python",
            link="https://www.python.org/",
            logo=None
        )
        self.project = Project.objects.create(
            title="Personal Site",
            description="A personal website project.",
            link="https://www.example.com/",
            image=None
        )
        self.project.languages.add(self.language)

    def test_string_representation(self):
        self.assertEqual(str(self.project), self.project.title)

    def test_slug_creation(self):
        self.assertEqual(self.project.slug, "personal-site")

    def test_languages_association(self):
        self.assertIn(self.language, self.project.languages.all())

    def test_ordering(self):
        proj1 = Project.objects.create(title="Blog", description="A blog project.", link="https://www.blog.com/")
        proj2 = Project.objects.create(title="Fishing", description="A fishing project.", link="https://www.fishing.com/")
        projects = Project.objects.all()
        self.assertEqual(projects[0], proj1)
        self.assertEqual(projects[1], proj2)
        self.assertEqual(projects[2], self.project)