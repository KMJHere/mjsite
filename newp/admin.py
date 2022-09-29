from django.contrib import admin

from newp.models import board, member, like

# Register your models here.
admin.site.register(member);
admin.site.register(board);
admin.site.register(like); 