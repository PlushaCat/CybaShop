from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .forms import *
from .models import *
# Create your views here.
from django.views.generic import *


def index(request):
    return render(request, "index.html")


def catalogue(request):
    good = Goods.objects.all()
    firstrow = good[:good.count() / 2]
    tworow = good[good.count() / 2:good.count()]
    category = Category.objects.all()
    return render(request, "index2.html", {'good': good, 'category': category, 'firstrow': firstrow,
                                           'tworow': tworow})


def show_category(request, cat_id=1):
    good_with_category = Goods.objects.filter(cat_id=cat_id)
    firstrow = good_with_category[:good_with_category.count() / 2]
    tworow = good_with_category[good_with_category.count() / 2:good_with_category.count()]
    category = Category.objects.all()
    return render(request, "index2.html", {'good': good_with_category, 'firstrow': firstrow,
                                           'tworow': tworow, 'category': category})

def register(request):
    return render(request, "index4.html")


def login(request):
    return render(request, "index3.html")


def profile(request):
    return render(request, "index6.html")


def ViewOrderForm(request, good_id):
    good = Goods.objects.get(id=good_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            try:
                Order.objects.create(**form.cleaned_data)
                return redirect("catalog")
            except:
                form.add_error(None, 'Ошибка заказа')
    else:
        form = OrderForm()

    return render(request, "index5.html", {'form': form, 'good': good})

def logout_user(request):
    logout(request)
    return redirect('login')


def search_task(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ""
    results = Goods.objects.filter(name__icontains=q)
    return render(request, 'task_list.html', {'results': results})

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'index4.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'index3.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

