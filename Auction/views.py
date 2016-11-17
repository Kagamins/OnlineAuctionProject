from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.db.models import Avg, Max, Min
from .forms import newAuctionForm, newProductForm,newBidForm
from .models import auction, live_auction, item,bid


@login_required
def createAuction(request):

    if request.method == 'POST':
        form = newAuctionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect(obj)
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

    if request.method == 'POST':
        form = newBidForm(request.POST,instance=auction)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = newBidForm(initial={'l_auction': pk,'Bidder':request.user})
    return render(request, 'bidAuction.html', {'form': form,'live_auction':auction})


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


def index_page(request):
    obj = live_auction.objects.all().order_by('-id')
    queryset = item.objects.all()
    bidobj = bid.objects.filter(l_auction_id=obj[0].pk)
    if request.method == 'POST':
	     qs = item.objects.filter(product_name__icontains=request.POST['term'])
	     return render(request, 'Index.html',
                 {'auction': obj,
                 'product':queryset,
                 'item_search':qs,
                 'bids':bidobj})
    else:
        return render(request, 'Index.html',
                         {'auction': obj,
                         'product':queryset,
                         'bids':bidobj})
