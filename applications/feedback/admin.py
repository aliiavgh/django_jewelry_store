from django.contrib import admin

from applications.feedback.models import Like, Review

admin.site.register(Like)
admin.site.register(Review)
