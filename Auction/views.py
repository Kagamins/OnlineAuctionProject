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
from Users.models import message
from django.core.paginator import *


@login_required
def my_page(request):
    my_messages = message.objects.filter(receiver=request.user)
    my_products = item.objects.filter(owner=request.user)
    my_auctions = auction.objects.filter(user=request.user)
    my_live_auctions = live_auction.objects.filter(
        owner=request.user)

    return render(request, 'my_page.html', {'messages': my_messages, 'products': my_products, 'auctions': my_auctions,'live_auctions': my_live_auctions})


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
def bid_auction(request, pk):
    auction = get_object_or_404(live_auction, pk=pk)
    bidders = bid.objects.filter(l_auction_id=pk)
    if request.method == 'POST':
        form = newBidForm(request.POST, instance=auction)
        if form.is_valid():
            print('form is valid :D')
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = newBidForm(
            initial={'l_auction': auction, 'Bidder': request.user})
    return render(request, 'bidAuction.html', {'form': form, 'live_auction': auction, 'bids': bidders})


@login_required
def update_bid_auction(request, pk):
    auction = get_object_or_404(live_auction, pk=pk)
    bidders = bid.objects.filter(l_auction_id=pk)
    if request.method == 'POST':
        form = newBidForm(request.POST, instance=auction)
        if form.is_valid():
            print('form is valid :D')
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = newBidForm(
            initial={'l_auction': auction, 'Bidder': request.user})
    return render(request, 'bidAuction.html', {'form': form, 'live_auction': auction, 'bids': bidders})


class Bid_Auction(UpdateView):
    model = bid
    login_required = True
    fields = ['User_bid', 'l_auction']
    context_object_name = 'live_auction'
    template_name = 'bidAuction.html'

    def get_queryset(self):
        return bid.objects.filter(l_auction=self.kwargs['pk'])


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
            messages.success(request, 'Product  has been  successfully added.')

            return HttpResponseRedirect('/success/url/')
    else:
        form = newProductForm(initial={'owner': request.user})
    return render(request, 'createItem.html', {'form': form})


def product_details(request, pk):
    obj = get_object_or_404(item, pk=pk)
    #alist = [x for x in obj]
    return render(request, 'product_details.html', {
        'item': obj},)


def auction_details(request, pk):
    obj = get_object_or_404(live_auction, pk=pk)
    obj_d = get_object_or_404(auction, pk=obj.auction_id)
    bids = bid.objects.filter(l_auction_id=obj.auction_id)
    return render(request, 'auctiondetail.html', {'auction': obj_d, 'bidders': bids})


def index_page(request):
    obj = live_auction.objects.all().order_by('-id')
    premium_obj = live_auction.objects.filter(
        auction__auction_type='P')
    queryset = item.objects.all()
    paginator = Paginator(queryset, 2)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    if request.method == 'POST':
        qs = item.objects.filter(
            product_name__icontains=request.POST.get('term', False))
        return render(request, 'Index.html',
                      {'auction': obj,
                       'p_auction': premium_obj,
                       'product': items,
                       'item_search': qs})
    else:
        return render(request, 'Index.html',
                      {'auction': obj,
                       'p_auction': premium_obj,
                       'product': items})


def index_car_filter(request):
    obj = item.objects.filter(product_type='C')
    paginator = Paginator(obj, 2)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'Index_Car.html', {'product': obj})


def index_part_filter(request):
    obj = item.objects.filter(product_type='P')
    paginator = Paginator(obj, 1)
    page = request.GET.get('page')
    try:
        items = paginator.page(page)
    except PageNotAnInteger:
        items = paginator.page(1)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'Index_Part.html', {'product': items})


@login_required
def delete_product(request, pk):
    obj = item.objects.get(pk=pk)
    if request.user == obj.owner:
        obj.delete()
    return render(request, 'Index.html')


@login_required
def edit_product(request, pk):
    obj = item.objects.get(pk=pk)
    if request.user == obj.owner:
        if request.method == 'POST':
            form = newProductForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'Product  has been  successfully edited.')

                return HttpResponseRedirect('/success/url/')
        else:
            form = newProductForm(instance=obj)
        return render(request, 'editItem.html', {'form': form, 'p': obj})


@login_required
def payment_page(request):
    if request.method == 'POST':
        form = newPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = newPaymentForm(initial={'User': request.user})
    return render(request, 'payment_page.html', {'form': form})
