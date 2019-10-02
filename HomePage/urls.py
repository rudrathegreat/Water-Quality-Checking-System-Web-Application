from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from WaterQualitySystem import settings
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns = [
    url(r"^$", views.index, name='Home Page'),
    url(r"^about-us/", views.AboutUs, name='About Us'),
    url(r"^wqcs/", views.WQCS, name='Water Quality Checking System'),
    url(r"^hkwts/", views.HKWTS, name='Robot Walking School Bus'),
    url(r"^rums/", views.RUMS, name='Rain Water Usage Monitoring System'),
    url(r"^contacts/$", views.Contacts, name='Contacts'),
    url(r"^posts/$", views.posts, name="Posts"),
    url(r"^md/$", views.showMonitoringDataPage, name="Monitoring Data"),
    url(r"^tkp/$", views.tkp, name="The Kangaroo Project"),
]
