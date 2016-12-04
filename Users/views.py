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


@login_required
def view_message_details(request):
    obj = message.objects.filter(receiver=request.user)
    if obj:
        return render(request, 'view_message_list.html', {'messages': obj})
    else:
        return render(request, 'view_message_list.html', {'messages': obj})


def create_user_profile(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = SignupForm()
    return render(request, 'Signup.html', {'form': form})
