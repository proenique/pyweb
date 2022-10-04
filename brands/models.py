from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now
from apps.services.models import Service
# Create your models here.

class Brand(models.Model):

    user = models.OneToOneField(User, related_name='Brand', on_delete=models.CASCADE)
    
    logo = models.ImageField(default='logos/default.png', upload_to='logos')
    site_name = models.CharField(default='company name', max_length=50)
    site_url = models.URLField(default='www.companyname.co.zw', max_length=100)
    about_site = models.TextField()

    # Plan choices
    BASIC = 'BASIC'
    PRO = 'PRO'
    ENTERPRISE = 'ENTERPRISE'
    PLAN = [
        (BASIC, 'Basic'),
        (PRO, 'Pro'),
        (ENTERPRISE, 'Enterprise'),
    ]
    plan = models.CharField(max_length=10, choices=PLAN, default=BASIC,)
    created = models.DateTimeField(default=now, auto_now=False, auto_now_add=False)
    next_payment = models.DateField(default=now)
    last_service = models.DateField(default=now)
    active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, null=True)
    
    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("users:user_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)





