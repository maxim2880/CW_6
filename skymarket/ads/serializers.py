from rest_framework import serializers


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою
from ads.models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class AdDetailSerializer(serializers.ModelSerializer):
    author_first_name = serializers.SerializerMethodField()
    author_last_name = ''
    author_id = ''

    def get_author_first_name(self, obj):
        return obj.author.first_name

    class Meta:
        model = Ad
        fields = '__all__'
