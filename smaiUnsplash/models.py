from django.db import models


# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=120)

    def __str__(self):
        return self.location

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    class Meta:
        ordering = ['location']

    @classmethod
    def location_item(cls):
        location = cls.objects.all()
        return location


class Category(models.Model):
    name = models.CharField(max_length=50)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    class Meta:
        ordering = ['name']

    @classmethod
    def category_item(cls):
        category = cls.objects.all()
        return category

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
        image = cls.objects.all()
        return image

    @classmethod
    def get_image_by_id(cls, id):
        pass

    @classmethod
    def update_image(cls, id, image):
        image = cls.objects.filter(id).update(image=image)

    @classmethod
    def search_image(cls, search_term):
        category = cls.objects.filter(category__name__icontains=search_term)
        return category

    @classmethod
    def filter_by_location(cls, location):
        pass
