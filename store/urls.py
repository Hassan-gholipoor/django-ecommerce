from django.urls import path

from . import views

urlpatterns = [
	path('', views.store, name="store"),
	path('product/<int:pk>/', views.productDetail, name='detail'),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path("signup/", views.SignUp.as_view(), name="signup"),
]