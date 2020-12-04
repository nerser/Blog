from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreate, ObjectUpdate, ObjectDelete
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


class PostDelete(ObjectDelete, View):
	model = Post
	template = 'blog/post_delete_form.html'
	model_list_template = 'post_list'


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


class TagDelete(ObjectDelete, View):
	model = Tag
	template = 'blog/tag_delete_form.html'
	model_list_template = 'tags_list_url'


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})
