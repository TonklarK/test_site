from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('contact',views.contact,name='contact'),
    path('blog/<int:id>',views.blog_details,name="blog_details"),
    path('search_result',views.search,name="search"),
    path('all_blog',views.all_posts,name="all_blog")
]