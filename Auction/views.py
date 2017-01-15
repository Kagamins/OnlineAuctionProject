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
from django import forms
from django.http import *




@login_required
def createAuction(request):

    if request.method == 'POST':
        form = newAuctionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/')
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

@login_required
def createLiveAuction(request):

    if request.method == 'POST':
        form = newLiveAuctionForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect('/')
    else:

        form = newLiveAuctionForm(initial={'owner': request.user.pk,'auction_user':request.user.pk
                                       })

    return render(
        request,
        'createLiveAuction.html',
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
    widgets = {
    'user' : forms.HiddenInput,
    'auction_date' : DateWidget(bootstrap_version=3),
    'auction_time' : TimeWidget(bootstrap_version=3)

    }

@login_required
def edit_auction(request,pk):
    auction = get_object_or_404(auction,pk=pk)
    if request.method =='POST':
        form = newAuctionForm(request.POST, instance=auction)
        if form.is_Valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = newAuctionForm(instance=auction)
        return render (request,'editAuction.html',{'form':form, 'auction' : auction})

@login_required
def bid_auction(request,pk):
    auction = get_object_or_404(live_auction,pk=pk)
    bidders = bid.objects.filter(l_auction=auction)
    if request.user != auction.auction.user:
        if request.method == 'POST':
            form = newBidForm(request.POST)
            if form.is_valid():
                message.objects.create(sender=request.user,receiver=auction.auction.user,subject="Notification:Bid",body="The Potentil Buyer "+request.user.username+" is Bidding On the Product "+auction.auction.product.product_name)
                form.save()
                return HttpResponseRedirect('/')
        else:
            form = newBidForm(
                initial={'Bidder': request.user.pk,'l_auction': auction.pk})
        return render(request, 'bidAuction.html', {'form': form,'live_auction': auction,'bids':bidders})
    else:
        raise Http404


@login_required
def update_bid_auction(request, pk):
    obj = get_object_or_404(bid,pk=pk)
    if request.method == 'POST':
        form = UpdateBidForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UpdateBidForm(instance=obj)
    return render(request, 'update_bidAuction.html', {'form': form,'bid':obj})


class Bid_Auction(UpdateView):
    model = bid
    login_required = True
    fields = ['User_bid', 'l_auction']
    context_object_name = 'bid'
    template_name = 'update_bidAuction.html'


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

            return HttpResponseRedirect('/')
    else:
        form = newProductForm(initial={'owner': request.user})
    return render(request, 'createItem.html', {'form': form})


def product_details(request, pk):
    obj = get_object_or_404(item, pk=pk)
    pictures_list = [x for x in obj.pictures.all()]
    return render(request, 'product_details.html', {
        'item': obj,'picturs':pictures_list},)


def auction_details(request, pk):
    obj = get_object_or_404(live_auction, pk=pk)
    obj_d = get_object_or_404(auction, pk=obj.auction_id)
    bids = bid.objects.filter(l_auction_id=obj.auction_id).order_by('-User_bid')
    return render(request, 'auctiondetail.html', {'auction': obj_d, 'bidders': bids,'live_auction':obj})


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

                return HttpResponseRedirect('/')
        else:
            form = newProductForm(instance=obj)
        return render(request, 'editItem.html', {'form': form, 'p': obj})


@login_required
def payment_page(request):
    if request.method == 'POST':
        form = newPaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = newPaymentForm(initial={'User': request.user})
    return render(request, 'payment_page.html', {'form': form})

@login_required
def pictures_upload(request):
    if request.method =='POST':
        form = newPictureUpload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form= newPictureUpload(initial={'user':request.user.pk})
    return render (request,'upload_picture.html',{'form':form})

@login_required
def stop_auction(request,pk):
    liveauction = live_auction.objects.get(pk=pk)
    obj = bid.objects.filter(l_auction_id=pk).order_by('-User_bid')
    liveauction.winining_bid == obj[0].User_bid
    liveauction.auction_bidding_open = False
    message.objects.create(sender=liveauction.owner,receiver=obj[0].Bidder,subject="Notification:Winner",body=" Congratualtion Buyer "+obj[0].Bidder.username+" You Won the Product "+liveauction.auction.product.product_name)
    return HttpResponseRedirect('/')
