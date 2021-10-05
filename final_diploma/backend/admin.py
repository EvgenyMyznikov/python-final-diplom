import csv
import datetime
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import Order, OrderItem, User, Contact


def export_to_csv(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    filename = f'{opts.verbose_name}.csv'
    f = open(filename, 'w')
    writer = csv.writer(f)
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    for obj in queryset:
        data_row = []
        for field in fields:
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            data_row.append(value)
        writer.writerow(data_row)
export_to_csv.short_description = 'Export to CSV'


class CustomUserAdmin(UserAdmin):
    """
    Users control panel
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'user_type')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'company', 'position')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'city', 'street', 'house', 'structure', 'building', 'apartment', 'user', 'phone')
    llist_display_links = ('user',)
    list_filter = ('user', 'city',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Contact, ContactAdmin)


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['order']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date', 'state', 'contact']
    list_filter = ['user', 'date']
    inlines = [OrderItemInline]
    actions = [export_to_csv]







