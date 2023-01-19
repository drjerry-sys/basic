"""
Definition of urls for Purrfect_Match.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import appforms, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('add/', views.profileForm, name='profileForm'),
    path('search/results/', views.SearchPage, name='search'),
    path('edit/add/', views.editAdd, name='modify'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=appforms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)