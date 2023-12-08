from django.urls    import path
from .              import views


app_name = 'home'
urlpatterns = [
    path('',                                        views.HomeView.as_view(),           name='home'),
    path('post/<int:post_id>/<slug:post_slug>/',    views.PostDetailView.as_view(),     name='detail'),
    path('post/delete/<int:post_id>/',              views.PostDeleteView.as_view(),     name='delete'),
    path('post/update/<int:post_id>',               views.PostUpdateView.as_view(),     name='update'),
    path('post/create/',                            views.PostCreateView.as_view(),     name='create'),
    path('reply/<int:post_id>/<int:comment_id>/',   views.PostAddReplyView.as_view(),   name='add_reply'),
    path('like/<int:post_id>/',                     views.PostLikeView.as_view(),       name='post_like')
]