from django.contrib import admin
from django.urls import path
from appname import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls, ),
    path('location',views.location,name="location"),
    path('feedback',views.feedback,name="feedback"),
    path('',views.home,name="home"),
    path('gallery',views.gallery,name="gallery"),
    path('s717',views.s717,name="s717"),
    path('take_number',views.take_number,name="take_number"),
    path('verify_otp',views.verify_otp,name="verify_otp"),
    path('g_try',views.g_try,name="g_try"),
    path('s724',views.s724,name="s724"),
    path('s733',views.s733,name="s733"),
    path('s735',views.s735,name="s735"),
    path('s744',views.s744,name="s744"),
    path('s855',views.s855,name="s855"),
    path('s969',views.s969,name="s969"),     
    path('s963',views.s963,name="s963"),
    # path('check_verified',views.check_verified,name="check_verified"),
    path('combine1',views.combine1,name="combine1"),
    path('combine2',views.combine2,name="combine2"),
    path('combine3',views.combine3,name="combine3"),
    path('index',views.index,name="index"),
    # path('genrate_otp',views.generate_otp,name="genrate_otp"),
    path('generate_otp',views.generate_otp,name="generate_otp"),
    path('xt',views.xt,name="xt"),
    path('send_otp_to_phone_number/<phone_number>/' , views.send_otp_to_phone_number , name="send_otp_to_phone_number")
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)