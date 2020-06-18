from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from .models import post
from .models import us
from .models import video

# Create your views here.

from django.http import HttpResponse


def home(request):
    return render(request, 'blog/home.html')

    # return render(request, 'blog/home.html')


def posts(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request, 'blog/posts.html', context)


class PostListView(ListView):
    model = post
    template_name = 'blog/posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6


class UserPostListView(ListView):
    model = post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['date_posted']
    paginate_by = 6

    def get_queryset(self):

        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})

def videos(request):
    vids =video.objects.all()
    return render(request, 'blog/videos.html', {'vids': vids})

def shop(request):
    return render(request, 'blog/shop.html')
   
