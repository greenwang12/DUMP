from rest_framework import generics
from .models import Badge, UserBadge
from .serializers import BadgeSerializer, UserBadgeSerializer

class BadgeListView(generics.ListAPIView):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer

class UserBadgeListView(generics.ListAPIView):
    queryset = UserBadge.objects.all()
    serializer_class = UserBadgeSerializer
