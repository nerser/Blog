from django.shortcuts import render
from django.shortcuts import get_object_or_404

from typing import Callable


class ObjectDetailMixin:
	model: Callable = None
	template: str = None

	def get(self, request, slug):
		obj = get_object_or_404(self.model, slug__iexact=slug)
		return render(request, self.template, context={self.model.__name__.lower(): obj})
