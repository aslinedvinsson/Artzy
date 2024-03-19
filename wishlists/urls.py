from django.urls import path
from . import views

app_name = 'wishlists'

urlpatterns = [
    path('wishlists/', views.user_wishlists, name='user_wishlists'),
    path('wishlists/add/<int:item_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlists/remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlists/add_wish_to_cart/<int:item_id>/', views.add_wish_to_cart, name='add_wish_to_cart'),
]

