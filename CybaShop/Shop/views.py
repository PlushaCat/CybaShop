from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from .forms import *
from .models import *
# Create your views here.
from django.views.generic import *


def index(request):
    category = Category.objects.all()
    return render(request, "index.html", {'category': category})

def reports(request):
    total_good_quantity = len(Goods.objects.all())
    total_good_price = sum((i.price for i in Goods.objects.all()))
    total_user_quantity = len(User.objects.all())
    total_orders_quantity = len(Order.objects.all())

    order = Order.objects.all()
    return render(request, "index7.html", {'goods_quantity': total_good_quantity, 'total_good_price': total_good_price, 'total_user_quantity':
                                           total_user_quantity, 'total_orders_quantity': total_orders_quantity})

def catalogue(request):
    good = Goods.objects.all()

    category = Category.objects.all()
    return render(request, "index2.html", {'good': good, 'category': category})


def show_category(request, cat_id=1):
    good_with_category = Goods.objects.filter(cat_id=cat_id)
    category = Category.objects.all()
    return render(request, "index2.html", {'good': good_with_category, 'category': category})

def register(request):
    return render(request, "index4.html")


def login(request):
    return render(request, "index3.html")


def profile(request):
    return render(request, "index6.html", context={'Basket': Basket.objects.filter(user=request.user)})


def ViewOrderForm(request):
    basket = Basket.objects.filter(user=request.user)
    basket_data = {'basket': basket}
    if request.method == 'POST':
        form = OrderForm(request.POST, basket_data)
        if form.is_valid():
            try:
                Order.objects.create(**form.cleaned_data)
                return redirect("catalog")
            except:
                form.add_error(None, 'Ошибка заказа')
    else:
        form = OrderForm()

    return render(request, "index5.html", {'form': form, 'Basket': basket})

def logout_user(request):
    logout(request)
    return redirect('login')


def search_task(request):
    q = request.GET.get('q')
    if len(q) > 0:
        results = Goods.objects.filter(name__iregex=q)
    else:
        results = None
    return render(request, 'task_list.html', {'results': results})
@login_required
def basket_add(request, good_id):
    good = Goods.objects.get(id=good_id)
    baskets = Basket.objects.filter(user=request.user, good=good)

    if not baskets.exists():
        Basket.objects.create(user=request.user, good=good, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
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

