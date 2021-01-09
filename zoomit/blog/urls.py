from django.urls import path,include
from django.views.decorators.http import require_POST
from django.views.generic import ArchiveIndexView

from blog.models import Post
from blog.views import main_page, comment_like, PostsView, SinglePost, create_comment, Categories, CategoryPosts, \
    AuthorsPosts, ArticleMonthArchiveView, ArticleWeekArchiveView, ShowMonthly, ShowWeekly, SearchField
from .api import comment_detail,comment_list,PostViewSet,CommentViewSet,CategoryViewSet,PostSettingViewSet

from zoomit.urls import router
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'post_settings', PostSettingViewSet)

urlpatterns = [

    path('posts/<slug:slug>/', SinglePost.as_view(), name='single_post'),
    path('categories/<slug:slug>/', CategoryPosts.as_view(), name="category_posts"),
    path('categories/', Categories.as_view(), name='show_categories'),
    path('', main_page, name="main_page"),
    path('like_comment/', comment_like, name='like_comment'),
    path('posts/', PostsView.as_view(), name='posts_archive'),
    path('comment/', create_comment, name='comment_create'),
    path('authors/<slug:slug>/', AuthorsPosts.as_view(), name="authors_posts"),
    path('latest/', ArchiveIndexView.as_view(model=Post, date_field='create_at', template_name='blog/posts.html',
                                             context_object_name='post_list'),
         name="latest_posts"),
    path('monthly/<int:year>/<int:month>/', ArticleMonthArchiveView.as_view(month_format='%m'),
         name="archive_month_numeric"),
    path('<int:year>/week/<int:week>/', ArticleWeekArchiveView.as_view(), name="archive_week"),
    path('show_month/', ShowMonthly.as_view(), name='show_month'),
    path('show_week/', ShowWeekly.as_view(), name='show_week'),
    path('search/', SearchField.as_view(), name='search'),
    # path('api/comments/', comment_list, name='comment_list'),
    # path('api/comments/<int:pk>/', comment_detail, name='comment_detail')
]
