from django.conf.urls import url
from .views import *

dust_list = DustViewSet.as_view({"get" : "list", "post" : "create"})
switch_list = SchViewSet.as_view({"get" : "list", "post" : "create"})
urlpatterns = [
    url("^dusts/$", dust_list, name="dust-list"),
    url("^switch/$", switch_list, name="switch-list"),
]