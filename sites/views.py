from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .forms import *

# class SearchNewsView(ListView):
#     model = News
#     template_name = 'main/news.html'
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         news_list = News.objects.filter(
#             Q(title__icontains=query) | Q(sub_title__icontains=query)
#         )
#         return news_list

# class SearchProjectView(ListView):
#     template_name = 'main/projects.html'
#     def get_queryset(self): # новый
#         query = self.request.GET.get('q')
#         projects_list = Projects.objects.filter(
#             Q(title__icontains=query) | Q(sub_title__icontains=query)
#         )
#         return (projects_list)


def index(request):
	form = CalculateForm()
	if request.method == 'POST':
		form2 = CalculateForm(request.POST)
		if form2.is_valid():
			form2.save()


	template_name = 'main/index.html'
	return render(request, template_name, context = {'form': form})

def product(request):
	template_name = 'main/product.html'
	return render(request, template_name)

def slider(request):
	template_name = 'main/slider.html'
	return render(request, template_name)

def five_blocks(request):
	template_name = 'main/five_blocks.html'
	return render(request, template_name)

def detail_five(request):
	template_name = 'main/detail_five.html'
	return render(request, template_name)

def second(request):
	template_name = 'main/second_page.html'
	return render(request, template_name)

def three(request):
	template_name = 'main/3.html'
	return render(request, template_name)

def four(request):
	template_name = 'main/four_page.html'
	return render(request, template_name)

def five(request):
	template_name = 'main/five_page.html'
	return render(request, template_name)

def six(request):
	template_name = 'main/six_page.html'
	return render(request, template_name)

def seven(request):
	template_name = 'main/seven_page.html'
	return render(request, template_name)

def projects(request):
	template_name = 'main/projects_all.html'
	projects = Projects.objects.all()
	context = {
		'projects': projects
	}
	return render(request, template_name, context)

def news(request):
	template_name = 'main/news_all.html'
	news = News.objects.all()
	context = {
		'news': news
	}
	return render(request, template_name, context)

def nine(request):
	template_name = 'main/nine_page.html'
	return render(request, template_name)

def ten(request):
	template_name = 'main/3.html'
	return render(request, template_name)

def eleven(request):
	template_name = 'main/six_page.html'
	return render(request, template_name)
