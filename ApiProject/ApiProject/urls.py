from django.contrib import admin
from django.urls import path
from ApiApplication import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls), #username: admin | password: 123 
    path('sirket/', views.SirketApiView.as_view()),
    path('sirket/<int:sirket_id>/', views.SirketApiDetailView.as_view()),
    path('kisi/', views.KisiApiView.as_view()),
    path('kisi/<int:kisi_id>/', views.KisiApiDetailView.as_view()),
    path('kisi/<int:kisi_id>/cagrilar', views.KisiCagriView.as_view()),
    path('cagri/', views.CagriApiView.as_view()),
    path('cagri/<int:cagri_id>/', views.CagriUpdateView.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
