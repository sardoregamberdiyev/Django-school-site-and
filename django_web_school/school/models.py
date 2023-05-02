from django.db import models

# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    content = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128, blank=True, null=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.content)

        super(Category, self).save(*args, **kwargs)


class Recipe(models.Model):
    name = models.CharField(max_length=256)
    img = models.ImageField()
    text = models.TextField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

