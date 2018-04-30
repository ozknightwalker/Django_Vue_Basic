from __future__ import unicode_literals

from .models import Article
from .serializers import ArticleSerializer

from rest_framework import viewsets


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
