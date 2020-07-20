from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.http_response),
    path('render/', views.template_render),
    path('model-render/', views.model_template_render),
    path('<int:pk>/', views.post_detail),
]
