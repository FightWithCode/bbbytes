from django.db import models
from django.urls import reverse
import random, string
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField


def default_list():
	return []

GENDER = (
	("male", "Male"),
	("female", "Female")
)

LANGUAGES = (
	("English", "English"),
	("Hindi", "Hindi")
)


class Author(models.Model):
	name = models.CharField(max_length=255)
	bio = models.TextField()
	profile = models.ImageField(upload_to='author', default='author/default.png')

	facebook = models.CharField(max_length=255, default="#")
	twitter = models.CharField(max_length=255, default="#")
	insta = models.CharField(max_length=255, default="#")
	youtube = models.CharField(max_length=255, default="#")
	linkedin = models.CharField(max_length=255, default="#")

	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=255)
	slug = models.CharField(max_length=150, default="test")
	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name_plural = "Categories"

	def save(self, *args, **kwargs):
		if self.slug == "test":
			self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)


class Blog(models.Model):
	title = models.CharField(max_length=150)
	short_title = models.CharField(max_length=45, default=None, null=True, blank=True)
	slug = models.CharField(max_length=150, default="test")
	category = models.ForeignKey(Category, on_delete=models.SET_NULL, default=None, blank=True, null=True)
	sub_categories = models.ManyToManyField(Category, related_name='sub_category')
	featured = models.BooleanField(default=False)
	trending = models.BooleanField(default=False)
	person_featured = models.JSONField(default=default_list, null=True, blank=True)
	

	front_image = models.ImageField(upload_to='blogs')
	front_image_233 = models.ImageField(upload_to='blogs', default='blogs/default.png')
	front_image_500 = models.ImageField(upload_to='blogs', default='blogs/default.png')
	
	description = models.CharField(max_length=500)
	content = RichTextField()
	author = models.ForeignKey(Author, default=None, null=True, blank=True, on_delete=models.SET_NULL)
	
	tags = models.JSONField(default=default_list, null=True, blank=True)
	
	language = models.CharField(choices=LANGUAGES, max_length=10, default="English")
	is_available_in_hindi = models.BooleanField(default=False)

	public = models.BooleanField()
	
	meta_description = models.CharField(max_length=200)
	post_hash = models.CharField(max_length=10, default=0)
	total_views = models.IntegerField(default=0)
	created = models.DateField(auto_now=True)
	updated = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.slug == "test":
			self.slug = slugify(self.title)
		if not self.post_hash or self.post_hash == '0':
			self.post_hash = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
		# list_of_image_name = self.front_image.split('.')
		# self.front_image_233 = list_of_image_name[0] + "_233" + "." + list_of_image_name[1]
		# self.front_image_500 = list_of_image_name[0] + "_500" + "." + list_of_image_name[1]
		super(Blog, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('BlogDetailView', kwargs={'slug': self.slug})
