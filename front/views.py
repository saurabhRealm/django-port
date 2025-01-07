from django.shortcuts import render
from home.models import Post , Home
# Create your views here.

def index(request):
    home = Home.objects.filter(slug="home").first()
    return render(request ,'front/index.html' , {'home': home})