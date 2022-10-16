from rest_framework import routers

from post.viewsets import PostViewSet, PostScoreViewSet

router = routers.SimpleRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('post-scores', PostScoreViewSet, basename='post-scores')

urlpatterns = router.urls
