from django.urls import path,include
from testapp.api.views import HydCRUD
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('hydjobs',HydCRUD)

urlpatterns = [
    path('',include(router.urls))
]