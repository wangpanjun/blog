# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '26/11/15'
from django.contrib.postgres.fields import ArrayField
from django.contrib.gis.db import models
from django.utils import timezone


class Article(models.Model):
    art_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, db_index=True, null=True)
    content = models.TextField()
    create_time = models.DateField(auto_created=True)
    update_time = models.DateField(auto_now=True)


    class Meta:
        db_table = 'article'

    def detail(self):
        return {
            'art_id': self.art_id,
            'title': self.title,
            'content': self.content
        }


class DoArticle(object):
    @classmethod
    def do_save(cls, article):
        Article.objects.create(**article)

    @classmethod
    def get_by_art_id(cls, art_id):
        try:
            article = Article.objects.get(art_id=art_id)
        except Article.DoesNotExist:
            return None, Article.DoesNotExist
        return article.detail(), None
