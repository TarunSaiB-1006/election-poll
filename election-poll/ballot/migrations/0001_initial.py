# Generated by Django 5.2.3 on 2025-06-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_class', models.CharField(choices=[('IX', 'IX'), ('XI', 'XI')], max_length=3)),
                ('section', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=3)),
                ('post_preference_1', models.CharField(max_length=50)),
                ('post_preference_2', models.CharField(blank=True, max_length=50, null=True)),
                ('number_of_votes', models.PositiveIntegerField(default=0, editable=False)),
                ('logo_path', models.ImageField(upload_to='ballot/logos/')),
                ('image_path', models.ImageField(upload_to='ballot/candidate_images/')),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
    ]
