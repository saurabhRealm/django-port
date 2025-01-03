from django.shortcuts import render , HttpResponse , redirect , get_object_or_404
from datetime import datetime
from home.models import Post

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