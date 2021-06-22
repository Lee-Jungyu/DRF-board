from django.db.models import fields
from rest_framework import serializers
from .models import Post

# Serializer 사용
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()
    author = serializers.CharField()
    created_date = serializers.DateTimeField(read_only=True)
    updated_date = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.author = validated_data.get('author', instance.author)
        instance.save()
        return instance

    # custom validation    
    def validate_title_length(self, data):
        if len(data['title']) > 50:
            raise serializers.ValidationError("Title length should be less than 50")

# ModelSerializer 사용
# 필드를 재정의할 필요가 사라지고 create와 update 함수를 기본으로 제공
# validate 함수 자동 제공
class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'