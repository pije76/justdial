from django.urls import path, re_path

from . import views

app_name = 'listing'

from .models import *
from .views import *

urlpatterns = [
    path('', home, name='home'),
    #   path('united-states/', us_country, name='us_country'),
    path('privacy/', privacy, name='privacy'),
    re_path(r'^(?P<country_id>[\w-]+)/$', region_list, name='region_list'),
    #   path('canada/', canada_country, name='canada_country'),
    #    path('<slug:slug>/', us_country, name='us_country'),
    #   path('united-states/<slug:slug>/', us_region, name='us_region'),
    #   re_path(r'^united-states/(?P<region_slug>[\w-]+)', us_region, name='us_region'),
    #   path('united-states/<region_slug>/', us_region, name='us_region'),
    #   re_path(r'^(?P<country_id>[\w-]+)/(?P<region_id>\d+)/$', city_list, name='city_list'),
    re_path(r'^(?P<country_id>[\w-]+)/(?P<region_id>[\w-]+)/$', city_list, name='city_list'),


    #   re_path(r'^united-states/(?P<city_slug>[\w-]+)/$', us_region, name='us_region'),
    #   re_path(r'^united-states/(?P<region_slug>[\w-]+)/$', RegionList.as_view(), name='us_region'),
    #   re_path(r'^(?P<country_slug>[\w-]+)/(?P<region_slug>[\w-]+)/$', region_list, name='region_list'),
    #   re_path(r'^united-states/(?P<slug>[-\w]+)/$', us_cities, name='us_cities'),
    #   re_path(r'^(?P<slug>[-\w]+)/$', asia_cities, name='asia_cities'),
    #   re_path(r'^(?P<slug>\d+)/$', CityDetail.as_view()),

    #    re_path(r'^schools/(?P<country_slug>[\w-]+)/$', CountrySchoolList.as_view(), name='country_list'),
    #    re_path(r'^schools/(?P<country_slug>[\w-]+)/(?P<region_slug>[\w-]+)/$', ProvinceSchoolList.as_view(), name='region_list'),
    #    re_path(r'^schools/(?P<country_slug>[\w-]+)/(?P<region_slug>[\w-]+)/(?P<city_slug>[\w-]+)/$', CitySchoolList.as_view(), name='city_list'),
    re_path(r'^(?P<country_slug>[\w-]+)/(?P<region_id>[\w-]+)/(?P<city_id>[\w-]+)/$', listing_list, name='listing_list'),
    re_path(r'^(?P<country_slug>[\w-]+)/(?P<region_id>[\w-]+)/(?P<city_id>[\w-]+)/(?P<category_id>[\w-]+)/$', category_list, name='category_list'),
    re_path(r'^(?P<country_slug>[\w-]+)/(?P<region_id>[\w-]+)/(?P<city_slug>[\w-]+)/(?P<category_slug>[\w-]+)/(?P<slug>[\w-]+)/$', listing_detail, name='listing_detail'),

    path('category/', category, name='category'),
]
