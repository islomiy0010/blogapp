from django.urls import path
from . views import index,post_detail,post_edit,post_delete

urlpatterns=[
    path('blog/',index,name='index-page'),
    path('post_detail/<int:pk>',post_detail,name='post-detail-page'),
    path('post_edit/<int:pk>',post_edit,name='post-edit-page'),
    path('post_delete/<int:pk>',post_delete,name='post-delete-page'),
]