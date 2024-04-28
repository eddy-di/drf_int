from blog.models import Post
from blog.serializers import PostSerializer
from rest_framework import viewsets, routers

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
