from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Author

# Create your views here.
from .forms import *


def start_page(request):
    posts = Post.objects.all().order_by('-likes')
    return render(request, 'appBlog/start_page.html', {'posts': posts})


def create_new_post(request):
     # Instantiate the author form separately

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        author_form = AddNewAuthor(request.POST)
        if author_form.is_valid():
            form_data = author_form.cleaned_data
            name = form_data.get('name')
            surname = form_data.get('surname')
            if Author.objects.filter(name=name, surname=surname).exists():
                return render(request, 'appBlog/create_new_post.html',
                              {'author_form': author_form, 'error': 'Author with the same name and surname already exists.'})
            author_form.save()
            return redirect('create_new_post')


        if form.is_valid():
            form.save()
            return redirect('start_page')

    form = AddPostForm()
    author_form = AddNewAuthor()
    return render(request, 'appBlog/create_new_post.html', {'author_form': author_form, 'form': form})





def view_post(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'appBlog/view_post.html', {'post': post})


def increase_likes_number(request, id):
    post = get_object_or_404(Post, id=id)
    post.likes += 1
    post.save()
    return redirect('start_page')


#
# def add_author(request):
#     if request.method == 'POST':
#         form = AddNewAuthor()
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             surname = form.cleaned_data['surname']
#             if Author.objects.filter(name=name, surname=surname).exists():
#                 return render(request, 'appBlog/create_new_author.html',
#                               {'form': form, 'error': 'Author with the same name and surname already exists.'})
#
#             form.save()
#             return redirect('create_new_post')
#     form = AddNewAuthor()
#
#     return render(request, 'appBlog/create_new_post.html', {'author_form': form})
