from django.urls import path
from .views import home , terms,privacy,disc,cancel,shipping,contact,facebook,instagram,twitter,linkedin,priyanshu,kunal,riya,anuska,success,text
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from Printf.views import about, snippet_detail

from Printf.sitemaps import StaticViewSitemap
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from Printf.sitemaps import SnippetSitemap, StaticViewSitemap
sitemaps = {'static': StaticViewSitemap, 'snippet': SnippetSitemap}


urlpatterns = [
    path('',home,name='home' ),
    path('privacy_policy/',terms,name='privacy' ),
    path('terms_and_conditon/',privacy ,name='terms'),
    path('disclaimer',disc,name='disc' ),
    path('cancellation_and_refund_policy',cancel,name='refund' ),
    path('shipping_and_delivery_policy', shipping,name='shipping' ),
    path('contact', contact,name='contact' ),
    path('facebook', facebook ,name='f' ),
    path('instagram', instagram ,name='i' ),
    path('twitter', twitter ,name='t' ),
    path('linkedin', linkedin ,name='l' ),
    path('riya', riya , name="r" ),
    path('anuska', anuska , name="a" ),
    path('kunal', kunal , name="k" ),
    path('priyanshu', priyanshu , name="p" ),
    path('success/',success,name="success"),
    path('texts/',text,name="texts"),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('<slug:slug>/', snippet_detail),
    



]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
