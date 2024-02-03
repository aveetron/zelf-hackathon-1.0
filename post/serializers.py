from rest_framework import serializers
from .models import Author, MediaUrl, SocialMediaPost, Like, Comment, View


class ZelfBaseSerializer(serializers.Serializer):
    unique_id = serializers.CharField(allow_blank=True, allow_null=True)
    unique_uuid = serializers.CharField(allow_blank=True, allow_null=True)
    origin_unique_id = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        abstract = True


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class MediaUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaUrl
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = View
        fields = "__all__"


class SocialMediaPostSerializer(serializers.ModelSerializer):
    like = LikeSerializer(read_only=True, allow_null=True)
    comment = CommentSerializer(read_only=True, allow_null=True)
    view = ViewSerializer(read_only=True, allow_null=True)

    class Meta:
        model = SocialMediaPost
        fields = "__all__"

    def get_like(self, social_media_post):
        likes = [{"id": like.id, "count": like.count}
                 for like in Like.objects.filter(social_media_post=social_media_post)]
        return likes

    def get_comment(self, social_media_post):
        comments = [{"id": comment.id, "count": comment.count}
                 for comment in Comment.objects.filter(social_media_post=social_media_post)]
        return comments

    def get_view(self, social_media_post):
        views = [{"id": view.id, "count": view.count}
                 for view in View.objects.filter(social_media_post=social_media_post)]
        return views

