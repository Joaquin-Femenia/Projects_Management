# Generated by Django 5.1.3 on 2025-01-15 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_project_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='priority',
            field=models.CharField(choices=[('Low', 'Baja'), ('Medium', 'Media'), ('High', 'Alta')], default='Low', max_length=6),
        ),
    ]
