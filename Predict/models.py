from django.db import models


# Create your models here.

class ImageModel(models.Model):
    model_image= models.ImageField(upload_to = "Image_store/")

    
    def __file__(self):
        return self.model_image

