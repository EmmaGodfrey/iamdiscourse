import os
from urllib import response
from django.http import FileResponse, Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import Ebook, BlogPost, Resource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    return render(request, 'library/home.html')


def ebook_list(request):
    ebooks = Ebook.objects.all()
    return render(request, 'library/ebook_list.html', {'ebooks': ebooks})


def blog_list(request):
    blog_posts = BlogPost.objects.all()
    return render(request, 'library/blog_list.html', {'blog_posts': blog_posts})


def ebook_detail(request, pk):
    ebook = get_object_or_404(Ebook, pk=pk)
    return render(request, 'library/ebook_detail.html', {'ebook': ebook})


def blog_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'library/blog_detail.html', {'post': post})


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
    resource_list = Resource.objects.order_by('id')
    # print(resource_list)
    paginator = Paginator(resource_list, 10)

    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    print(page_obj)
    print(paginator)
    context = {'resources': page_obj, 'paginator': paginator}
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
