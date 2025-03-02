from django.contrib import admin 
from .models import task
admin.site.register(task)


# Register your models here.
# models= apps.get_models()
# for model in models:
#     try:
#         admin.site.register(model)
#     except admin.sites.AlreadyRegistered:
#         pass