from django.contrib.auth.decorators import *
from django.utils.decorators import *
from django.http import *
from django.views.generic import *
from django.shortcuts import *
from django.contrib import *
from django.core.urlresolvers import *
from django.views.generic.edit import *
from django.db.models import *
from .forms import *
from .models import *
from django.core.paginator import *

@login_required
def createAuction(request):

    if request.method == 'POST':
        form = newAuctionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/success/url/')
    else:

        form = newAuctionForm(initial={'user': request.user.pk,
                                       })

    return render(
        request,
        'createAuction.html',
        {
            "form": form,
        }
    )


class Create_Auction(CreateView):
    model = auction
    fields = '__all__'
    template_name = 'createAuction.html'


class Edit_Auction(UpdateView):
    model = auction
    fields = '__all__'
    context_object_name = 'auction'
    template_name = 'editAuction.html'


@login_required
def bid_auction(request,pk):
    auction = get_object_or_404(live_auction, pk=pk)
    bidders = bid.objects.filter(l_auction_id=pk)
    if request.method == 'POST':
        form = newBidForm(request.POST,instance=auction)
        if form.is_valid():
            print('form is valid :D')
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = newBidForm(initial={'l_auction': auction,'Bidder':request.user})
    return render(request, 'bidAuction.html', {'form': form,'live_auction':auction,'bids':bidders})


class Bid_Auction(UpdateView):
    model = bid
    fields = ['User_bid', 'Time_of_Bid', ]
    context_object_name = 'live_auction'
    template_name = 'bidAuction.html'


class Create_Product(FormView):
    model = item
    context_object_name = 'product'
    template_name = 'createItem.html'


class View_Auction(DetailView):
    model = auction
    context_object_name = 'auction'
    template_name = 'auctiondetail.html'



@login_required
def create_product(request):
    if request.method == 'POST':
        form = newProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = newProductForm()
    return render(request, 'createItem.html', {'form': form})

def product_details(request,pk):
        obj = get_object_or_404(item, pk=pk)
        #alist = [x for x in obj]
        return render(request,'product_details.html', {
        'item': obj},)

def index_page(request):
    obj = live_auction.objects.all().order_by('-id')
    premium_obj= live_auction.objects.filter(auction__auction_type='P')
    queryset = item.objects.all().order_by('-id')
    paginator = Paginator(queryset,5)
    page = request.GET.get('page')
    #for o in queryset:
    #    queryset_dict[o.product_name] = [o.manufacture_year,o.product_description,o.picture];

    if request.method == 'POST':
	     qs = item.objects.filter(product_name__icontains=request.POST.get('term',False))
	     return render(request, 'Index.html',
                 {'auction': obj,
                 'p_auction':premium_obj,
                 'product':queryset,
                 'item_search':qs})
    else:
        return render(request, 'Index.html',
                         {'auction': obj,
                         'p_auction':premium_obj,
                         'product':queryset})
