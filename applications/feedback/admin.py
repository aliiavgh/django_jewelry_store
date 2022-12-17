from django.contrib import admin

from applications.feedback.models import Like, Review, Favorite, Rating

admin.site.register(Like)
admin.site.register(Review)
admin.site.register(Favorite)
admin.site.register(Rating)
