from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from parler.models import TranslatableModel, TranslatedFields, TranslatedFieldsModel
from parler.fields import TranslatedField

# from https://phrase.com/blog/posts/website-i18n-with-django-rest-framework-and-django-parler/

class Post(TranslatableModel):
    translations = TranslatedFields(
        title = models.CharField(_('Title'), max_length=200, unique=True),
        content = models.TextField(_('Content'), null=True, blank=True)
    )
    # title = TranslatedField(any_language=True)
    # content = TranslatedField(any_language=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

    def __str__(self):
        return self.title
    

# class PostTranslation(TranslatedFieldsModel):
#     master = models.ForeignKey(Post, related_name='translations', null=True)
#     title = models.CharField(_('Title'), max_length=200)
#     content = models.TextField(_('Content'), blank=True)

#     class Meta:
#         verbose_name = _('Post translation')
#         verbose_name_plural = _('Posts translation')

