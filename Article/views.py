from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
import random

def error_404_view(request, exception):
    return render(request, '404.html', {})
def random_num(min, max):
    rand_id = random.randint(min, max)
    return rand_id

class ArticleAPIView(APIView):
    def get(self, request):
        lst = Article.objects.filter(id=random_num(20, 16019)).values('discipline', 'subject', 'article')
        return Response({'article': list(lst)})