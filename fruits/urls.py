from django.urls import path
from . import views

app_name = 'fruits'
urlpatterns = [
	path('', views.home, name='home'),
	path('store/', views.store, name='store'),
    
	####################### FOR CATEGORIES #################
    
	path('categories/', views.categories, name='categories'),

	########################   CLOTHINGS  ########################
    
	path('categories/bags', views.bags, name='bags'),
	path('categories/blouses', views.blouses, name='blouses'),
	path('categories/gele', views.gele, name='gele'),
	path('categories/gowns', views.gowns, name='gowns'),
	path('categories/shoes', views.shoes, name='shoes'),
	path('categories/tops', views.tops, name='tops'),
    
	#########################   OTHERS   ########################

	path('categories/jewelries', views.jewelries, name='jewelries'),
	path('categories/make-ups', views.make_ups, name='make-ups'),
	path('categories/purses', views.purses, name='purses'),
	path('categories/wigs', views.wigs, name='wigs'),
	path('categories/sanitaries', views.sanitaries, name='sanitaries'),
	path('categories/sunglasses', views.sunglasses, name='sunglasses'),




	path('cart/', views.cart, name='cart'),
	path('product/<int:pk>', views.product, name='product'),
    
	path('checkout/', views.checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
	path('process_order/', views.processOrder, name='process_order'),

]