from django.urls import path

from . import views
from .registration import views as authViews

urlpatterns = [
    path('', authViews.acc_login),
    path('register', authViews.acc_register),
    path('password_reset', authViews.reset_pwd),
    path('password_reset/<str:rand>', authViews.reset_pass_form),
    path('main/<str:name>', views.welcome),
    path('main/<str:name>/tests/<int:id>', views.demo),
    path('main/<str:name>/tests/<int:id>/evaluate', views.run_evaluation)
]