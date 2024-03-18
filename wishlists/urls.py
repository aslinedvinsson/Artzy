from django.urls import path
from . import views

app_name = 'wishlists'

urlpatterns = [
    path('wishlists/', views.user_wishlists, name='wishlists'),
    path('wishlists/add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlists/remove/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),

]