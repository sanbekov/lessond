from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post, Comment
from posts.forms import Postform, Commentform
from posts.constants import PAGINATION_LiMIT
from django.views.generic import ListView, CreateView, DetailView, UpdateView


def get_user_from_request(request):
    return request.user if not request.user.is_anonymous else None


class MainView(ListView):
    queryset = Post.objects.all()
    template_name = 'posts.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        return {
            'posts': self.queryset,
            'user': get_user_from_request(self.request)
        }

    def get(self, request, **kwargs):
        page = int(request.GET.get('page', 1))
        start_post = PAGINATION_LiMIT * page if page != 1 else 0
        end_post = start_post + PAGINATION_LiMIT
        max_page = len(self.queryset) / PAGINATION_LiMIT
        if max_page > round(max_page):
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)
        context = {
            'posts': self.queryset[start_post:end_post],
            "user": get_user_from_request(self.request),
            'pages': range(1, (self.queryset.__len__() // PAGINATION_LiMIT) + 1)
        }
        return render(request, self.template_name, context=context)


class PostDetailView(DetailView):
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'detail.html'


class CreatePostView(ListView, CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = Postform

    def get(self, request, **kwargs):
        if get_user_from_request(request):
            return render(request, self.template_name, context={
                'post_form': self.form_class,
            })
        return redirect('/')

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            Post.objects.create(
                title=form.cleaned_data.get("title"),
                desciption=form.cleaned_data.get("desciption"),
                stars=form.cleaned_data.get("stars"),
                type=form.cleaned_data.get("type")
            )
            return redirect('/')
        else:
            return render(request, self.template_name, context={
                'post_form': form
            })


class EditPostView(ListView, CreateView):
    template_name = 'edit.html'
    queryset = Post.objects.all()
    form_class = Postform

    def get(self, request, pk, *args):
        return render(request, self.template_name, context={
            'post_form': self.form_class,
            'pk': pk
        })

    def post(self, request, pk, **kwargs):
        form = self.form_class(request.POST)
        instance = get_object_or_404(Post, pk=pk)
        if form.is_valid():
            instance.title = form.cleaned_data.get('title')
            instance.description = form.cleaned_data.get('description')
            instance.stars = form.cleaned_data.get('stars')
            instance.type = form.cleaned_data.get('type')
            instance.save()
            return redirect('/')
        else:
            return render(request, self.template_name, context={
                'post_form': self.form_class,
                'pk': pk
            })


