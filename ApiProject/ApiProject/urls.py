from django.contrib import admin
from django.urls import path
from ApiApplication import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('sirket/', views.SirketApiView.as_view()),
    path('sirket/<int:sirket_id>/', views.SirketApiPutView.as_view()),
    path('kisi/', views.KisiApiView.as_view()),
    path('kisi/<int:kisi_id>/', views.KisiApiPutView.as_view()),
    path('cagri/', views.CagriApiView.as_view()),
    path('cagri/<int:cagri_id>/', views.CagriDeleteView.as_view())
]
