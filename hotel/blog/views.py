from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Blog, Comment
from .forms import BlogModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required
import datetime
# Create your views here.
def blogList(request):
    all_blog = Blog.objects.all()
    context = {
        'all_blog' : all_blog
    }
    return render(request, 'blog-list.html',context )


@login_required(login_url='login')
def addBlog(request):
    blogform = BlogModelForm()
    if request.method == 'POST':
        blogform = BlogModelForm(request.POST, request.FILES)
        if blogform.is_valid():
            blogform.save()
            return redirect('blog-submit')
    context = {
        'blogform' : blogform
    }
    return render(request, 'add-blog.html',context)



def blogDetail(request, slug):
    blog_detail = Blog.objects.get(slug = slug)
    context = {
        'blog_detail' : blog_detail

    }
    return render(request, 'blog-detail.html', context)

def addComment(request, slug):
    blogInst = Blog.objects.get(slug = slug)
    form = CommentModelForm(instance=blogInst)
    if  request.method == 'POST':
        form = CommentModelForm(request.POST, instance=blogInst)
        if form.is_valid():
            name = request.POST.get('name')
            body = form.cleaned_data['body']
            date_created = request.POST.get('date_created')
            c= Comment(post = blogInst, name=name, body=body, date_created=date_created)
            c.save()
        return redirect (reverse('blog-detail', args=[blogInst.slug]))
    else:
        form = CommentModelForm()
    context = {
        'form' : form,
        'blogInst' : blogInst
    }

    return render(request, 'add-comment.html', context)

def commentdelete(request, pk):
    delete_obj = Comment.objects.get(id=pk)
    if request.method == 'POST':
        delete_obj.delete()
        return redirect(reverse('blog-detail', args=[delete_obj.post.slug]))
    return render(request, 'comment-delete.html')