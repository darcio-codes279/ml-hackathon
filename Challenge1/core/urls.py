from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index_view, name="index"),
    path('submit/',views.submitForm, name="submit"),
    path('form/',views.getForm, name="form"),
    path('selectReport/',views.reportView, name="selectReport"),
    path('report/',views.getReport, name="report"),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)