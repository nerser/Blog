from django.shortcuts import render, redirect
from django.views.generic import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q

from .models import Post, Tag
from .utils import ObjectDetailMixin, ObjectCreate, ObjectUpdate, ObjectDelete
from .forms import TagForm, PostForm


# Create your views here.
def post_list(request):
	search_query = request.GET.get('search', '')

	if search_query:
		posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
	else:
		posts = Post.objects.all()

	paginator = Paginator(posts, 3)

	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = f'?page={page.previous_page_number()}'
	else:
		prev_url = ''

	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	context = {
		'page_object': page,
		'is_paginated': is_paginated,
		'prev_url': prev_url,
		'next_url': next_url
	}

	return render(request, 'blog/index.html', context=context)


class PostDetail(ObjectDetailMixin, View):
	model = Post
	template = 'blog/post_detail.html'


class PostCreate(LoginRequiredMixin, ObjectCreate, View):
	form_model = PostForm
	template = 'blog/post_create_form.html'
	raise_exception = True


class PostUpdate(LoginRequiredMixin, ObjectUpdate, View):
	form_model = PostForm
	model = Post
	template = 'blog/post_update_form.html'
	raise_exception = True


class PostDelete(LoginRequiredMixin, ObjectDelete, View):
	model = Post
	template = 'blog/post_delete_form.html'
	model_list_template = 'post_list'
	raise_exception = True


class TagDetail(ObjectDetailMixin, View):
	model = Tag
	template = 'blog/tag_detail.html'


class TagCreate(LoginRequiredMixin, ObjectCreate, View):
	form_model = TagForm
	template = 'blog/tag_create.html'
	raise_exception = True


class TagUpdate(LoginRequiredMixin, ObjectUpdate, View):
	form_model = TagForm
	model = Tag
	template = 'blog/tag_update_form.html'
	raise_exception = True


class TagDelete(LoginRequiredMixin, ObjectDelete, View):
	model = Tag
	template = 'blog/tag_delete_form.html'
	model_list_template = 'tags_list_url'
	raise_exception = True


def tags_list(request):
	tags = Tag.objects.all()
	return render(request, 'blog/tags_list.html', context={'tags': tags})
