from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.home, name='home'),
    url(r'^search/', views.search_results, name='search_results'),
    # url(r'^image/', views.image, name='image')
    url(r'^image/(\d+)', views.image, name='image')
]


# configure our urls.py to register the MEDIA_ROOT route.
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
