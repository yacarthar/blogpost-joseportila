class DefaultConfig:
    DEBUG = True
    JSONIFY_PRETTYPRINT_REGULAR = True
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
            },
        },
        'handlers': {
            'default': {
                'level': 'INFO',
                'formatter': 'standard',
                'class': 'logging.FileHandler',
                'filename': 'flask.log',
                'mode': 'w'
            },
        },
        'loggers': {
            '': {  # root logger
                'handlers': ['default'],
                'level': 'INFO',
                'filemode': 'w',
                'filename': 'crawl.log',
                'propagate': False
            },
            'crawl': {
                'handlers': ['default'],
                'level': 'INFO',
                'propagate': False
            },
            '__main__': {  # if __name__ == '__main__'
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': False
            },
        }
    }


class DevelopmentConfig(DefaultConfig):
    pass
    # LOGGING_CONFIG.update(
    #     {
    #
    #     }
    #
    # )


class ProductionConfig(DefaultConfig):
    DEBUG = False
