from django.urls import path

from . import views


urlpatterns = [
    path('home', views.home),
    path('', views.default),
    path('class', views.MyView.as_view(), name='class'),
    path('extend/<int:num>/<str:bla>', views.serve_extend),
    path('base', views.serve_base),
    # path("", views.serve_home),
    # path("toyota", views.serve_toyota),
    # path("suzuki", views.serve_suzuki),
]
