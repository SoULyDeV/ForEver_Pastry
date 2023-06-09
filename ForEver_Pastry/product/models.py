from io import BytesIO
from PIL import Image


from django.core.files import File
from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    
    class Meta:
        ordering : ('name',)
        
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/{self.slug}/"
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering : ('-date_added',)
        
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/{self.category.slug}/{self.slug}/"
    
    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        else:
            return ''
        
    def get_thumbnail(self):
        if self.thumbnail:
            return 'http://127.0.0.1:8000' + self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()
                #return the img thumbnail
                return 'http://127.0.0.1:8000' + self.thumbnail.url
            else:
                return ''
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        #to make sure the image is ok
        img.thumbnail(size)
        #The thumbnail() method in Pillow allows you to create a smaller version (thumbnail) of an image while maintaining its aspect ratio. It takes in a size parameter
        
        thum_io = BytesIO()
        #It is commonly used when you need to work with binary data in memory
        img.save(thum_io, format='JPEG', quality=85)
        
        thumbnail = File(thum_io, name=image.name)
        
        return thumbnail
        
        
        