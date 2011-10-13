from django.contrib.comments.models import Comment
import mptt
from mptt.fields import TreeForeignKey
from django.db import models

__all__ = ['Comment']

treefk = TreeForeignKey(Comment, blank=True, null=True, related_name='children')
treefk.contribute_to_class(Comment, 'parent')
title = models.CharField(blank=True, null=True, max_length=255)
title.contribute_to_class(Comment, 'title')
mptt.register(Comment)
