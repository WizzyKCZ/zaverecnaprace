from django.shortcuts import render
from games.models import Hra

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from games.forms import HraModelForm


def index(request):
    """View function for home page of site."""

    num_hras = Hra.objects.all().count()
    hras = Hra.objects.order_by('jazyk')[:3]

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

    return render(request, 'game/list.html', context=context)


class HraDetailView(DetailView):
    model = Hra

    context_object_name = 'hra_detail'
    template_name = 'game/detail.html'


class HraCreate(CreateView):
    model = Hra
    template_name = 'game/hra_bootstrap_form.html'
    form_class = HraModelForm


class HraUpdate(UpdateView):
    model = Hra
    template_name = 'game/hra_bootstrap_form.html'
    form_class = HraModelForm
    # fields = '__all__' # Not recommended (potential security issue if more fields added)


class HraDelete(DeleteView):
    model = Hra
    success_url = reverse_lazy('hry')
    template_name = 'hra_confirm_delete.html'
