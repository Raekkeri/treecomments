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

Also set ``COMMENTS_APP = 'treecomments'``.

And then run ``syncdb`` command.


An example for rendering comments in a tree
===========================================

Add ``'mptt'`` to ``INSTALLED_APPS``

```
{% load mptt_tags treecomments_tags %}
{% get_treecomment_list for object as comment_list %}
<div class="root">
    {% recursetree comment_list %}
        <div>
            <p>{{ node.pk }}: {{ node.user_name }} {{ node.submit_date }}</p>
            <p>{{ node.comment }}</p>
            {% if not node.is_leaf_node %}
                <div class="children" style="margin-left: 30px;">
                    {{ children }}
                </div>
            {% endif %}
        </div>
    {% endrecursetree %}
</div>
```
