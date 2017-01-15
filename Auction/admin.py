from django.contrib import admin
from .models import *

# Register your models here.
class AuctionInLine(admin.StackedInline):
    model = auction

class ItemAdmin(admin.ModelAdmin):
    list_display = ('product_name','manufacture_year')
    inlines = [AuctionInLine, ]

class PictureAdmin(admin.ModelAdmin):
    list_display=('tittle',)

class AuctionAdmin(admin.ModelAdmin):
    list_display = ('auction_date','auction_time','user')

admin.site.register(auction,AuctionAdmin)
admin.site.register(item,ItemAdmin)
admin.site.register(live_auction)
admin.site.register(bid)
admin.site.register(Picture,PictureAdmin)
