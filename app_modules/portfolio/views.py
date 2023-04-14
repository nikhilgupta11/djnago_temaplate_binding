from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from .models import (
    AboutUs,
    WhyUs,
    Services,
    OurSpace,
    ContactUs,
    SocialMediaLinks,
    MutualFunds,
    ContactDetails,
)
from .forms import ContactUsForm


# Create your views here.
def landing_page(request):
    return render(request, "portfolio/landing.html")


def home_view(request):
    contact_form = ContactUsForm()
    about_us = AboutUs.objects.all().first()
    why_us = WhyUs.objects.all().first()
    services = Services.objects.order_by('?')
    our_space = OurSpace.objects.all()
    social_media_links = SocialMediaLinks.objects.all()
    mutual_funds = MutualFunds.objects.all()
    contact_details = ContactDetails.objects.all().first()

    context = {
        "about_us": about_us,
        "why_us": why_us,
        "services": services,
        "our_space": our_space,
        "social_media_links": social_media_links,
        "mutual_funds": mutual_funds,
        "contact_details": contact_details,
        "contact_form": contact_form,
    }
    return render(request, "portfolio/index.html", context)


def contact_us(request):

    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("OK")
        return HttpResponse(form.errors)
