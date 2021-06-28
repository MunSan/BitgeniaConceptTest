from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'), #Uso una vista genérica de django para el home.
    path('accounts/', include('django.contrib.auth.urls')), #Views de autenticacion provistas por django mismo. /login /pass_change, etc.
    path('admin/', admin.site.urls),
    path('genes/', views.RetrieveGeneListView),
    path('genes/<int:_id>/', views.RetrieveGeneDetailView),
    path('genes/create_gene', views.CreateGeneView),
    path('genes/<int:_id>/update_gene', views.UpdateGeneView),
    path('genes/<int:_id>/delete_gene', views.DeleteGeneView),
    path('diseases/', views.RetrieveDiseaseListView),
    path('diseases/<int:_id>/', views.RetrieveDiseaseDetailView),
    path('diseases/create_disease', views.CreateDiseaseView),
    path('diseases/<int:_id>/update_disease', views.UpdateDiseaseView),
    path('diseases/<int:_id>/delete_disease', views.DeleteDiseaseView),
    path('variants/', views.RetrieveVariantListView),
    path('variants/<int:_id>/', views.RetrieveVariantDetailView),
    path('variants/create_variant', views.CreateVariantView),
    path('variants/<int:_id>/update_variant', views.UpdateVariantView),
    path('variants/<int:_id>/delete_variant', views.DeleteVariantView),
    path('query/', views.QueryView),
]
