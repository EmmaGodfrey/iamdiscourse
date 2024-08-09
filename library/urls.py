from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ebooks/', views.ebook_list, name='ebook_list'),
    path('ebooks/download/pdf/<int:pk>/',
         views.download_ebook_pdf, name='download_ebook_pdf'),
    path('ebooks/download/audio/<int:pk>/',
         views.download_ebook_audio, name='download_ebook_audio'),
    path('blog/', views.blog_list, name='blog_list'),
    path('resources/', views.resource_list, name='resources'),
    path('download/<int:file_id>/', views.download_file, name='download_file'),
    path('/admin/logout/', views.logout_view, name='logout'),
]

