from django.shortcuts import render
from home.models import Post , Home
# Create your views here.

def index(request):
    home = Home.objects.filter(slug="home").first()
    aboutus = Home.objects.filter(slug="about").first()
    recenteducation = Home.objects.filter(slug="recenteducation")
    honors = Home.objects.filter(slug="honors_and_awards").first()

    skills = Home.objects.filter(slug="skills")
    experience = Home.objects.filter(slug="experience")
    project = Home.objects.filter(slug="project")
    certifications = Home.objects.filter(slug="certifications")

    return render(request ,'front/index.html' , {'home': home , 'aboutus': aboutus , 'recenteducation': recenteducation , 'honors': honors , 'skills': skills , 'experience': experience , 'project': project , 'certifications': certifications})