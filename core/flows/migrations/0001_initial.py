# Generated by Django 3.2.9 on 2021-11-18 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=250)),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('content', models.TextField()),
                ('slug', models.SlugField(null=True, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-published_date',),
            },
        ),
    ]
