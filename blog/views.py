from django.shortcuts import render


# Create your views here.
def post_list(request):
	names = ['Illia', 'Olya', 'Kolya']
	return render(request, 'blog/index.html', context={'names': names})
