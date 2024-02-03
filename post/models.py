from django.db import models


class ZelfBaseModel(models.Model):
    unique_id = models.CharField(max_length=100)
    unique_uuid = models.CharField(max_length=200, null=True, blank=True)
    origin_unique_id = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        abstract = True


class Author(ZelfBaseModel):
    name = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    followers = models.JSONField(null=True, blank=True)
    avatar_urls = models.TextField(null=True, blank=True)
    profile_text = models.TextField(null=True, blank=True)


class MediaUrl(models.Model):
    url = models.TextField()
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.url


class SocialMediaPost(ZelfBaseModel):
    created_at = models.DateTimeField(null=True, blank=True)
    timestamp = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)
    main_text = models.TextField(null=True, blank=True)
    token_count = models.IntegerField(null=True, blank=True)
    char_count = models.IntegerField(null=True, blank=True)
    tag_count = models.IntegerField(null=True, blank=True)
    origin_platform = models.CharField(max_length=100)
    origin_url = models.TextField(null=True, blank=True)
    media = models.ForeignKey(MediaUrl, on_delete=models.DO_NOTHING)


class SocialMediaOperations(models.Model):
    social_media_post = models.ForeignKey(SocialMediaPost, on_delete=models.DO_NOTHING)
    count = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True


class Like(SocialMediaOperations):
    pass


class View(SocialMediaOperations):
    pass


class Comment(SocialMediaOperations):
    pass