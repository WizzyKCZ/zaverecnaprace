from django.shortcuts import render
from django.views.generic import DetailView
from games.models import Hra


def index(request):
    """View function for home page of site."""

    num_hras = Hra.objects.all().count()
    hras = Hra.objects.order_by('-jazyk')[:3]

    context = {
        'num_hras': num_hras,
        'hras': hras
    }

    return render(request, 'index.html', context=context)


def HraListView(request):
    num_hras = Hra.objects.all().count()
    hras = Hra.objects.all()

    context = {
        'num_hras': num_hras,
        'hras': hras
    }

    return render(request, 'index.html', context=context)


class HraDetailView(DetailView):
    model = Hra

    context_object_name = 'hra_detail'
    template_name = 'game/detail.html'
