from django.shortcuts import render
from django.http import HttpResponse
from .forms import NewsletterSignupForm

def signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            return render(request, 'signup.html', {'form': form})

    form = NewsletterSignupForm()
    return render(request, 'signup.html', {'form': form})
