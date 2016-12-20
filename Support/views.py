from django.shortcuts import render

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
