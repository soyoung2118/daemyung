from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.allProdCat, name='category'),
    path('<slug:c_slug>/', views.allProdCat, name = 'products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>', views.ProdCatDetail, name = 'ProdCatDetail'),
]