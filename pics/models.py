from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField


class Images(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    # location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def save_image(self):
        self.save()


    # update image
    def update_image(self, name, description):
        self.name = name
        self.description = description
        # self.location = location
        # self.category = category
        self.save()

    # get all images
    @classmethod
    def get_all_images(cls):
        images = Images.objects.all()
        return images
