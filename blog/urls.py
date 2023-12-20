from blog import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('addpost/', views.AddPost.as_view(), name='add_post'),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name="post_like"),
    path('<slug:slug>/update', views.UpdatePost.as_view(), name="update_post"),
    path(
        '<slug:slug>/delete/',
        views.DeletePost.as_view(), name='delete_post'
        ),
    path(
        'comments/<int:pk>/update/',
        views.UpdateComment.as_view(), name='update_comment'
        ),
    path(
        'comments/<int:pk>/delete/',
        views.DeleteComment.as_view(), name='delete_comment'
        ),
]
