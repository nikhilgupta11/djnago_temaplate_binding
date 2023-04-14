from django.contrib import admin

from .models import (
    AboutUs,
    WhyUs,
    Services,
    OurSpace,
    ContactUs,
    SocialMediaLinks,
    MutualFunds,
    ContactDetails

)

admin.site.site_header = 'Administration'
admin.site.site_title = 'Happy Niveshak'

# Register your models here.
admin.site.register(AboutUs)
admin.site.register(WhyUs)
admin.site.register(Services)
admin.site.register(OurSpace)
admin.site.register(ContactUs)
admin.site.register(SocialMediaLinks)
admin.site.register(MutualFunds)
admin.site.register(ContactDetails)