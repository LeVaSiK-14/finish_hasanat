from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from .forms import *



def view_404_error(request, exception):
    return render(request, 'errs/404.html')





def tag(request, tag_id):
	template_name = 'main/tag.html'
	products = Products.objects.filter(sub_tag__id=tag_id)
	subtag = SubTags.objects.get(id = tag_id)

	context = {
	'subtag': subtag,
	'products': products,
	}

	return render(request, template_name, context)

def index(request):
	all_projects = Projects.objects.order_by('-id')[:8]
	all_news = News.objects.order_by('-id')[:8]
	context = {
				"all_projects": all_projects,
				'all_news': all_news,
	}
	template_name = 'main/index.html'
	return render(request, template_name, context)

def new_news_detail(request, new_id):
	template_name = 'main/five_blocks.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	new = get_object_or_404(News, id=new_id)
	new_images = Images_news.objects.filter(new=new)
	context = {
				"new": new,
				'new_images': new_images,
				'all_projects': all_projects,
				'all_news': all_news,
	}
	return render(request, template_name, context)

def project_detail(request, id):
	template_name = 'main/new-detail.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	project = get_object_or_404(Projects, id=id)
	images = Images_Projects.objects.filter(project=project)
	context = {
				"project": project,
				'images': images,
				'all_projects': all_projects,
				'all_news': all_news,
	}
	return render(request, template_name, context)

def product_detail(request, id):
	template_name = 'main/product_detail.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	product = get_object_or_404(Products, id=id)
	images = Images_Products.objects.filter(product=product)
	context = {
				"product": product,
				'images': images,
				'all_projects': all_projects,
				'all_news': all_news,
	}
	return render(request, template_name, context)

def news(request):
	template_name = 'main/news_all.html'
	news = News.objects.all()
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'news': news,
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def about_company(request):
	template_name = 'main/about_company.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def shef_montaj(request):
	template_name = 'main/five_page.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def vakansii(request):
	template_name = 'main/vakansii.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def pusko_naladochnue(request):
	template_name = 'main/four_page.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def contacts(request):
	template_name = 'main/six_page.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def voprosy_otvety(request):
	template_name = 'main/seven_page.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def podbor_oborudovania(request):
	template_name = 'main/slider.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def create_documetation(request):
	template_name = 'main/slider_2.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def liscence(request):
	template_name = 'main/liscence.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def detail_five(request):
	template_name = 'main/detail_five.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)

def coming_soon(request):
	template_name = 'main/coming_soon.html'
	all_news = News.objects.order_by('?')[:20]
	all_projects = Projects.objects.order_by('?')[:20]
	context = {
		'all_projects': all_projects,
		'all_news': all_news,
	}
	return render(request, template_name, context)















# def projects(request):
# 	template_name = 'main/projects_all.html'
# 	projects = Projects.objects.all()
# 	context = {
# 		'projects': projects
# 	}
# 	return render(request, template_name, context)




# def sub_tags(request, id):
# 	template_name = 'main/sub_tags.html'
# 	sub_tags = SubTags.objects.filter(tag__id=id)
# 	tags = get_object_or_404(Tags, id=id)
# 	context = {
# 		'sub_tags': sub_tags,
# 		'tags': tags,
# 	}
# 	return render(request, template_name, context)





# def three(request):
# 	template_name = 'main/3.html'
# 	return render(request, template_name)






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


