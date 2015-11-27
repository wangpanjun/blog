# encoding=utf-8

__author__ = 'xiaowang'
__date__ = '27/11/15'

import json
from django.views.generic import View
from django.http.response import HttpResponse, HttpResponseNotFound
from article.models import DoArticle


class ArticleView(View):
    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass

    def get(self, request, art_id):
        print(art_id)
        info, flag = DoArticle.get_by_art_id(art_id)
        if flag:
            return HttpResponseNotFound()
        return HttpResponse(json.dumps(info, ensure_ascii=False, indent=4), content_type='application/json')
