import logging

from django import forms
from django.contrib.comments.forms import CommentForm
from django.conf import settings


COMMENT_EMAIL_REQUIRED = getattr(settings, "COMMENT_EMAIL_REQUIRED", False)


class TreeCommentForm(CommentForm):
    parent_pk = forms.IntegerField(widget=forms.HiddenInput, required=False)

    def __init__(self, *args, **kwargs):
        super(TreeCommentForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = COMMENT_EMAIL_REQUIRED

    def get_comment_create_data(self):
        data = super(TreeCommentForm, self).get_comment_create_data()
        parent_pk = self.cleaned_data['parent_pk']
        if parent_pk:
            try:
                data['parent'] = self.get_comment_model().objects.get(
                                                                  pk=parent_pk)
            except self.get_comment_model().DoesNotExist:
                logging.warn('Parent comment was not found with pk %s' %
                             parent_pk)
                pass
        return data
