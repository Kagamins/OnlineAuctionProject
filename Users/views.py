from .models import *
from .forms import *
from django.shortcuts import *
from django.contrib.auth.decorators import *
from django.utils.decorators import *
from django.http import *
from django.views.generic import *
from django.shortcuts import *
from django.contrib import *
from django.core.urlresolvers import *
from django.views.generic.edit import *
from django.db.models import *
from Auction.models import *
# Create your views here.


class Create_User(CreateView):
    model = User
    context_object_name = 'user'
    exclude = ['user', ]
    template_name = 'Signup.html'


class Edit_User(UpdateView):
    model = User
    context_object_name = 'user'
    exclude = ['user', ]
    template_name = 'edit_profile.html'

@login_required
def edit_profile(request):
    obj = User.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = EditUserProfileForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()

            return redirect('home')
    else:
        form = EditUserProfileForm(instance=obj)
    return render(request,
                  'edit_profile.html',
                  {
                      'user': obj,
                      'form': form,
                  })


@login_required
def create_message(request):
    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = Message_Form(
            initial={'sender': request.user})
    return render(request, 'create_message.html', {'form': form})

def create_message_auction(request,pk):
    obj = User.objects.get(user_id=pk)
    if request.method == 'POST':
        form = Message_Form_Auction(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = Message_Form_Auction(
            initial={'sender': request.user,'receiver':obj})
    return render(request, 'create_message_auction.html', {'form': form,'receiver':pk})

@login_required
def view_message_details(request,pk):
    obj = message.objects.get(pk=pk)
    return render(request, 'message_details.html', {'message': obj})

@login_required
def view_message_list(request):
    obj = message.objects.filter(receiver_id=request.user.pk)
    return render(request, 'message_list.html', {'messages': obj})

@login_required
def my_page(request):
    my_messages = message.objects.filter(receiver=request.user)
    my_products = item.objects.filter(owner=request.user)
    my_auctions = auction.objects.filter(user=request.user)
    my_live_auctions = live_auction.objects.filter(
        owner=request.user)

    return render(request, 'my_page.html', {'messages': my_messages, 'products': my_products, 'auctions': my_auctions,'live_auctions': my_live_auctions})



def create_user_profile(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = SignupForm()
    return render(request, 'Signup.html', {'form': form})

def buyer_history(request):
    bids = bid.objects.filter(Bidder=request.user.pk)
    return render (request,'buying_history.html')

def seller_history(request):
    auction_ = auction.objects.filter(user=request.user.pk)
    return render (request,'selling_history.html',{'auction':auction_})
