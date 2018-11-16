from django.conf.urls import url, include
from rest_framework import routers
from posts import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewset)

urlpatterns = [
    url('^', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace="rest_framework"))
]