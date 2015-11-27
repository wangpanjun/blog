# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '27/11/15'


from django.conf.urls import url
from article.views import ArticleView

urlpatterns = [
    url(r'^article/(\d*)$', ArticleView.as_view()),
]