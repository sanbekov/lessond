from django.shortcuts import render, redirect
from django.http import HttpResponse
from posts.forms import Postform, Commentform
from posts.models import Post, Comment


def main(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        data = {
            'posts': posts
        }

        return render(request, 'posts.html', context=data)


def post_detail(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(post=post)

    data = {
        'post': post,
        'comments': comments
    }

    return render(request, 'detail.html', context=data)


def creat_post(request):
    if request.method == 'GET':
        return render(request, 'create_post.html', context={
            'post_form': Postform
        })

    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get('title'),
                desciption=form.cleaned_data.get('description'),
                stars=form.cleaned_data.get('stars'),
                type=form.cleaned_data.get('type')
            )
            return redirect('/')
        else:
            return render(request, 'create_post.html', context={
                'post_form': form
            })



def creat_comment(request):
    if request.method == 'GET':
        return render(request, 'create_comment.html', context={
            'comment_form': Commentform
        })

    if request.method == "COMMENT":
        form = Commentform(request.POST)
        if form.is_valid():
            Comment.objects.create(
                author=form.cleaned_data.get('author'),
                text=form.cleaned_data.get('text')
            )
            return redirect('/')
        else:
            return  render(request, 'create_comment.html', context={
                'comment_form': Commentform
            })



