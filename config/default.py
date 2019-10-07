import logging

# logging config
logging.basicConfig(level=logging.DEBUG,
                    filemode='w',
                    filename='test/crawl.log'
                    )
# Flask config
DEBUG = True
JSONIFY_PRETTYPRINT_REGULAR = True

# celery config
# Broker settings.
broker_url = 'redis://localhost:6379/0'

# List of modules to import when the Celery worker starts.
# imports = ('myapp.tasks',)

# Using the database to store task state and results.
# result_backend = 'db+sqlite:///results.db'

# task_annotations = {'task.handle_topic': {'rate_limit': '10/s'},
#                     'task.handle_post': {'rate_limit': '10/s'}
#                     }

