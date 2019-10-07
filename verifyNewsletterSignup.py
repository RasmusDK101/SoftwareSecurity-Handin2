from django.core.exceptions import ValidationError
from django.core.validators import validate_unicode_slug
from newsletter_signup.models import NewsletterSignup

def validate_name(name):
    try:
        validate_unicode_slug(name)
    except ValidationError:
        return False
    else:
        return True 

for obj in NewsletterSignup.objects.all():
    if  not validate_name(obj.username) or not validate_name(obj.firstnames) or not validate_name(obj.lastnames):
        print('Deleting db record id:{} with username:{}'.format(obj.id,obj))
        NewsletterSignup.objects.filter(id=obj.id).delete()
