from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'about_kali/index.html')

def about(request):
    return render(request,'about_kali/about.html')

def installation(request):
    return render(request,'about_kali/installation.html')

def download(request):
    return render(request,'about_kali/download.html')
    
def cantact(request):
    return render(request,'about_kali/cantact.html')