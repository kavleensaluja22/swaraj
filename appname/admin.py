from django.contrib import admin

# Register your models here.



from appname.models import Feedback
from appname.models import GalleryImage
# from appname.models import Enquiry
from appname.models import OTP

admin.site.register(Feedback)
admin.site.register(GalleryImage)
# admin.site.register(Enquiry)
admin.site.register(OTP)

