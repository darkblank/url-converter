from flask import Flask, jsonify, request, render_template
from flask_wtf import CSRFProtect

from app.apis import api
from app.views import view

csrf = CSRFProtect()


def create_app(config_object):
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    app.config.from_object(config_object)
    app.register_blueprint(view)
    app.register_blueprint(api, url_prefix='/api')
    csrf.init_app(app)

    @app.route('/ping')
    def health_check():
        return jsonify(dict(ok='ok'))

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    @app.teardown_request
    def teardown_sessions(exception):
        ctx = request._get_current_object()
        if hasattr(ctx, '_current_session'):
            if exception:
                ctx._current_session.rollback()
            ctx._current_session.close()

    return app
