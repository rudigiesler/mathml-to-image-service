import os
import subprocess
import uuid

from config import STATIC_DIR


class ImageConvertError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "Image processing error: %s" % self.error


def to_image(svg_string, image_format, max_size):
    if max_size > 1000:
        raise NameError("max_size is too big. Max of 1000px.")

    tmp_file_name = STATIC_DIR % '%s.svg' % uuid.uuid4().hex

    svg_file = open(tmp_file_name, 'w', encoding='utf-8')
    svg_file.write(svg_string)
    svg_file.close()

    if image_format.upper() == 'PNG':
        extension = '.png'
    elif image_format.upper() == 'GIF':
        extension = '.gif'
    else:
        os.remove(tmp_file_name)
        raise NameError(
            'Unsupported output file format - "GIF" and "PNG" only.')

    png_filename = "%s.png" % (uuid.uuid4().hex)
    filename = "%s%s" % (uuid.uuid4().hex, extension)

    try:
        subprocess.check_call(
            ['rsvg-convert', tmp_file_name, '-w', '%s' % (max_size,),
             '--background-color', 'white', '-o', STATIC_DIR % png_filename],
            stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        os.remove(tmp_file_name)
        os.remove(STATIC_DIR % png_filename)
        raise ImageConvertError('Invalid SVG')

    if image_format.upper() == 'GIF':
        try:
            subprocess.check_call(
                ['convert', STATIC_DIR % png_filename, STATIC_DIR % filename],
                stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            os.remove(tmp_file_name)
            os.remove(STATIC_DIR % png_filename)
            raise ImageConvertError('Invalid PNG')

        os.remove(tmp_file_name)
        os.remove(STATIC_DIR % png_filename)
        return filename

    else:
        os.remove(tmp_file_name)
        return png_filename

    #TODO: Implement optional file size optimisation.
    #convert foo1.png -colors 2 foo2.png; (reduce color depth)
    #pngcrush -bit_depth 1 foo2.png final.png (implement optimal png)


def main():
    svg_string = open('example.svg', 'r', encoding='utf-8').read()
    print (to_image(svg_string, 'PNG', 300))


if __name__ == '__main__':
    main()
