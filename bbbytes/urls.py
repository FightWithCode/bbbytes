"""
path configuration for bbbytes project.

The `pathpatterns` list routes paths to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/paths/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a path to pathpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a path to pathpatterns:  path('', Home.as_view(), name='home')
Including another pathconf
    1. Import the include() function: from django.paths import include, path
    2. Add a path to pathpatterns:  path('blog/', include('blog.paths'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

from blogs.sitemaps import BlogSitemap

from pages import views as PagesView

from django.contrib.sitemaps.views import sitemap
from blogs.sitemaps import BlogSitemap
from pages.sitemaps import PageSitemap



sitemaps = {
    'blogs': BlogSitemap,
    'pages': PageSitemap
}

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('newsletter/', PagesView.NewsLetterView, name="NewsLetterView"),
    path('search-results/', PagesView.SearchView, name="SearchView"),
    path('blog/', include('blogs.urls')),
    path('MasterAdminOfEWT/', admin.site.urls),
    path('sw.js/', PagesView.sw_js),
    path('ads.txt/', PagesView.AdsTxtView),
    path('robots.txt/', PagesView.RobotsView),
    path('', PagesView.IndexView, name="IndexView"),
    path('about/', PagesView.AboutView, name="AboutView"),
    path('privacy-policy/', PagesView.PrivacyView, name="PrivacyView"),
    path('blog/', PagesView.BlogView, name="BlogView"),
    path('contact/', PagesView.ContactView, name="ContactView"),
    path('thankyou/', PagesView.SubmitThankView, name="SubmitThankView"),
    path('category/<str:slug>/', PagesView.CategoryView, name='CategoryView'),
    # re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)