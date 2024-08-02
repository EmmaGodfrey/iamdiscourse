import os
from urllib import response
from django.http import FileResponse, Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Ebook, BlogPost, Resource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    breadcrumbs = [{'name': 'Home', 'url': '#'}]
    return render(request, 'library/home.html', {'breadcrumbs': breadcrumbs})


def ebook_list(request):
    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
        {'name': 'E-books', 'url': '/ebooks/'}
    ]
    ebooks = Ebook.objects.all()
    return render(request, 'library/ebook_list.html', {'breadcrumbs': breadcrumbs, 'ebooks': ebooks})


def blog_list(request):
    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Blog', 'url': '/blog/'}
    ]
    blog_posts = BlogPost.objects.all()
    return render(request, 'library/blog_list.html', {'breadcrumbs': breadcrumbs, 'blog_posts': blog_posts})


def download_ebook_pdf(request, pk):
    try:
        ebook = Ebook.objects.get(pk=pk)
        if ebook.pdf_file:
            response = FileResponse(ebook.pdf_file.open(
            ), as_attachment=True, filename=ebook.pdf_file.name)
            return response
        else:
            raise Http404("PDF file not found")
    except Ebook.DoesNotExist:
        raise Http404("Ebook does not exist")


def download_ebook_audio(request, pk):
    try:
        ebook = Ebook.objects.get(pk=pk)
        if ebook.audio_file:
            response = FileResponse(ebook.audio_file.open(
            ), as_attachment=True, filename=ebook.audio_file.name)
            return response
        else:
            raise Http404("Audio file not found")
    except Ebook.DoesNotExist:
        raise Http404("Ebook does not exist")


def resource_list(request):
    breadcrumbs = [
        {'name': 'Home', 'url': '/'},
        {'name': 'Resources', 'url': '/resources/'}
    ]
    resource_list = Resource.objects.order_by('id')
    context = {'breadcrumbs': breadcrumbs, 'resources': resource_list}
    return render(request, 'library/resources.html', context)


def download_file(request, file_id):
    resource = get_object_or_404(Resource, pk=file_id)

    if resource.resource_type != 'download':
        return HttpResponseNotFound('Invalid resource type')

    try:
        with resource.file.open(mode='rb') as fh:
            response = FileResponse(
                fh, content_type='application/force-download')
            response['Content-Disposition'] = f'attachment; filename={resource.file.name}'
            return response
    except FileNotFoundError:
        return HttpResponseNotFound('File not found')
