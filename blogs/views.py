from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import random
from datetime import timedelta
from django.utils import timezone

def BlogDetailView(request, slug):
	obj = get_object_or_404(Blog, slug__iexact=slug)
	# last_obj, first_obj = False, False
	# pre_obj = None
	# next_obj = None
	# i = obj.id
	# last_i = Blog.objects.all().last().id
	# while i is not 0:
	# 	try:
	# 		pre_obj = Blog.objects.get(id=i - 1, public=True)
	# 		if pre_obj is not None:
	# 			first_obj = True
	# 			break
	# 	except ObjectDoesNotExist:
	# 		i = i - 1
	# i = obj.id
	# while i is not last_i:
	# 	try:
	# 		next_obj = Blog.objects.get(id=i + 1, public=True)
	# 		if next_obj is not None:
	# 			last_obj = True
	# 			break
	# 	except ObjectDoesNotExist:
	# 		i = i + 1
	# if obj.language == "English":
	# 	tag_str = obj.english_tags
	# 	tags = tag_str.split(',')
	# 	all_objs = Blog.objects.filter(public=True, language="English")
	# else:
	# 	tag_str = obj.hindi_tags
	# 	tags = tag_str.split(',')
	# 	all_objs = Blog.objects.filter(public=True, language="Hindi")
	# no = random.sample(range(all_objs.count()), 3)
	# sugested = []
	# for i in no:
	# 	sugested.append(all_objs[i])
	# 	title = obj.title
	# 	if obj.meta_description == "":
	# 		description = obj.description
	# 	else:
	# 		description = obj.meta_description
	# 	if i.language == "Engish":
	# 		keywords = obj.english_tags
	# 	else:
	# 		keywords = obj.hindi_tags
	if obj.is_available_in_hindi:
		same_contents_in_diff_language = Blog.objects.filter(post_hash__iexact=obj.post_hash)
	else:
		same_contents_in_diff_language = None
	return render(request, "blogs/blog_detail.html", {'blog': obj, 'same_contents_in_diff_language': same_contents_in_diff_language})
	# return render(request, "blogs/blog_detail.html", {'blog': obj, 'tags': tags, 'sugested': sugested, 'title': title, 'description': description, 'keywords': keywords, 'same_contents_in_diff_language': same_contents_in_diff_language})
