# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from apps.admin_auth.models import User
from apps.logger.models import Log


@admin.register(User)
class AdminUser(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'username',
                'email',
                'first_name',
                'last_name',
                'is_active',
                'groups',
                'user_permissions',
                'is_staff',
                'is_superuser',
            ]
        }),
        ('Logs', {
            'classes': ('suit-tab', 'suit-tab-logs',),
            'fields': []}),
    ]

    suit_form_tabs = (('general', 'General'),
                      ('logs', 'Logs'))
    suit_form_includes = (
        ('admin/logger/tab_logs.html', '', 'logs'),
    )

    filter_horizontal = ['user_permissions']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.user.is_superuser:
            extra_context = extra_context or {}
            obj = self.get_object(request, object_id)
            c_type = ContentType.objects.get_for_model(obj)
            extra_context['logs'] = Log.objects.filter(c_type=c_type,
                                                       o_id=object_id)
        return super().change_view(request, object_id, form_url, extra_context)
