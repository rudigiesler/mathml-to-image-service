from flask import Flask, jsonify, request, url_for

from mathoid_client import get_svg
import svg_to_image


app = Flask(__name__)


def safe_get_field(field):
    if field in request.form:
        return request.form[field]
    raise KeyError(field)


@app.route('/', methods=['GET', 'POST'])
def convert():
    if request.method == 'GET':
        return jsonify(error='Try sending MathML in a POST request. :)')
    try:
        mathml = safe_get_field('mathml')
        format = safe_get_field('image_format')
        max_size = safe_get_field('max_size')
    except KeyError as error:
        return jsonify(error='Missing field: %s' % error, status=400)

    svg_string = get_svg(mathml)

    print('svg strung')

    file_name = svg_to_image.to_image(svg_string, format, int(max_size))

    return jsonify(url=url_for('static', filename=file_name))


if __name__ == '__main__':
    app.run()
