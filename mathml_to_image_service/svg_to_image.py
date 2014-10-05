import os
import subprocess
import uuid

from config import STATIC_DIR


class ImageConvertError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return "Image processing error: %s" % self.error


def reduce_quality(path, quality):
    """
    Takes in a PNG or GIF and reduces the file size at the cost of image
    quality. If quality is 3, the image is not touched. If the quality is 2,
    the image quality is slightly reduced, if the quality is 1, the image
    quality is greatly reduces.

    :param string path:
        The path of the image file.
    :param int quality:
        The desired quality setting.
    """

    def pngcrush(source, destination):
        """
        Runs pngcrush on source, and stores in destination. Removes source.
        If the conversion fails, raises exception, and moves source to
        destination.
        """
        try:
            subprocess.check_call(
                ['pngcrush -bit_depth 1', source, destination],
                stderr=subprocess.DEVNULL)
            os.remove(source)
            return destination
        except subprocess.CalledProcessError as e:
            os.remove(destination)
            os.rename(source, destination)
            raise ImageConvertError('Cannot pngcrush the image')

    def reduce_colour_depth(source, destination):
        """
        Reduces colour depth on source, and stores in destination. Removes
        source. If the conversion fails, raises exception, and moves source to
        destination.
        """
        try:
            subprocess.check_call(
                ['convert', source, '-colors 2', destination],
                stderr=subprocess.DEVNULL)
            os.remove(source)
            return destination
        except subprocess.CalledProcessError as e:
            os.remove(destination)
            os.rename(source, destination)
            raise ImageConvertError('Cannot reduce colour depth with convert')

    if quality > 3 or quality < 1:
        raise NameError('Unsupported quality. Only values [1, 3] allowed.')
    if quality == 3:
        return filename

    tmp_filename = '%s.tmp' % filename
    _, extension = os.path.splitext(filename)
    os.rename(filename, tmp_filename)
    if quality == 2:
        pngcrush(tmp_filename, filename)
        return filename
    if quality == 3:
        reduce_colour_depth(tmp_filename, filename)
        if extension.upper() == 'PNG':
            os.rename(filename, tmp_filename)
            pngcrush(tmp_filename, filename)
            return filename
        else:
            return filename


def to_image(svg_string, image_format, max_size, quality=3):
    """
    Takes an svg string and converts it to GIF or PNG with various parameters.
    Stores the image on disk and returns the filename.

    :param string svg_string:
        The string that represents the SVG to convert
    :param string image_format:
        The format of the resulting image. One of ``GIF`` or ``PNG``.
    :param int max_size:
        The maximum size of the image in pixels. Must be between [1, 1000].
    :param int quality:
        The amount of effort put towards reducing the size of the resulting
        image. 3 is the maximum and 1 is the minimum. Note that 1 and 2 might
        break compatibility on some devices.
    """

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
            os.remove(STATIC_DIR % filename)
            raise ImageConvertError('Invalid PNG')

        os.remove(tmp_file_name)
        os.remove(STATIC_DIR % png_filename)
        reduce_quality(filename, quality)
        return filename
    else:
        os.remove(tmp_file_name)
        reduce_quality(png_filename, quality)
        return png_filename


def main():
    svg_string = open('example.svg', 'r', encoding='utf-8').read()
    print (to_image(svg_string, 'PNG', 300))


if __name__ == '__main__':
    main()
