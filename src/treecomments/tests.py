import unittest

from django.contrib import comments
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.contenttypes.models import ContentType


Comment = comments.get_model()


def create_comment(obj, title=None, **kwargs):
    return Comment.objects.create(content_object=obj,
        title=title, site_id=settings.SITE_ID, **kwargs)


class TreeCommentTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')

    def tearDown(self):
        self.user.delete()
        self.user2.delete()
        Comment.objects.all().delete()

    def create_comment(self, obj=None, title=None, **kwargs):
        obj = obj or self.user
        return create_comment(obj, title, **kwargs)


class SanityCheck(unittest.TestCase):
    def test_mptt_fields(self):
        self.assert_(hasattr(Comment, 'tree'))


class TestModel(TreeCommentTestCase):
    def test_title(self):
        c1 = self.create_comment(title='uniq title 1')
        db_obj = Comment.objects.get(title='uniq title 1')
        self.assertEquals(db_obj.id, c1.id)


class TestCustomManager(TreeCommentTestCase):
    def test_get_comments(self):
        root = self.create_comment(comment='root')
        root_c1 = self.create_comment(comment='answer to root', parent=root)
        comments = Comment.objects.comments_for_object(self.user)
        self.assertEquals([c for c in comments], [root, root_c1])
        self.assert_(root_c1 in root.get_children())
        self.assert_(root in root_c1.get_ancestors())

    def test_sibling(self):
        c1 = self.create_comment(title='title1', comment='hi!')
        c2 = self.create_comment(title='title2', comment='o hello')
        other = self.create_comment(obj=self.user2)
        comments = Comment.objects.comments_for_object(self.user)
        self.assertEquals(list(comments), [c1, c2])
