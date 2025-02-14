from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from django.shortcuts import get_list_or_404, get_object_or_404

from cities_light.models import *

from .models import *

# Create your views here.


def home(request):
    us_country = Country.objects.filter(code3='USA')
    us_region = Region.objects.filter(country__slug='united-states')
    canada_region = Region.objects.filter(country__slug='canada')
    uk_region = Region.objects.filter(country__slug='united-kingdom')
    australia_country = Country.objects.filter(continent='OC')
    africa_country = Country.objects.filter(continent='AF')
    asia_country = Country.objects.filter(continent='AS')
    middle_country = Country.objects.filter(continent='')
    europe_country = Country.objects.filter(continent="EU")
    latin_country = Country.objects.filter(continent='SA')
#    us_country = Country.objects.get(id=234)
    context = {
        'us_country': us_country,
        'us_region': us_region,
        'canada_region': canada_region,
        'uk_region': uk_region,
        'australia_country': australia_country,
        'africa_country': africa_country,
        'asia_country': asia_country,
        'middle_country': middle_country,
        'europe_country': europe_country,
        'latin_country': latin_country,
    }
    return render(request, "home.html", context)

def privacy(request):
    context = {
    }
    return render(request, "privacy.html", context)

def region_list(request, country_id):
    country_name = Country.objects.filter(id=country_id)
    regions = Region.objects.filter(country=country_id)
    context = {
        'country_name': country_name,
        'regions': regions,
    }
    return render(request, "region_list.html", context)


def city_list(request, country_id, region_id):
    region_name = Region.objects.filter(id=region_id)
    cities = City.objects.filter(region=region_id)
    #   flow = get_object_or_404(City, slug=slug)

    context = {
        'region_name': region_name,
        'cities': cities,
    }
    return render(request, "cities.html", context)


def listing_list(request, country_slug, region_id, city_id):
    categories = Category.objects.add_related_count(Category.objects.root_nodes(), Listing, 'category', 'cat_count', cumulative=True)
    region_name = Region.objects.filter(id=region_id).values_list('name', flat=True).first()
    city_name = City.objects.filter(id=city_id).values_list('name', flat=True).first()
    listing_list = Category.objects.all()
    context = {
        'categories': categories,
        'region_name': region_name,
        'city_name': city_name,
        'listing_list': listing_list,
    }
    return render(request, 'category.html', context)


def category_list(request, country_slug, region_id, city_id, category_id):
    categories = Category.objects.filter(id=category_id)
#    country_name = Country.objects.filter(id=country_id)
    region_name = Region.objects.filter(id=region_id).values_list('name', flat=True).first()
    city_name = City.objects.filter(id=city_id).values_list('name', flat=True).first()
    cities = City.objects.filter(region=region_id)
    listing_list = Listing.objects.filter(city_id=city_id, category=category_id)
    context = {
        'categories': categories,
#        'country_name': country_name,
        'region_name': region_name,
        'cities': cities,
        'city_name': city_name,
        'listing_list': listing_list,
    }
    return render(request, 'listing.html', context)


def listing_detail(request, country_slug, region_id, city_slug, category_slug, slug):
    categories = Category.objects.filter(slug=category_slug)
    region_name = Region.objects.filter(id=region_id)
    cities = City.objects.filter(region=region_id)
    city_name = City.objects.filter(slug=city_slug)
    listing_detail = Listing.objects.filter(slug=slug)
    context = {
        'categories': categories,
        'region_name': region_name,
        'cities': cities,
        'city_name': city_name,
        'listing_detail': listing_detail,
    }
    return render(request, 'view_ad.html', context)


def category(request):
    #    parentcategory = Category.objects.add_related_count(Category.objects.all(), Project, 'category', 'cat_count', cumulative=True)
    categories = Category.objects.add_related_count(Category.objects.root_nodes(), Listing, 'category', 'cat_count', cumulative=True)
    context = {
        'categories': categories,
    }
    return render(request, 'category.html', context)

