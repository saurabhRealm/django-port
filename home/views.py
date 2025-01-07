from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from datetime import datetime
from home.models import Post , Home

# Create your views here.

def index(request):
    context = {
            "variable" : "this is sent "
        }
    return render(request ,'home/index.html' , context)

def about(request):
    return HttpResponse('this is aboutpage ')

def post(request):
     posts = Post.objects.all()
     return render(request, 'home/posts/index.html', {'posts': posts})

def addpost(request):
     return render(request, 'home/posts/add.html')

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()  
    return redirect('post')


def savepost(request):
    if request.method == 'POST':
        name     = request.POST.get('name')
        desc = request.POST.get('description')
        post = Post(name=name, description=desc, date=datetime.today())
        post.save()
        return redirect('post')  

def editpost(request, post_id):
    id  = post_id
    post = Post.objects.filter(id=post_id).first()
    if request.method == 'POST':
        name     = request.POST.get('name')
        desc = request.POST.get('description')
        post.name = name
        post.description = desc
        post.date = datetime.today() 
        
        post.save()

        return redirect('post') 
    return render(request , 'home/posts/edit.html' ,{'postid': id , 'post': post})

def home(request):
    home = Home.objects.filter(slug="home").first()
    aboutus = Home.objects.filter(slug="about").first()
    recenteducation = Home.objects.filter(slug="recenteducation")
    
    if request.method == 'POST':
        slug = request.POST.get('slug')
        title = request.POST.get('title')
        desc = request.POST.get('description')


        course_title = request.POST.getlist('course_title[]')
        titles = request.POST.getlist('title[]')
        descs = request.POST.getlist('description[]')
        project_url = request.POST.getlist('project_url[]')
        certification_titles = request.POST.getlist('certification_title[]')

        print(titles)  # Debugging line to check if titles are being captured

        if slug == "home":
            if home:
                home.title = title
                home.description = desc
                home.save()
            else:
                home = Home(title=title, description=desc, slug="home", date=datetime.today())
                home.save()

        if slug == "about":
            if aboutus:
                aboutus.title = title
                aboutus.description = desc
                aboutus.save()
            else:
                aboutus = Home(title=title, description=desc, slug="about", date=datetime.today())
                aboutus.save()
        elif slug == "skills":
            Home.objects.filter(slug="skills").delete()
            for title in titles:
                Home.objects.create(title=title ,slug="skills", date=datetime.today())

        elif slug == "recenteducation":
            Home.objects.filter(slug="recenteducation").delete()
            for title, course, desc in zip(titles, course_title, descs):
                 Home.objects.create(
                title=title,
                title2=course,
                description=desc,
                slug="recenteducation",
                date=datetime.today()
                 )
        elif slug == "experience":
            Home.objects.filter(slug="experience").delete()
            for title, course, desc in zip(titles, course_title, descs):
                 Home.objects.create(
                title=title,
                title2=course,
                description=desc,
                slug="experience",
                date=datetime.today()
                 )
        elif slug == "project":
            Home.objects.filter(slug="project").delete()
            for title, url, desc in zip(titles, project_url, descs):
                 Home.objects.create(
                title=title,
                url=url,
                description=desc,
                slug="project",
                date=datetime.today()
                 )
     
        elif slug == "certifications":
            print(certification_titles)  # Debugging line to check if certification titles are being captured correctly
            Home.objects.filter(slug="certifications").delete()
            for title in certification_titles:
                Home.objects.create(title=title ,slug="certifications", date=datetime.today())

        return redirect('home')
    
    skills = Home.objects.filter(slug="skills")
    experience = Home.objects.filter(slug="experience")
    project = Home.objects.filter(slug="project")
    certifications = Home.objects.filter(slug="certifications")
    return render(request, 'home/banner/index.html', {
        'home': home,
        'aboutus': aboutus,
        'skills': skills,
        'recenteducations': recenteducation,
        'experience': experience,
        'project': project,
        'certifications': certifications
    })