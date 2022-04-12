"""new_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from blog_app import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.test, name='test'),
    
# ]

from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from blog_app.sitemaps import PostSitemap
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    # path('grappelli/', include('grappelli.urls')), # grappelli URLS
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')), # Django JET dashboard URLS
    path('admin/', admin.site.urls),
    path('', include('blog_app.urls', namespace='blog')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    
 ] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Modifies default django admin titles and headers with custom app detail.
admin.site.site_header = "Lydia Admin"
admin.site.site_title = "Lydia Admin Portal"
admin.site.index_title = "Welcome to Lydia Blog Portal"
