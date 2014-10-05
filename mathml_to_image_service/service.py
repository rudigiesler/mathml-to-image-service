from flask import Flask, jsonify, request, url_for

from mathoid_client import get_svg
import svg_to_image


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        return jsonify(error='Try sending MathML in a POST request. :)')
    try:
        mathml = request.form['mathml']
        format = request.form['image_format']
        max_size = request.form['max_size']
    except KeyError as error:
        return jsonify(error='Missing field: %s' % error.args[0]), 400

    svg_string = get_svg(mathml)

    file_name = svg_to_image.to_image(svg_string, format, int(max_size))

    return jsonify(url=url_for('static', filename=file_name))


if __name__ == '__main__':
    app.run()
