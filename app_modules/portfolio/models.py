from django.db import models
from tinymce.models import HTMLField


# Create your models here.

class AboutUs(models.Model):
    description1 = HTMLField()
    description2 = HTMLField(blank=True)

    def __str__(self):
        return "About Us Description"

    class Meta:
        verbose_name = verbose_name_plural = "About Us"

    def save(self, *args, **kwargs):
        if not self.pk and AboutUs.objects.exists():
            return None
        return super(AboutUs, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return None


class WhyUs(models.Model):
    whyus_heading = models.CharField(max_length=80)
    whyus_description = HTMLField()
    philosphy_heading = models.CharField(max_length=80)
    philosphy_description = HTMLField()

    def __str__(self):
        return "WhyUs and Philosphy"

    class Meta:
        verbose_name = verbose_name_plural = "Why Us and Philosphy"

    def save(self, *args, **kwargs):
        if not self.pk and WhyUs.objects.exists():
            return None
        return super(WhyUs, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return None


class Services(models.Model):
    heading = models.CharField(max_length=30)
    description = models.CharField(max_length=100)

    def __str__(self):
        return f"Service: {self.heading}"

    class Meta:
        verbose_name = verbose_name_plural = "Services"

    def delete(self, *args, **kwargs):
        return None


class OurSpace(models.Model):
    name = models.CharField(max_length=100, default="Our Space")
    photo = models.ImageField(upload_to="OurSpace")
    
    def __str__(self):
        return f"Our Space Photo: {self.name}-{self.id}"

    class Meta:
        verbose_name = verbose_name_plural = "Our Space"

    def delete(self, *args, **kwargs):
        return None


class ContactUs(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    unread = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} (Subject: {self.subject})"

    class Meta:
        verbose_name = verbose_name_plural = "Contact Us"

    def delete(self, *args, **kwargs):
        return None


class SocialMediaLinks(models.Model):
    logo = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    link = models.URLField(max_length=250, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Social Media Links"

    def save(self, *args, **kwargs):
        objs = SocialMediaLinks.objects.all()
        if not self.pk and len(objs) >= 5 :
            return None
        return super(SocialMediaLinks, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return None


class MutualFunds(models.Model):
    name = models.CharField(max_length=100, default="Mutual Funds")
    photo = models.ImageField(upload_to="MutualFunds")
    
    def __str__(self):
        return f"Mutual Funds Photo: {self.name}"

    class Meta:
        verbose_name = verbose_name_plural = "Mutual Funds"

    def delete(self, *args, **kwargs):
        return None


class ContactDetails(models.Model):
    address = HTMLField()
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return "Contact Details"

    class Meta:
        verbose_name = verbose_name_plural = "Contact Details"

    def save(self, *args, **kwargs):
        if not self.pk and ContactDetails.objects.exists():
            return None
        return super(ContactDetails, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return None

