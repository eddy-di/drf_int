from typing import Any
from django.contrib import admin
from parler.admin import TranslatableAdmin
from blog.models import Post


class PostAdmin(TranslatableAdmin):
    list_display = [
        'title',
        'content'
    ]
    fieldsets = [
        (None, {
            'fields': ('title', 'content')
        })
    ]

    def save_model(self, request: Any, obj: Any, form: Any, change: Any) -> None:
        obj.author_id = request.user.id
        super().save_model(request, obj, form, change)
    

admin.site.register(Post, PostAdmin)
