import logging as __logging
import logging.config

from {{package}} import __version__, config

__logging.basicConfig(
    level=__logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s'
)
logger = __logging.getLogger(__name__)
logger.info("intializing version %s", __version__)


# !! shortcuts !!


"""
Logger.info(msg, *args, **kwargs)
Logs a message with level INFO on this logger. The arguments are interpreted as for debug().
"""
info = logger.info

"""
Logger.warning(msg, *args, **kwargs)
Logs a message with level WARNING on this logger. The arguments are interpreted as for debug().
"""
warning = logger.warning

"""
Logger.error(msg, *args, **kwargs)
Logs a message with level ERROR on this logger. The arguments are interpreted as for debug().
"""
error = logger.error

"""
Logger.critical(msg, *args, **kwargs)
Logs a message with level CRITICAL on this logger. The arguments are interpreted as for debug().
"""
critical = logger.critical

"""
Logger.log(lvl, msg, *args, **kwargs)
Logs a message with integer level lvl on this logger. The other arguments are interpreted as for debug().
"""
log = logger.log

"""
Logger.exception(msg, *args, **kwargs)
Logs a message with level ERROR on this logger. The arguments are interpreted as for debug(). Exception info is added to the logging message. This method should only be called from an exception handler.
"""
exception = logger.exception
