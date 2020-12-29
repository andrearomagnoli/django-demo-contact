from django.shortcuts import render

from .forms import ContactModelForm


def contact_view(request):
    """Contact form."""

    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            message = form.save()
            return render(request, 'contact/success.html', {'sender': message.name})
    else:
        form = ContactModelForm()

    return render(request, 'contact/new.html', {'form': form})
