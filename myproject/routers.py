from __future__ import unicode_literals

from article.viewsets import ArticleViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register('article', ArticleViewSet)
