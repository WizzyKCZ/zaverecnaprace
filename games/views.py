from django.shortcuts import render
from games.models import Hra


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_hras = Hra.objects.all().count()
    hras = Hra.objects.order_by('-jazyk')[:3]

    context = {
        'num_hras': num_hras,
        'hras': hras
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

def topten(request):
    """
    View function for home page of site.
    """
    # Render the HTML template index.html
    return render(
        request,
        'topten.html',
    )