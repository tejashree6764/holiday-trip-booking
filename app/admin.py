from django.contrib import admin
from .models import Contact,Post
from .models import Register
# Register your models here.
admin.site.register(Contact)
admin.site.register(Register)
admin.site.register(Post)

