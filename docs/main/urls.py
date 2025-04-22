from django.urls import path
from . import views
app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('schools/', views.schools, name='schools'),
    path('school/<int:school_id>', views.school, name='school'),
    path('delete_school/<int:school_id>', views.delete_school, name='delete_school'),
    path('edit_school/<int:school_id>', views.edit_school, name='edit_school'),
    path('new_school/', views.new_school, name='new_school'),
    path('classes/<int:class_id>/', views.class_, name='class'),
    path('new_class/<int:school_id>', views.new_class, name='new_class'),
    path('edit_class/<int:class_id>/', views.edit_class, name='edit_class'),
    path('delete_class/<int:class_id>/',views.delete_class,name='delete_class'),
    path('new_activity/<int:class_id>/', views.new_activity, name='new_activity'),
    path('edit_activity/<int:activity_id>/', views.edit_activity, name='edit_activity'),
    path('delete_activity/<int:activity_id>/', views.delete_activity, name='delete_activity'),
    path('help/', views.help, name='help'),
]