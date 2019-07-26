from django.conf import settings
#from django.conf.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import include, path

# urlpatterns = [
#     path(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
#     path(r'^photos/', include('mysite.photos.urls', namespace='photos')),
# ]


urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('photos/', include('mysite.photos.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
