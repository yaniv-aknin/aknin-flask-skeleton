from os import path
from flask import Flask, send_from_directory

app = None

def initialize_app(settings):
    global app
    app = Flask(__name__)
    app.config.from_object(settings)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(path.join(app.static_folder, 'static', 'img'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    # import registries; the "import x ; x" idiom silences lint warnings for unused imports
    import models ; models
    import assets ; assets
    import views ; views
    # HACK: see https://github.com/twilio/flask-restful/issues/8
    #       and https://github.com/twilio/flask-restful/pull/9
    saved_handlers = app.handle_exception, app.handle_user_exception
    import api ; api
    app.handle_exception, app.handle_user_exception = saved_handlers


    return app
