from django.contrib import admin
from .models import item,auction,live_auction

# Register your models here.
class AuctionInLine(admin.StackedInline):
    model = auction

class ItemAdmin(admin.ModelAdmin):
    list_display = ('product_name','manufacture_year')
    inlines = [AuctionInLine, ]


admin.site.register(auction)
admin.site.register(item,ItemAdmin)
admin.site.register(live_auction)
