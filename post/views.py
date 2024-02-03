import os
import requests

from rest_framework.generics import GenericAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
from .models import SocialMediaPost, Author, MediaUrl
from rest_framework.pagination import LimitOffsetPagination
from .serializers import SocialMediaPostSerializer, AuthorSerializer
from .handler import SocialMediaPostHandler


class CollectContentsApiView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SocialMediaPostSerializer
    hack_api = os.environ.get("HACKAPI_URL")

    def get(self, request):
        contents = requests.get(f"{self.hack_api}/backend/api/v1/contents",
                                headers={"x-api-key": os.environ.get("x-api-key")})

        """
        social medis post handle will be called 
        if needed social media post handler will call 
        the auther handler as well. 
        """
        SocialMediaPostHandler.post_handler(contents)

        return Response({})


class SocialMediaPostsApiView(GenericAPIView):
    serializer_class = SocialMediaPostSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = LimitOffsetPagination

    def get(self, request):
        try:
            social_media_posts = SocialMediaPost.objects.all()
            social_media_post_serializer = self.get_paginated_response(
                self.serializer_class(self.paginate_queryset(social_media_posts),
                                      many=True).data)
            return Response(
                {
                    "data": social_media_post_serializer.data["results"],
                    "total": social_media_post_serializer.data["count"],
                    "prev_url": social_media_post_serializer.data["previous"],
                    "next_url": social_media_post_serializer.data["next"],
                    "page_size": 10,
                    "response_code": status.HTTP_200_OK,
                    "response_message": "success",
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response({
                "data": {},
                "response_message": e.args[0],
                "response_code": status.HTTP_400_BAD_REQUEST
            }, status=status.HTTP_400_BAD_REQUEST)
