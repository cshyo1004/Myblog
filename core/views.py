from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Post
from .forms import Postform

# Create your views here.
def index(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES)
        form.save()
    else:
        form = Postform()

    context = {
        'posts' : posts,
        'form' : form,
    }
    return render(request, 'core/index.html', context)

def post_detail(request, post_id=None):
    post = Post.objects.get(id=post_id)
    return render(request, 'core/post.html', {'post': post})

def delete_post(request, post_id=None):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def update_post(request, post_id=None):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = Postform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post.id)
    else:
        form = Postform(instance=post)
        return render(request, 'core/update_post.html', {'form': form})