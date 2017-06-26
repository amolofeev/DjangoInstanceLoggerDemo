**DjangoInstanceLogger**
=====================

Simple django app for store logs for any model instance over GenericForeignKey with example.

UI require django-suit package.


**Usage:**

```
from apps.logger.utils import Logger, lineno

with Logger(instance) as log:
    log.debug('reason', 'message', filename=None, lineno=None)
    log.info('reason', 'message', filename=None, lineno=None)
    log.success('reason', 'message', filename=None, lineno=None)
    log.warning('reason', 'message', filename=None, lineno=None)
    log.critical('reason', 'message', filename=None, lineno=None)
    log.fatal('reason', 'message', filename=None, lineno=None)
    raise Exception("Some error")
```

For adding filename and line number into log you can use helper function `lineno`
```
log.debug('reason', 'message', **lineno(__file__))
```

**Note**

To be able to store log `instance.id` or `instance.pk` are required.
`apps/logger/management/commands/test_log.py` contains some examples for that.
