# -*- coding: utf-8 -*-
import datetime
import inspect
import traceback
from apps.logger.models import Log


class Logger(object):
    def __init__(self, instance):
        self.instance = instance

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            self.fatal(
                "{0}({1})".format(exc_type.__name__, exc_val),
                ''.join(traceback.format_exception(exc_type, exc_val, exc_tb)))

    def debug(self, *args, **kwargs):
        self.__push_back(0, *args, **kwargs)

    def info(self, *args, **kwargs):
        self.__push_back(100, *args, **kwargs)

    def success(self, *args, **kwargs):
        self.__push_back(200, *args, **kwargs)

    def warning(self, *args, **kwargs):
        self.__push_back(300, *args, **kwargs)

    def critical(self, *args, **kwargs):
        self.__push_back(400, *args, **kwargs)

    def fatal(self, *args, **kwargs):
        self.__push_back(500, *args, **kwargs)

    def __push_back(self, level, reason, message,
                    filename=None,
                    lineno=None):

        # TODO: think how to store logs from not save model as expected
        if self.instance.pk:
            Log.objects.create(
                c_obj=self.instance,
                level=level,
                reason="{}".format(reason),
                message="{0}".format(message),
                filename=filename,
                lineno=lineno
            )


def lineno(filename):
    return dict(lineno=inspect.currentframe().f_back.f_lineno, filename=filename)
