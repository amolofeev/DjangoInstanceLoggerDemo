# -*- coding: utf-8 -*-
import random
from django.contrib.auth.models import AbstractUser
from django.core import serializers
from django.db.models.signals import pre_save
from django.dispatch import receiver
from dj_logger.utils import Logger, lineno


class User(AbstractUser):
    pass


@receiver(pre_save, sender=User)
def test_log(instance, *args, **kwargs):
    if instance.pk:
        with Logger(instance) as log:
            fmt = random.choice(['xml', 'json'])
            data = serializers.serialize(fmt, [instance], fields=('id', 'username',), indent=2)

            log.debug(
                "Debug message",
                "{}".format(data), **lineno(__file__)
            )

            log.info(
                "Info message",
                "{}".format(data), **lineno(__file__)
            )

            log.success(
                "Success message",
                "{}".format(data), **lineno(__file__)
            )

            log.warning(
                "Warning message",
                "{}".format(data), **lineno(__file__)
            )

            log.critical(
                "Critical message",
                "{}".format(data), **lineno(__file__)
            )

            log.fatal(
                "Fatal message",
                "{}".format(data), **lineno(__file__)
            )


@receiver(pre_save, sender=User)
def test_exception(instance, *args, **kwargs):
    if instance.pk:
        try:
            with Logger(instance):
                assert 1 == 2, "Oooops! I'm an test exception"
        except AssertionError:
            "just skip it for test"
