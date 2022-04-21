from rest_framework import serializers

from .models import Article, Comments


class FilterCommentSerializer(serializers.ListSerializer):
    """Фильтр комментариев, только для parent"""
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.ModelSerializer):
    """вывод рекурсивно children"""
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class ArticleListSerializer(serializers.ModelSerializer):
    """Список комментариев """
    class Meta:
        model = Article
        fields = ('name', 'description',)


class CommentsCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария"""
    class Meta:
        model = Comments
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    """Вывод комментария"""
    children = RecursiveSerializer(many=True)
    depth = 3
    class Meta:
        list_serializer_class = FilterCommentSerializer
        model = Comments
        fields = ('text', 'children',)
        depth = 1


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Список комментариев"""
    comments = CommentSerializer(many=True)

    class Meta:
        model = Article
        exclude = ('name',)
