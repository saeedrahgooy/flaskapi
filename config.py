class Config:
    DEBUG = True
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/courses'
    MONGODB_SETTINGS = {
        'db': 'courses',
        'username': '',
        'password': '',
        'host': 'mongodb://localhost/courses',
        'port': 27017
    }
