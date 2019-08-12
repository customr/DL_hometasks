# Generated by Django 2.2.4 on 2019-08-08 15:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='First name')),
                ('last_name', models.CharField(max_length=35, verbose_name='Last name')),
                ('email', models.CharField(max_length=50, verbose_name='Email')),
                ('date_of_birth', models.DateField(max_length=8, verbose_name='Date of birth')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, verbose_name='Topic')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', models.CharField(max_length=250, verbose_name='Text')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating')),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=150, verbose_name='Text')),
                ('rating', models.IntegerField(default=0, verbose_name='Rating')),
                ('date_published', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date published')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Author')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post')),
            ],
        ),
    ]
