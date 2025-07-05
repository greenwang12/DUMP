from django.test import TestCase
from .models import Message
from accounts.models import CustomUser

class MessageModelTest(TestCase):
    def setUp(self):
        self.sender = CustomUser.objects.create_user(username="sender", password="pass", college_id="CLG101")
        self.receiver = CustomUser.objects.create_user(username="receiver", password="pass", college_id="CLG102")

    def test_message_send(self):
        msg = Message.objects.create(sender=self.sender, receiver=self.receiver, message="Hello!")
        self.assertEqual(str(msg), "sender → receiver")
