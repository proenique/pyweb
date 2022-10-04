from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify 
from django.utils.translation import gettext_lazy as _
from django.utils.html import format_html
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.timezone import now

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatars/default.png', upload_to='avatars')
    skill = models.CharField(default='', max_length=50)
    phone = PhoneNumberField(blank=True)
    
    joined = models.DateTimeField(default=now, auto_now=False, auto_now_add=False)
    slug = models.SlugField(unique=True, null=True)
    
    class Meta:
        verbose_name = _("profile")
        verbose_name_plural = _("profiles")

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("users:user_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs): # new
        if not self.slug:
            self.slug = slugify(self.user.username)
        return super().save(*args, **kwargs)

    def avatar_tag(self):
        return format_html('<img src="/media/avatars/{}" style="width:40px;height:40px;border-radius:50%"  />'.format(self.avatar))