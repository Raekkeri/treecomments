from django.contrib.comments.templatetags.comments import BaseCommentNode

from django import template


register = template.Library()


class TreeCommentListNode(BaseCommentNode):
    """Insert a list of comments into the context."""
    def get_context_value_from_queryset(self, context, qs):
        return qs.order_by('tree_id', 'lft')


@register.tag
def get_treecomment_list(parser, token):
    """Returns django-mptt compatible queryset."""
    return TreeCommentListNode.handle_token(parser, token)
