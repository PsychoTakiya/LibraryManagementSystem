# Generated by Django 3.2.5 on 2022-02-13 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMS', '0003_borrowers'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowers',
            name='bdate',
            field=models.DateField(null=True),
        ),
    ]