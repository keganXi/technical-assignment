from django.test import TestCase


# Write tests below.


class TestCIWorflow(TestCase):

    def test_ci(self):
        return self.assertEquals(1 + 3, 4)