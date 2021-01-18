from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):
    title = models.CharField(_("Title"), max_length=50)
    slug = models.SlugField(_("Slug"), unique=True, db_index=True)
    parent = models.ForeignKey('self', verbose_name=_("Parent"), on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='children', related_query_name='children')

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(_("Title"), max_length=128)
    slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    content = models.TextField(_("Content"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    publish_time = models.DateTimeField(_("Publish at"), db_index=True, null=True)
    draft = models.BooleanField(_("Draft"), default=True, db_index=True)
    image = models.ImageField(_("image"), upload_to='post/images', null=True)
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.SET_NULL, related_name='posts',
                                 null=True, blank=True)
    author = models.ForeignKey(User, verbose_name=_("Author"), related_name='Posts', related_query_name='children',
                               on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Post")
        verbose_name_plural = _("Posts")
        ordering = ['-publish_time']

    def __str__(self):
        return self.title


class PostSetting(models.Model):
    post = models.OneToOneField("Post", verbose_name=_("post"), related_name='post_setting',
                                related_query_name='post_setting', on_delete=models.CASCADE)
    comment = models.BooleanField(_("comment"))
    author = models.BooleanField(_("author"))
    allow_discussion = models.BooleanField(_("allow discussion"))

    class Meta:
        verbose_name = _("PostSetting")
        verbose_name_plural = _("PostSettings")


class CommentLike(models.Model):
    author = models.ForeignKey(User, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    comment = models.ForeignKey("blog.Comment", verbose_name=_("Comment"), related_name='comment_like',
                                related_query_name='comment_like', on_delete=models.CASCADE)
    condition = models.BooleanField(_("Condition"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        unique_together = [['author', 'comment']]
        verbose_name = _("CommentLike")
        verbose_name_plural = _("CommentLikes")

    def __str__(self):
        return str(self.condition)


class Comment(models.Model):
    content = models.TextField(_("Content"))
    post = models.ForeignKey(Post, verbose_name=_("Post"), on_delete=models.CASCADE, related_name='comments',
                             related_query_name='comments')
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    author = models.ForeignKey(User, verbose_name=_("Author"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']

    def __str__(self):
        return self.content

    @property
    def like_count(self):
        q = CommentLike.objects.filter(comment=self, condition=True)
        return q.count()

    @property
    def dislike_count(self):
        q = CommentLike.objects.filter(comment=self, condition=False)
        return q.count()
    # from django.db import models
    # from django.utils.translation import ugettext_lazy as _
    # from django.contrib.auth.models import User
    #
    #
    # class Post(models.Model):
    #     title = models.CharField(_("Title"), max_length=128)
    #     slug = models.SlugField(_("Slug"), db_index=True, unique=True)
    #     content = models.TextField(_("Content"))
    #     created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    #     updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    #     publish_time = models.DateTimeField(_("Publish at"), db_index=True)
    #     draft = models.BooleanField(_("Draft"), default=True, db_index=True)
    #     image = models.ImageField(_("image"), upload_to='post/image')
    #     author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    #
    #     class Meta:
    #         verbose_name = _("Post")
    #         verbose_name_plural = _("Posts")
    #         ordering = ['-publish_time']
    #     def __str__(self):
    #         return self.title
    #
    # class PostSetting(models.Model):
    #     post = models.OneToOneField(
    #         "Post", verbose_name=_("post"), on_delete=models.CASCADE)
    #     comment = models.BooleanField(_("comment"))
    #     author = models.BooleanField(_("author"))
    #     allow_discusstion = models.BooleanField(_("allow discusstion"))
    #
    #     class Meta:
    #         verbose_name = _("PostSetting")
    #         verbose_name_plural = _("PostSettings")
    # class Comment(models.Model):
    #     content = models.TextField(_("Content"))
    #     created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    #     updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    #     post = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    #     Author = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    #     is_confirmed = models.BooleanField(_("Confirm"), default=True)
    #
    #     class Meta:
    #         verbose_name = _("Comment")
    #         verbose_name_plural = _("Comments")
    #
    #     def __str__(self):
    #         return self.Author
    #
    #
    # class CommentLike(models.Model):
    #     user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    #     comment = models.ForeignKey(Comment, verbose_name="Comment", on_delete=models.CASCADE)
    #     created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    #     updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    #     like_type = models.BinaryField(_("Like Type"), null=True)
    #     condition = models.BooleanField(_("Condition"))
    #
    #     class Meta:
    #         verbose_name = _("Comment like")
    #         verbose_name_plural = _("Comment Likes")
    #
    #     def __str__(self):
    #         return self.like_type
