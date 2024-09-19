import logging
from logging.handlers import RotatingFileHandler
from flask import Flask, render_template, make_response, jsonify
from quotes import get_quote

app = Flask(__name__)

def setup_logging():
    handler = RotatingFileHandler('app.log', maxBytes=1000000, backupCount=5)
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    )
    handler.setFormatter(formatter)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Logging setup complete.')

setup_logging()

@app.route("/")
def index():
    try:
        return render_template('index.html')
    except Exception as e:
        app.logger.error("Error rendering index page", exc_info=True)
        return make_response("Internal Server Error", 500)

@app.route("/quote")
def quote():
    try:
        quote = get_quote()
        return make_response(jsonify(quote), 200)
    except Exception as e:
        app.logger.error("Error fetching quote", exc_info=True)
        return make_response(jsonify({"error": "Failed to retrieve quote"}), 500)

# Custom error handlers
@app.errorhandler(404)
def not_found_error(error):
    app.logger.warning(f"404 error: {error}")
    return make_response(render_template('404.html'), 404)

@app.errorhandler(500)
def internal_error(error):
    app.logger.error(f"500 error: {error}", exc_info=True)
    return make_response(render_template('500.html'), 500)

if __name__ == "__main__":
    app.run()
