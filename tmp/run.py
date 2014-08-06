import os

from {{package}}.bootstrap import app
from {{package}} import logger


"""
Alias to be compatible w/ AWS or heroku (beanstalk)
"""
application = app

if __name__ == '__main__':
    try:
        port = int(os.environ.get('{{package}}_PORT', 8000))
        application.run(debug=True, host='0.0.0.0', port=port)
    except Exception:
        """
        don't ever catch SystemExit's here
        this could bug the reload in flasks webserver
        """
        logger.exception("caught in run.py")
        # RESTART
        raise SystemExit(3)
