from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify 
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Product(models.Model):
    """Model definition for Product."""

    # TODO: Define fields here
    name = models.CharField(default='Basic', max_length=50)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name

class Plan(models.Model):
    """Model definition for Plan."""

    # TODO: Define fields here
    name = models.CharField(default='Basic', max_length=50)
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    package = models.FloatField(blank=True, null=True)
    products = models.ManyToManyField('Product')
    slug = models.SlugField(unique=True, null=True)
    overview = models.TextField()


    class Meta:
        """Meta definition for Plan."""

        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'

    def __str__(self):
        """Unicode representation of Plan."""
        return self.name

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.service.slug)
        return super().save(*args, **kwargs)

class Service(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    image = models.ImageField(default='services/default.png', upload_to='services/', blank=True)
    name = models.CharField(default='', max_length=50)
    about = models.TextField()

    slug = models.SlugField(unique=True, null=True)
    class Meta:
        """Meta definition for Service."""

        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self):
        """Unicode representation of Service."""
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Service."""
        return reverse("services:service_detail", kwargs={"slug": self.slug})

    # TODO: Define custom methods here

class OtherService(models.Model):
    """Model definition for Service."""

    # TODO: Define fields here
    image = models.ImageField(default='services/default.png', upload_to='services/', blank=True)
    name = models.CharField(default='', max_length=50)
    about = models.TextField()

    slug = models.SlugField(unique=True, null=True)
    class Meta:
        """Meta definition for Other Service."""

        verbose_name = _('Other Service')
        verbose_name_plural = _('Other Services')

    def __str__(self):
        """Unicode representation of Other Service."""
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Return absolute url for Service."""
        return reverse("services:service_detail", kwargs={"slug": self.slug})

    # TODO: Define custom methods here
