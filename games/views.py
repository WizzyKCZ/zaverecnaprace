from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from games.models import Hra

from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from games.forms import HraModelForm
from django.contrib.auth.decorators import login_required


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


class HraCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Hra
    template_name = 'game/hra_bootstrap_form.html'
    form_class = HraModelForm
    permission_required = 'games.add_hra'
    login_url = '/accounts/login/'


class HraUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Hra
    template_name = 'game/hra_bootstrap_form.html'
    form_class = HraModelForm
    # fields = '__all__' # Not recommended (potential security issue if more fields added)
    permission_required = 'games.change_hra'
    login_url = '/accounts/login/'


class HraDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Hra
    success_url = reverse_lazy('hry')
    template_name = 'hra_confirm_delete.html'
    login_url = '/accounts/login/'
    permission_required = 'games.delete_hra'


def error_404(request, exception=None):
    return render(request, 'errors/404.html')


def error_500(request):
    return render(request, 'errors/500.html')


def error_403(request, exception=None):
    return render(request, 'errors/403.html')


def error_400(request, exception=None):
    return render(request, 'errors/400.html')

