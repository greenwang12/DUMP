from django.test import TestCase
from .models import Badge, UserBadge
from accounts.models import CustomUser

class BadgeTest(TestCase):
    def test_badge_create(self):
        badge = Badge.objects.create(name="Green Donor", description="For 5 donations", points_required=50)
        self.assertEqual(str(badge), "Green Donor")

class UserBadgeTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="badgeuser", password="pass", college_id="CLG103")
        self.badge = Badge.objects.create(name="Contributor", description="Donated 3 items", points_required=30)

    def test_user_badge_link(self):
        ub = UserBadge.objects.create(user=self.user, badge=self.badge)
        self.assertEqual(ub.user.username, "badgeuser")
