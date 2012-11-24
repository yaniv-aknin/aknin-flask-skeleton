from functools import partial

from flask.ext.assets import Environment, Bundle

from app import app

CoffeeBundle = partial(Bundle, filters='coffeescript', debug=False)
SCSSBundle = partial(Bundle, filters='pyscss', debug=False)
JSBundle = partial(Bundle, filters='yui_js')
CSSBundle = partial(Bundle, filters='yui_css')

assets = Environment(app)
assets.url = '/static/'

base_coffee = CoffeeBundle('js/lib/lib.coffee', output="gen/base.coffee.js")
base_js = JSBundle(base_coffee, output='gen/base.js')
assets.register('base.js', base_js)

base_scss = SCSSBundle('css/base.scss', output="gen/base_scss.css")
base_css = CSSBundle(base_scss, output='gen/base.css')
assets.register('base.css', base_css)
