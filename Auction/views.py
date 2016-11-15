from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView,DetailView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.db.models import Avg, Max, Min
from .forms import newAuctionForm, newProductForm
from .models import auction,live_auction, item




@login_required
def createAuction(request):

    if request.method == 'POST':
        form = newAuctionForm(request.POST, request.FILES)
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
    # we require all fields since students will need register him/her self
    fields = '__all__'
    template_name = 'createAuction.html'

class Edit_Auction(UpdateView):
    model = auction
    fields = '__all__'
    context_object_name = 'auction'
    template_name = 'editAuction.html'

class Bid_Auction(CreateView):
    model = live_auction
    exclude = ['auction','Bidder_name','Time_of_Bid']
    context_object_name = 'auction'
    template_name = 'bidAuction.html'

class Create_Product(FormView):
    model = item
    context_object_name = 'product'
    template_name = 'createItem.html'

def create_product(request):
    if request.method == 'POST':
        form = newProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = newProductForm()
    return render(request, 'createItem.html', {'form': form})
