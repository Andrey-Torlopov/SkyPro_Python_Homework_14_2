'''...'''
from flask import Flask
from flask import render_template

from app.api.views import api_blueprint


app = Flask(__name__)

# Register modules
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def not_found_404(error: Exception) -> str:
    '''Catch 404 error'''
    print(error)
    return render_template("404.html")


@app.errorhandler(500)
def not_found_500(error: Exception) -> str:
    '''Catch 500 error'''
    print(error)
    return render_template("500.html")


if __name__ == '__main__':
    app.debug = True
    app.run()
