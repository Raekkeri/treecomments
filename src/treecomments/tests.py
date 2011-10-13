import unittest
from django.contrib import comments
Comment = comments.get_model()


class SanityCheck(unittest.TestCase):
    def test_mptt_fields(self):
        self.assert_(hasattr(Comment, 'tree'))
