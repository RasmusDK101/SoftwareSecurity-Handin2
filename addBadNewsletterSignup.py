import random
import string
from newsletter_signup.models import NewsletterSignup

def randomStringwithDigitsAndSymbols(stringLength):
    character_set = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(character_set) for i in range(stringLength))

def username():
    return randomStringwithDigitsAndSymbols(10)

def firstnames():
    return randomStringwithDigitsAndSymbols(10)

def lastnames():
    return randomStringwithDigitsAndSymbols(10)

def email():
    return  randomStringwithDigitsAndSymbols(8) + "@" + randomStringwithDigitsAndSymbols(5) + "." + randomStringwithDigitsAndSymbols(2)

def createNewsletterSignup():
    n = NewsletterSignup(username=username(),firstnames=firstnames(), lastnames=lastnames(), email=email())
    n.save()

for i in range(10):
    createNewsletterSignup()
