from django.db import models
from django.forms import ValidationError


class Ebook(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    pdf_file = models.FileField(upload_to='ebooks/pdfs/')
    audio_file = models.FileField(
        upload_to='ebooks/audios/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        # Delete associated files if they exist
        if self.pdf_file:
            self.pdf_file.delete(save=False)
        if self.audio_file:
            self.audio_file.delete(save=False)
        super(Ebook, self).delete(*args, **kwargs)


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # Automatically set to current date and time
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Resource(models.Model):
    title = models.CharField(max_length=255)
    resource_type = models.CharField(
        max_length=10, choices=[('url', 'URL'), ('file', 'File')], default='url')
    url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to='resources/', blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def clean(self):
        if self.resource_type == 'url' and not self.url:
            raise ValidationError('URL is required for resource type URL')
        if self.resource_type == 'file' and not self.file:
            raise ValidationError('File is required for resource type File')
