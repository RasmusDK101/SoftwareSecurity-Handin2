from django.contrib import admin
from .models import NewsletterSignup

# Register your models here.

@admin.register(NewsletterSignup)
class NewsletterSignupAdmin(admin.ModelAdmin):
    list_display = ['username', 'firstnames', 'lastnames', 'email']
