treecomments
============

Adds threaded commenting feature on top of Django's commenting framework. Uses
django-mptt to archive this.


Installation
============

Requires that Django's commenting hasn't been enabled for the Django project
before (i.e. database shouldn't have ``django_comments``).

Add following to ``INSTALLED_APPS``

```
'django.contrib.comments',
'treecomments',
```

And then run ``syncdb`` command.
