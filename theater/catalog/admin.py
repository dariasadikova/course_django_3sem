from django.contrib import admin
from .models import Play, Genre, Actor, Ticket, Booking, Viewer, Review
from import_export import resources
from import_export.admin import ImportExportModelAdmin

admin.site.register(Genre)

class PlayResource(resources.ModelResource):
  
  class Meta:
    model = Play
    

class ReviewInline(admin.TabularInline):
    model = Review   

@admin.register(Play) 
class PlayAdmin(ImportExportModelAdmin):
    list_display = ('name', 'display_genre', 'director', 'datetime')
    list_filter = ('name', 'director')
    filter_horizontal = ('genre',)
    date_hierarchy = 'datetime'
    inlines = [ReviewInline]
    resources_classes = [PlayResource]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('viewer', 'play', 'amount', 'status')
    list_filter = ('play', 'status')

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_of_birth', 'contact')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('viewer', 'play', 'text', 'mark')
    list_filter = ('play', 'mark')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('play', 'seatkind', 'seatnum', 'price', 'status')
    list_filter = ('play', 'price', 'status')

@admin.register(Viewer)
class ViewerAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'contact', 'visits')
