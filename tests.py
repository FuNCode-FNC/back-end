from django.test import TestCase
from .models import Customer

class UserTestCase(TestCase):
    def setUp(self):
        user = Customer.objects.create_user(email='3@gmail.com', username="penis", password="sadasdasd",
                                            firstName='vlad', secondName='trof')




