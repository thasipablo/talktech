from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html', {'active':'active'})

def about(request):
    return render(request, 'pages/about.html', {'active':'active'})