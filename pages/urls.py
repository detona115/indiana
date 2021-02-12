from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (    
    ParentViewSetAPIView, 
    ParentIdViewSetAPIView,
    ChildViewSetAPIView,
    ChildIdViewSetAPIView
)

router = SimpleRouter()
router.register('parent', ParentViewSetAPIView, basename='parent_all')
router.register('parent/<int:pk>', ParentIdViewSetAPIView, basename='parent_id')
router.register('child', ChildViewSetAPIView, basename='child_all')
router.register('child/<int:pk>', ChildIdViewSetAPIView, basename='child_id')
# router.register('children', ChildViewSetAPIView, basename='children')
# router.register('parents', ChildViewSetAPIView, basename='parents')


urlpatterns = router.urls
