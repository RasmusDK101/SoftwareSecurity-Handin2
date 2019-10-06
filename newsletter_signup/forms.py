from django.forms import ModelForm
from .models import NewsletterSignup

class NewsletterSignupForm(ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['username','firstnames','lastnames','email']
