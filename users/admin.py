from django.contrib import admin

from carts.admin import CartTabAdmin
from orders.admin import OrderTabulareAdmin
from users.models import User


# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email', 'first_name', 'last_name']

    inlines=[CartTabAdmin,OrderTabulareAdmin]