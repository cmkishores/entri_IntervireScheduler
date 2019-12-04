from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
	model = CustomUser
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	list_display = ['email','username', 'user_type',]
	fieldsets = UserAdmin.fieldsets + ( (None, {'fields': ('user_type',)}), )
	# fieldsets = (

	# 	(None,{'fields':('email','password','username','age',)}),
	# 	('Permissions',{'fields':('is_staff','is_active')}),
	# 	)

	add_fieldsets = (

		(None,{
			'classes':('wide',),
			'fields':('email','username','password1','password2','is_staff','is_active')
			}),

		)
admin.site.register(CustomUser,CustomUserAdmin)

# Register your models here.
