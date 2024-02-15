from blog import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import profile, update_profile


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
    path('profile/<str:username>/', profile, name='profile'),
    path('profile/<str:username>/edit/', update_profile, name='update_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
