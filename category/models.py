# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '27/11/15'

from django.contrib.gis.db import models
from django.utils import timezone


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    create_time = models.DateField(auto_now=True)

    class Meta:
        db_table = 'category'

    def detail(self):
        return {
            'category': self.category_id,
            'name': self.name
        }


class DoCategory(object):
    @classmethod
    def do_save(cls, param):
        Category.objects.create(**param)

    @classmethod
    def get_category(cls, category_id):
        try:
            category = Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return None, Category.DoesNotExist

        return category.detail()

    @classmethod
    def get_category_all(cls):
        return [category.detail() for category in Category.objects.all()]
