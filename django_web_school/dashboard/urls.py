from django.urls import path
from .recipe import views as rec_views
from dashboard.category import views as ctg_views
from dashboard.views import index

urlpatterns = [

    path('', index, name='home'),

    path('rec/list/', rec_views.rec_list, name='rec_list'),
    path('rec/detail/<int:pk>/', rec_views.rec_detail, name='rec_detail'),
    path('rec/add/', rec_views.add, name='rec_add'),
    path('rec/edit/<int:pk>/', rec_views.edit, name='rec_edit'),
    path('rec/del/<int:pk>/', rec_views.rec_delete, name='rec_del'),

    path('ctg/one/<int:pk>/', ctg_views.one, name='ctg_one'),
    path('ctg/list/', ctg_views.list, name='ctg_list'),
    path('ctg/del/<int:pk>/', ctg_views.delete, name='ctg_del'),
    path('ctg/add/', ctg_views.add, name='ctg_add'),
    path('ctg/edit/<int:pk>/', ctg_views.edit, name='ctg_edit'),

]
