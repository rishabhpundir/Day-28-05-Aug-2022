from django.urls import path, include
from apiapp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('singer', views.SingerViewset, basename='singer')
router.register('song', views.SongViewset, basename='song')

urlpatterns = [
    path('', include(router.urls)),
]
