from django.conf.urls import url
from .views import DustViewSet

dust_list = DustViewSet.as_view({"get" : "list", "post" : "create"})

urlpatterns = [
    url("^dusts/$", dust_list, name="dust-list"),
]