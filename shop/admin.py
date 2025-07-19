from django.contrib import admin
from .models import Contact, IceCream, Testimonial , Service
from unfold.admin import ModelAdmin as UnfoldModelAdmin

@admin.register(Contact)
class ContactAdmin(UnfoldModelAdmin):
    list_display = ('name', 'email', 'phone')

@admin.register(IceCream)
class IceCreamAdmin(UnfoldModelAdmin):
    list_display = ('name', 'price')


@admin.register(Testimonial)
class TestimonialAdmin(UnfoldModelAdmin):
    list_display = ('name', 'text')
    search_fields = ('name', 'text')

    from .models import Service

@admin.register(Service)
class ServiceAdmin(UnfoldModelAdmin):
    list_display = ('title',)