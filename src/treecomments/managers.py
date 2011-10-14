from django.db import models
from django.contrib.contenttypes.models import ContentType
from models import Comment


class TreeCommentManager(models.Manager):
    def comments_for_object(self, obj):
        """Return QuerySet containing all comments for the given object."""
        ctype = ContentType.objects.get_for_model(obj)
        qs = Comment.objects.filter(object_pk=obj.pk, content_type=ctype)
        qs = qs.order_by('tree_id', 'lft')
        return qs
