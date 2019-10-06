# Generated by Django 2.2.5 on 2019-09-28 09:44

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersignup',
            name='email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='newslettersignup',
            name='firstnames',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
        migrations.AlterField(
            model_name='newslettersignup',
            name='lastnames',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^[-a-zA-Z0-9_]+\\Z'), "Enter a valid 'slug' consisting of letters, numbers, underscores or hyphens.", 'invalid')]),
        ),
    ]
