from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreate, ObjectUpdate
from .forms import TagForm, PostForm


# Create your views here.
def post_list(request):
	posts = Post.objects.all()
	return render(request, 'blog/index.html', context={'posts': posts})


class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_detail.html'


class PostCreate(ObjectCreate, View):
	form_model = PostForm
	template = 'blog/post_create_form.html'


class PostUpdate(ObjectUpdate, View):
	form_model = PostForm
	model = Post
	template = 'blog/post_update_form.html'


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'


class TagCreate(ObjectCreate, View):
	form_model = TagForm
	template = 'blog/tag_create.html'


class TagUpdate(ObjectUpdate, View):
	form_model = TagForm
	model = Tag
	template = 'blog/tag_update_form.html'


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})
