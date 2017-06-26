# -*- coding: utf-8 -*-
from django.core.management import BaseCommand
from django.db.models import Max
from apps.admin_auth.models import User
from apps.logger.models import Log
from apps.logger.utils import Logger, lineno


class Command(BaseCommand):
    def handle(self, *args, **options):
        Log.objects.all().delete()
        instance = User.objects.first()
        with Logger(instance) as log:
            log.debug("Debug log", "Example", **lineno(__file__))
            log.info("info log", "Example", **lineno(__file__))
            log.success("Success log", "Example", **lineno(__file__))
            log.warning("Warning log", "Example", **lineno(__file__))
            log.critical("Critical log", "Example", **lineno(__file__))
            log.fatal("Fatal log", "Example", **lineno(__file__))
            log.debug("Exmple log log", open(__file__).read())

        # hack to be able to write logs from pre_save signal on model creation.
        user_id = User.objects.aggregate(max_id=Max('id')+1)['max_id']

        username = 'user%d'%user_id
        User.objects.create(pk=user_id, username=username)

        with Logger(instance) as log:
            raise Exception("test exception")
