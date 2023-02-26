from django.urls import path
from .views import (
   PostList, PostDetail, PostCreate, PostSearch,  PostEdit, PostDelete, CategoryListView, subscribe
)
from .views import IndexView


urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('categories/<int:pk>', CategoryListView.as_view(), name='category_news'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('', IndexView.as_view())
]
