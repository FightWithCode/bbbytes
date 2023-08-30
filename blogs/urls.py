from django.urls import path
from . import views

name = "blog"

urlpatterns = [
    # url(r'^blog/(?P<slug>[-\w]+)/$', views.BlogDetailView, name="BlogDetailView"),
    path('<str:slug>/', views.BlogDetailView, name='BlogDetailView'),
]

