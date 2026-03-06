# Generated migration for order and archived fields

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_remove_project_languages_delete_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='archived',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['order']},
        ),
    ]
