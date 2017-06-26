# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from apps.logger.models import Log


@admin.register(Log)
class AdminLog(admin.ModelAdmin):
    exclude = ['message', 'filename', 'lineno', 'c_type', 'o_id', 'c_obj']
    readonly_fields = ['level',
                       'reason',
                       'get_message',
                       'call_point',
                       'created_at',
                       'get_obj'
                       ]
    list_display = ['level', 'reason', 'get_obj']

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_message(self, obj):
        return "<pre>%s</pre>" % obj.message
    get_message.allow_tags = True
    get_message.short_description = "Message"

    def call_point(self, obj):
        result = ''
        if obj.filename:
            result += obj.filename
            if obj.lineno:
                result += " [%d]" % obj.lineno
        return result
    call_point.short_description = "Point of call"

    def get_obj(self, obj):
        return "{}(id={}) [{}]".format(
            obj.c_obj.__class__.__name__,
            obj.c_obj.id,
            obj.c_obj)
    get_obj.short_description = "Object"

