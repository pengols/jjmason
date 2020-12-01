from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=128)
    friendly_name = models.CharField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    original_author = models.CharField(max_length=254)
    illustrator = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    isbn = models.DecimalField(max_digits=12, decimal_places=0,null=True, blank=True)
    language = models.CharField(max_length=254, null=True, blank=True)
    num_pages = models.DecimalField(max_digits=4, decimal_places=0,null=True, blank=True)
    publication_year = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    publisher = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name