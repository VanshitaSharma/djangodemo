
from django.urls import path,include
from . import views

urlpatterns =[

    path('',views.blogs_list,name='blogs'),
    path('<int:id>',views.blog_details_view,name='blog_details'),
]
