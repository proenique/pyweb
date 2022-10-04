from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class SiteInfo(models.Model):
    """Model definition for SiteInfo."""

    # TODO: Define fields here
    name = models.CharField(default='site name', max_length=50)
    logo = models.ImageField(default='site_image/logo.png', upload_to='site_image/')
    members = models.ManyToManyField(User)
    moto = models.CharField(default='', max_length=50)
    about = models.TextField(default='')
    vision = models.TextField(default='')
    mission = models.TextField(default='')
    info_email = models.EmailField(default='', max_length=254)
    sales_email = models.EmailField(default='', max_length=254)
    support_email = models.EmailField(default='', max_length=254)
    call_number = PhoneNumberField(blank=True)
    whatsapp_number = PhoneNumberField(blank=True)
    facebook = models.URLField(blank=True, max_length=200)
    twiter = models.URLField(blank=True, max_length=200)
    instagram = models.URLField(blank=True, max_length=200)
    published = models.DateField(default=now)

    class Meta:
        """Meta definition for SiteInfo."""

        verbose_name = 'Site Info'
        verbose_name_plural = 'Site Information'

    def __str__(self):
        """Unicode representation of SiteInfo."""
        return self.name


