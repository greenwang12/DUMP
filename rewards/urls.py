from django.urls import path
from .views import BadgeListView, UserBadgeListView

urlpatterns = [
    path('badges/', BadgeListView.as_view(), name='badge-list'),
    path('user-badges/', UserBadgeListView.as_view(), name='user-badge-list'),
]
