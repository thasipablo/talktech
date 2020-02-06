from django.shortcuts import render

# BLOG VIEWS

def home(request):
    return render(request, 'blog/home.html')
