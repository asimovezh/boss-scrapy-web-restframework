from django.urls import path

from . import views
from django.conf.urls import url, include

from . import views



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

]





