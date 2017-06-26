# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

LOG_LEVELS = [
    (0, "Debug"),
    (100, "Info"),
    (200, "Success"),
    (300, "Warning"),
    (400, "Critical"),
    (500, "Fatal"),
]


class Log(models.Model):
    c_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    o_id = models.PositiveIntegerField()
    c_obj = GenericForeignKey('c_type', 'o_id')
    created_at = models.DateTimeField(auto_now_add=True)

    level = models.IntegerField(choices=LOG_LEVELS, null=True)
    reason = models.CharField(max_length=128, null=True)
    message = models.TextField(null=True)

    filename = models.CharField(max_length=256, null=True)
    lineno = models.PositiveIntegerField(null=True)

    def __str__(self):
        return "{0.__class__.__name__}".format(self.c_type)

    def css_level(self):
        if self.level == 100:
            return 'info'
        if self.level == 200:
            return 'success'
        if self.level == 300:
            return 'warning'
        if self.level in [400, 500]:
            return 'error'
        return ''  # debug

    def short(self):
        return self.message[:300] + ("..." if len(self.message) > 300 else '')

    def is_long(self):
        return len(self.message) > 300

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"
