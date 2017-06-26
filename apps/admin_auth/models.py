# -*- coding: utf-8 -*-
import random
from django.contrib.auth.models import AbstractUser
from django.core import serializers
from django.db.models.signals import pre_save
from django.dispatch import receiver
from apps.logger.utils import Logger, lineno


class User(AbstractUser):
    pass


@receiver(pre_save, sender=User)
def test(instance, *args, **kwargs):
    if instance.pk:
        with Logger(instance) as log:
            fmt = random.choice(['xml', 'json'])
            data = serializers.serialize(fmt, [instance], indent=2)
            log.debug("signal pre_save called for User(pk={})".format(instance.pk),
                      "{}".format(data),
                      **lineno(__file__))
