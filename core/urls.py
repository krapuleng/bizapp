# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("",admin.site.urls),
    #path("", include("apps.home.urls")),            # UI Kits Html files
    #path("cash/", include("apps.appcash.urls"))             # UI Kits Html files
]
admin.site.site_header = "Cash Management"
admin.site.site_title = "Cash Management"
admin.site.index_title = ""