from django.db import models


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=120)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    class Meta:
        ordering = ['location']

    '''
    Class methods for Location Model
    '''
    @classmethod
    def location_item(cls):
        location = Location.objects.all()
        return location

    @classmethod
    def update_location(cls, id, location):
        image = Location.objects.filter(id=id).update(location=location)
        return image

    def __str__(self):
        return self.location


class Category(models.Model):
    name = models.CharField(max_length=50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    class Meta:
        ordering = ['name']

    '''
    Class methods for Category Model
    '''
    @classmethod
    def category_item(cls):
        category = Category.objects.all()
        return category

    @classmethod
    def update_category(cls, id, category):
        image = Category.objects.filter(id=id).update(category=category)
        return image

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='album/', null=True, blank=True)
    image_name = models.CharField(max_length=50)
    image_description = models.TextField(max_length='255')
    pub_date = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ['category']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    '''
    Class methods for Image Model
    '''
    @classmethod
    def image_item(cls):
        image = Image.objects.all()
        return image

    @classmethod
    def get_image_by_id(cls, id):
        pass

    @classmethod
    def update_image(cls, id, image):
        image = Image.objects.filter(id=id).update(image=image)
        return image

    @classmethod
    def search_by_category(cls, search_term):
        category = Image.objects.filter(category__name__icontains=search_term)
        return category

    @classmethod
    def filter_by_location(cls, location):
        pass
