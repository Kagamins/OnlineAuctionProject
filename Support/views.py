from django.contrib.auth.decorators import *
from django.utils.decorators import *
from django.http import *
from django.views.generic import *
from django.shortcuts import *
from django.contrib import *
from django.core.urlresolvers import *
from django.views.generic.edit import *
from django.db.models import *
from .models import *
from .forms import *
# Create your views here.


@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = Message_Form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = Newticketform(
            initial={'user': request.user})
    return render(request, 'create_ticket.html', {'form': form})


def support_page(request):
    questions_answers_account_support = FAQ.objects.filter(category='Account support')
    questions_answers_technical_support = FAQ.objects.filter(category="technical support")
    questions_answers_transaction_support = FAQ.objects.filter(category="transaction support")
    return render(request, 'support_page.html', {'QAAS': questions_answers_account_support, 'QATS': questions_answers_technical_support, 'QATrS': questions_answers_transaction_support})
