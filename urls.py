from django.urls import path

from techblog.views import *

urlpatterns=[
    path('index/',index,name='index'),
    path('addpost/',create_post,name='create_post'),
    path('readmore/<int:id>', read_more,name='read_more'),
    path('update/<int:id>', updatepost,name='update'),
    path('delete/<int:id>', delete_post,name='delete'),
    # path('showpost/',show_post,name='show_post'),

]