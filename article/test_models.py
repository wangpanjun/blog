# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '27/11/15'

import unittest
from article.models import DoArticle
import django

django.setup()


class ArticleTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_save(self):
        param = {"title":"title"}
        DoArticle.do_save(param)


    def tearDown(self):
        pass