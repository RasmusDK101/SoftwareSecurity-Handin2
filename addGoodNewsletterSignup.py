from newsletter_signup.models import NewsletterSignup
from pronounceable import PronounceableWord


def username():
    return PronounceableWord().length(8, 15)

def firstnames():
    return PronounceableWord().length(8, 15)

def lastnames():
    return PronounceableWord().length(8, 15)

def email():
    return PronounceableWord().length(8, 15) + "@" + PronounceableWord().length(8, 15) + "." + PronounceableWord().length(2, 3)

def createNewsletterSignup():
    n = NewsletterSignup(username=username(),firstnames=firstnames(), lastnames=lastnames(), email=email())
    n.save()

for i in range(10):
    createNewsletterSignup()
