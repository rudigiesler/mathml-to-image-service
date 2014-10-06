from flask import Flask, jsonify, make_response, request, url_for

from mathoid_client import get_svg, SVGEncodeError
from svg_to_image import to_image


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        return jsonify(
            error="Try a post with fields: 'mathml', 'max_size', and "
                  "'image_format'")
    try:
        mathml = request.form['mathml']
        format = request.form['image_format']
        max_size = request.form['max_size']
    except KeyError as error:
        return jsonify(error='Missing field: %s' % error.args[0]), 400

    try:
        svg_string = get_svg(mathml)
    except SVGEncodeError as e:
        return jsonify(error=e.args[0]), 400

    try:
        file_name = to_image(svg_string, format, int(max_size))
    except NameError as error:
        return jsonify(error=error.args[0]), 400

    url = url_for('static', filename=file_name)
    data = jsonify(url=url)

    return make_response((data, 302, {'Location': url}))


if __name__ == '__main__':
    app.run()
