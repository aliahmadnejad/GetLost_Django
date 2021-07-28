from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'webApp/home.html') #taken from template folder

def about(request):
    return render(request, 'webApp/about.html')

def contactus(request):
    return render(request, 'webApp/contactus.html')

