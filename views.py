from django.shortcuts import render, redirect

# Create your views here.
from techblog.forms import PostBlogFrm
from techblog.models import PostBlog


def index(request):
    posts = PostBlog.objects.all()
    return render(request, "techblog/index.html", {'posts': posts})

def create_post(request):
    form=PostBlogFrm()
    if request.method=="POST":
        form=PostBlogFrm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,"techblog/create_post.html",{"form":form})

def read_more(request,id):
    post=PostBlog.objects.get(id=id)
    return render(request,'techblog/readmore.html')

def updatepost(request,id):
    post=PostBlog.objects.get(id=id)
    return render(request, 'techblog/edit_post.html',{'post':post})

def delete_post(request,id):
    post=PostBlog.objects.get(id=id)
    post.delete()
    return redirect("/index")



