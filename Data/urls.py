from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^last24HoursTemperature/", views.Last24HoursTemperature, name='Last 24 Hours Temperature Data'),
    url(r"^lastYearTemperature/", views.LastYearTemperature, name='Last Year Temperature Data'),
    url(r"^lastYearConductivity/", views.LastYearConductivity, name='Last Year Conductivity Data'),
    url(r"^last24HourspH/", views.Last24HourspH, name='Last 24 Hours pH Data'),
    url(r"^lastYearpH/", views.LastYearpH, name='Last Year pH Data'),
    url(r"^last24HoursConductivity/", views.Last24HoursConductivity, name='Last 24 Hours Conductivity Data'),
]

