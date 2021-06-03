"""foodfun URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from foodapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home_view),
    path('aboutus/', views.aboutus_view),
    path('menu/', views.menu_view),
    path('contactus/', views.contactus_view),
    path('contactuslist/', views.contactuslist_view),
    path('reservation/', views.reservation_view),
    path('reservationlist/', views.reservationlist_view),
    path('food_list/', views.foodlist_view),
    path('addfood/', views.addfood_view),
    path('updatefood/<int:foodId>', views.updatefood_view, name='updatefood'),
    path('deletefood/<int:foodId>', views.deletefood_view, name='delete'),
    path('customerlist/', views.customerlist_view),
    path('signup/', views.signup_view),
    path('register/', views.register_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('cart/', views.cart),
    path('updateitem/', views.updateItem),
    path('updateprofile/', views.updateprofile_view, name='updateprofile'),
    path('profile/', views.profile_view),
    path('orderlist/', views.orderlist_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
