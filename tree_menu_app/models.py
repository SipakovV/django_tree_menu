from django.db import models
from django.urls import reverse


class TreeMenu(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(max_length=255)
    named_url = models.CharField(max_length=255, verbose_name='Named URL', blank=True,
                                 help_text='Named url from your urls.py file')

    def __str__(self):
        return str(self.title)

    def get_full_path(self):
        if self.named_url:
            url = reverse(self.named_url)
        else:
            url = reverse(self.slug)
        return url


class TreeMenuItem(models.Model):
    menu = models.ForeignKey(TreeMenu, related_name='items', on_delete=models.CASCADE, blank=True, null=True, default=None)
    parent = models.ForeignKey('self', related_name='items', on_delete=models.CASCADE,
                               blank=True, null=True, default=None)
    url = models.CharField(max_length=255, blank=True, null=True, default=None)
    named_url = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=40)

    def __str__(self):
        if self.named_url:
            return reverse(self.named_url)
        elif self.parent:
            return str(self.parent) + '/' + str(self.title)
        else:
            return str(self.menu) + ':' + str(self.title)

    def get_url(self):
        if self.url:
            return self.url
        else:
            return '/'
