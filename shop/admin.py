from django.contrib import admin
from .models import Contact, IceCream, Testimonial, Service


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(IceCream)
class IceCreamAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
    search_fields = ('name', 'text')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)