from django.test import TestCase
from .models import Location, Category, Image

# Create your tests here.


class LocationTestClass(TestCase):
    # set up method
    def setUp(self):
        self.location = Location(location='Nairobi,Kenya')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location) > 0)


class CategoryTestClass(TestCase):
    # set up method
    def setUp(self):
        self.category = Category(name='Cool')

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)


class ImageTestClass(TestCase):

    # set up method
    def setUp(self):
        # Location
        self.location = Location(location="Nairobi")
        self.location.save()

        # Category
        self.category = Category(category="Home Desktop")
        self.category.save()

        self.image = Image(image='', image_name='photo', image_description='Breif description', location=self.location)
        self.image.save()

        self.new_image.category.add(self.category)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Image.objects.all().delete()
