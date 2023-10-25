from django.template.context_processors import static
from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("catalog/", views.catalogue, name="catalog"),
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("login/", views.LoginUser.as_view(), name="login"),
    path("Order/<int:good_id>/", views.ViewOrderForm, name="OrderForm"),
    path("Profile/", views.profile, name="profile"),
    path("logout/", views.logout_user, name="logout"),
    path("catalog/<int:cat_id>/", views.show_category, name="category_page"),
    path("Search_products/", views.search_task, name="search")
]

