from django.test import TestCase
from pics.models import Location, Category, Images

# Create your tests here.
class ImagesTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        Images.objects.create(
            name="Test Image",
            description="Test Description",
            location=Location.objects.create(name="Test Location"),
            category=Category.objects.create(name="Test Category"),
            image="http://test.com/test.jpg",
            created_at=None
        )

    def test_image_name(self):
        """
        Test that the image name is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(Images.name, "Test Image")

    def test_image_description(self):
        """
        Test that the image description is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(Images.description, "Test Description")

    def test_image_location(self):
        """
        Test that the image location is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(Images.location.name, "Test Location")

    def test_image_category(self):
        """
        Test that the image category is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(Images.category.name, "Test Category")

    def test_image_image(self):
        """
        Test that the image image is correct
        """
        image = Images.objects.get(name="Test Image")
        self.assertEqual(Images.image, "http://test.com/test.jpg")


    def test_image_str(self):
        """
        Test that the image string representation is correct
        """
        image = Images.objects.get(name="Test Image")
        self