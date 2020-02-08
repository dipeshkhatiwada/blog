from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from blog.models import Blog
from django.contrib.auth.models import User
from django.contrib import messages
from blog.forms import BlogForm


def about(request):
    return render(request, 'about.html')


def detail(request, id):
    # data = Blog.objects.get(pk=id)
    data = get_object_or_404(Blog, pk=id)
    context = {
        'blog': data
    }
    return render(request, 'detail.html', context)


def home(request):
    data = Blog.objects.all()
    context = {
        'blogs': data
    }
    return render(request, 'home.html', context)


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        u = request.POST.get('username')
        # u = request.POST['username']
        e = request.POST.get('email')
        p1 = request.POST.get('password1')
        p2 = request.POST.get('password2')
        if p1 == p2:
            try:
                u = User(username=u, email=e)
                u.set_password(p1)
                u.save()
            except:
                messages.add_message(request, messages.ERROR, "Username already exists")
                return redirect("signup")
            messages.add_message(request, messages.SUCCESS, "Sign up successfully login to continue")
            return redirect("signin")
        else:
            messages.add_message(request, messages.ERROR, "Password doesn't match")
            return redirect("signup")


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        u = request.POST.get('username')
        # u = request.POST['username']
        p = request.POST.get('password')
        user = authenticate(username=u, password=p)
        if user is not None:
            login(request, user)
            # messages.add_message(request, messages.SUCCESS, "Login success")
            return redirect("dashboard")
        else:
            messages.add_message(request, messages.ERROR, "Username and Password doesn't match")
            return redirect("signin")

        # else:
        #     return HttpResponse("Password Error")


def signout(request):
    logout(request)
    return redirect('signin')


@login_required(login_url='signin')
def dashboard(request):
    data = Blog.objects.all()[::-1]
    context = {
        'blogs': data
    }
    return render(request, 'dashboard.html', context)


def create_post(request):
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Post added successfully")
        return redirect('dashboard')
    context = {
        'forms': form
    }
    return render(request, 'create_post.html', context)


def edit_post(request, id):
    data = Blog.objects.get(pk=id)
    form = BlogForm(request.POST or None, request.FILES or None, instance=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, "Post updated successfully")
        return redirect('dashboard')
    context = {
        'forms': form

    }
    return render(request, 'edit_post.html', context)


def delete_post(request, id):
    blog = Blog.objects.get(pk=id)
    blog.delete()
    messages.add_message(request, messages.SUCCESS, "Post successfully deleted")
    return redirect('dashboard')
