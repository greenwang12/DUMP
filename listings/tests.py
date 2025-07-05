from django.test import TestCase
from .models import Listing
from accounts.models import CustomUser

class ListingModelTest(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(username="lister", password="pass", college_id="CLG100")

    def test_listing_creation(self):
        listing = Listing.objects.create(
            owner=self.user,
            title="Test Book",
            description="Test description",
            category="books",
        )
        self.assertEqual(str(listing), "Test Book")
