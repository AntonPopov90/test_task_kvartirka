from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ArticleListSerializer, CommentsCreateSerializer, ArticleDetailSerializer
from .models import Article


class ArticleView(APIView):
    """Вывод списка cтатей"""
    def get(self, request):
        comments = Article.objects.all()
        serializer = ArticleListSerializer(comments, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        article = Article.objects.get(id=pk)
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)


class CommentCreateView(APIView):
    """Добавление комментария к статье"""
    def post(self, request):
        comment = CommentsCreateSerializer(data=request.data)
        if comment.is_valid():
            comment.save()
        return Response(status=201)