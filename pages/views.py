from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
from django.http import HttpResponse
from django.utils import timezone
from django.core.validators import validate_email
from django.db.models import Q

from blogs.models import Blog, Category
from pages.models import NewsLetter
from pages.forms import QueryForm

from datetime import timedelta

import os
import random



def IndexView(request):
	last_week = timezone.now().date() - timedelta(days=7)
	featured_blog = Blog.objects.filter(featured=True).order_by('-id').first()
	popular_blogs = Blog.objects.filter(public=True, created__gte=last_week).order_by('-total_views')[0:4]
	recent_blogs = Blog.objects.filter(public=True).order_by('-id')[0:4]
	trending = Blog.objects.filter(public=True, trending=True).order_by('-id')[0:4]
	controversies = Blog.objects.filter(public=True, category__slug__in=["controversies"]).order_by('-id')[0:4]
	cinema = Blog.objects.filter(public=True, category__slug__in=["movies", "web series", "songs", "dance", "cinema"]).order_by('-id')[0:4]
	return render(request, 'index.html', {'populars': popular_blogs, 'recents': recent_blogs, "trendings": trending, "controversies": controversies, "featured": featured_blog, "cinemas": cinema})


def ContactView(request):
	form = QueryForm()

	if request.method == 'POST':
		form = QueryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('SubmitThankView')
		else:
			print("Form Invalid")
	return render(request, 'contact.html', {'form': form})


def AboutView(request):
	return render(request, 'about.html', {})


def PrivacyView(request):
	return render(request, 'privacy.html', {})


def BlogView(request):
	obj = Blog.objects.filter(public=True).filter(category__name__in=["Cinema", "Fashion", "Lifestyle"]).order_by('-id')
	return render(request, 'blog.html', {'blogs': obj})


def SubmitThankView(request):
	return render(request, 'submit_thankyou.html', {})


def sw_js(request):
    full_script_path = os.path.join(settings.STATIC_ROOT, "js/sw.js")
    print(full_script_path)
    with open(full_script_path, 'r') as f:
        javascript_contents = f.read()
    return HttpResponse(javascript_contents, content_type="text/javascript")


def AdsTxtView(request):
    full_script_path = os.path.join(settings.STATIC_ROOT, "js/ads.txt")
    with open(full_script_path, 'r') as f:
        javascript_contents = f.read()
    return HttpResponse(javascript_contents, content_type="text")


def RobotsView(request):
    full_script_path = os.path.join(settings.STATIC_ROOT, "js/robots.txt")
    with open(full_script_path, 'r') as f:
        javascript_contents = f.read()
    return HttpResponse(javascript_contents, content_type="text")


def NewsLetterView(request):
	email = request.POST.get('email')
	try:
		validate_email(email)
		NewsLetter.objects.create(email=email)
		return render(request, 'newsletter.html', {"success": True})
	except:
		return render(request, 'newsletter.html', {"success": False})


def SearchView(request):
	search = request.POST.get("search")
	blogs = Blog.objects.filter(Q(title__icontains=search)|Q(short_title__icontains=search))
	return render(request, 'search_result.html', {"blogs": blogs, "search": search})


def CategoryView(request, slug):
	category_obj = Category.objects.get(slug=slug)
	category_blogs = Blog.objects.filter(category__slug=slug)
	return render(request, 'category.html', {"blogs":category_blogs, "category": category_obj})
