from django.contrib.comments.models import Comment
from django.db import models
import mptt
from mptt.fields import TreeForeignKey

from managers import TreeCommentManager


__all__ = ['Comment']

treefk = TreeForeignKey(Comment, blank=True, null=True, related_name='children')
treefk.contribute_to_class(Comment, 'parent')
title = models.CharField(blank=True, null=True, max_length=255)
title.contribute_to_class(Comment, 'title')
Comment.objects = TreeCommentManager()
Comment.objects.model = Comment
mptt.register(Comment)
