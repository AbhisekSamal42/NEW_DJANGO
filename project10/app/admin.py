from django.contrib import admin

# Register your models here.
from app.models import*
admin.site.register(DEPT)
admin.site.register(EMP)
admin.site.register(BONUS)
admin.site.register(SALGRADE)