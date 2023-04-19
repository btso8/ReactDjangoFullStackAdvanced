from django.urls import path, include
from api import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'profile', views.UserProfileViewSet)
router.register(r'comments', views.CommentViewset)
router.register(r'bets', views.BetViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', views.CustomObtainAuthToken.as_view()),
]
