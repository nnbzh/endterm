from rest_framework import routers
from app.posts import views

router = routers.DefaultRouter()
router.register(r'', views.PostsViewSet, basename='post')

urlpatterns = router.urls
