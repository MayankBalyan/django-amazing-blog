from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
from blog.models import Post,Category,BlogComment
from django.contrib import messages


def home(request):
    posts = Post.objects.all()[:11]
    data = {
        'posts': posts
    }
    return render(request, "index.html", data)


def post(request, url):
    post = Post.objects.get(url=url)
    comments=BlogComment.objects.filter(post=post)


    return render(request, 'post.html',{'post':post,'comments':comments})
def categories_page(request):
    cat=Category.objects.all()


    return render(request,'categories_page.html',{'cat':cat})

def category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)

    data = {
        'cat':cat,
        'posts': posts

    }
    return render(request, 'category_posts.html',data )

def allposts(request):
    posts = Post.objects.all()
    data = {
        'posts': posts
    }
    return render(request,'allposts.html',data)
def about(request):
    return render(request,'about.html')




def login_page(request):
    return render(request,"login-page.html")
def register_page(request):
    return render(request,"register-page.html")
def handleSignup(request):
    if request.method =="POST":
        fname = request.POST['fname']
        username = request.POST['username']
        lname=request.POST['lname']

        email= request.POST['email']
        Password= request.POST['Password']
        #checks

        myUser=User.objects.create_user(username,email,Password)
        myUser.first_name= fname
        myUser.last_name=lname
        myUser.save()
        messages.success(request,"Your Account has been created Succesfully!! Now Login")
        return redirect("/login-page/")



    else:
        return HttpResponse("404  - Not Found")
def handleLogin(request):
    if request.method=="POST":
        loginUsername= request.POST['loginUsername']
        loginPassword = request.POST['loginPassword']
        user= authenticate(username=loginUsername,password=loginPassword)
        if user is not None:
            login(request,user)
            return redirect('/')
    else:
        return HttpResponse('Invalid Username or Password')
        return HttpResponse("404 - Not Found")
def handleLogout(request):

    logout(request)
    messages.success(request,"Logged Out Successfully !!")
    return redirect("/")


def postComment(request):
    if request.method=="POST":

        comment =request.POST.get("comment")
        user =request.user
        postsno =request.POST.get("sno")
        post=Post.objects.get(post_id=postsno)
        comment=BlogComment (comment=comment,user=user,post=post)
        comment.save()
        messages.success(request,"Your Comment has been posted successfully")
    return redirect(f"/blog/{post.url}/")





