from . import views

from django.urls import path

urlpatterns = [
    
    path("", views.index, name="Shopapp"),
    path("about/", views.about, name="About Us"),
    path("contact/", views.contact, name="Contact"),
    path("track/", views.track, name="TrackingStatus"),
    path("search/", views.search, name="Search"),
    path("prodview/<int:myid>", views.prodview, name="ProductView"),
    path("checkout", views.checkout, name="Checkout"),
]
