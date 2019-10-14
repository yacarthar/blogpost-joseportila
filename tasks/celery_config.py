MONGO_URI = "mongodb://localhost:27017/"
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
            'filename': 'crawl.log',
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
            'filemode': 'w',
            'filename': 'crawl.log',
            'propagate': False
        },
        '__main__': {  # if __name__ == '__main__'
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': False
        },
    } 
}

class DefaultConfig:
    RESULT_BACKEND = 'database'
    RESULT_DBURI = 'sqlite:///temp.db'
    BROKER_URL = 'redis://localhost:6379/0'
    MONGO_URI = "mongodb://localhost:27017/"
    LOGGING_CONFIG.update({})


class DevelopmentConfig(DefaultConfig):
    pass


class ProductionConfig(DefaultConfig):
    pass

