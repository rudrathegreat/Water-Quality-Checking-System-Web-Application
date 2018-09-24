from django.conf.urls import url
from django.conf.urls.static import static
from WaterQualitySystem import settings

from . import views

static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = [
    url(r"^$", views.index, name='Home Page'),
    url(r"^about-us/", views.AboutUs, name='About Us'),
    url(r"^wqcs/", views.WQCS, name='Water Quality Checking System'),
    url(r"^hkwts/", views.HKWTS, name='Helping Kids Walk to School'),
    url(r"^rums/", views.RUMS, name='Rain Water Usage Monitoring System'),
    url(r"^contacts/$", views.Contacts, name='Contacts'),

]
