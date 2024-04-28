from parler_rest.serializers import TranslatableModelSerializer
from parler_rest.fields import TranslatedFieldsField
from rest_framework import routers, serializers, viewsets
from blog.models import Post


class PostSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Post)

    class Meta:
        model = Post
        fields = [
            'translations',
            'author',
            'created_at',
            'updated_at'
        ]
