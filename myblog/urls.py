# /api/work: GET, POST
# /api/work/:id: GET, PUT
# /api/work/active: GET
from django.conf.urls import url
from .views import work_list, work_detail, work_active

urlpatterns = [
    url(r'^api/work$', work_list),
    url(r'^api/work/(?P<id>[0-9]+)$', work_detail),
    url(r'^api/work/active$', work_active)
]