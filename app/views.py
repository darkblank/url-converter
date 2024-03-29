import datetime

from flask import Blueprint, redirect, render_template

from app.database import session
from app.models import Url

view = Blueprint('view', __name__)


@view.route('/')
def index():
    return render_template('index.html')


@view.route('/view/urls')
def url_list():
    return render_template('url_list.html')


@view.route('/<string:short_url>')
def redirect_to_original_url(short_url):
    obj = session.query(Url).filter(Url.short_url == short_url).first()
    if not obj:
        return render_template('404.html'), 404

    obj.update_hit_count_and_last_used_at()
    return redirect(obj.original_url)
