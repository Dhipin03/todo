# Generated by Django 4.2.5 on 2023-10-26 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_task_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('completed', 'Completed'), ('pending', 'Pending'), ('expired', 'Expired')], default='pending', max_length=10),
        ),
    ]
