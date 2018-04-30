from __future__ import unicode_literals

from django.views.generic import TemplateView


class HomepageView(TemplateView):
    template_name = 'article/homepage.html'
