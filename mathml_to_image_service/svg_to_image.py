import os
import subprocess
import uuid


def to_image(svg_string, image_format, max_size):
    if max_size > 1000:
        raise NameError("max_size is too big. Max of 1000px.")

    tmp_file_name = '%s.svg' % uuid.uuid4().hex

    svg_file = open(tmp_file_name, 'w', encoding='utf-8')
    svg_file.write(svg_string)
    svg_file.close()

    if image_format.upper() == 'PNG':
        extention = '.png'
    elif image_format.upper() == 'GIF':
        extention = '.gif'
    else:
        raise NameError(
            'Unsupported output file format - "GIF" and "PNG" only.')

    filename = "%s%s" % (uuid.uuid4().hex, extention)
    subprocess.check_call(
        ['convert', tmp_file_name, '-resize',
         '%sx%s' % (max_size, max_size), filename], stderr=subprocess.DEVNULL)
    os.remove(tmp_file_name)

    return filename


def main():
    svg_string = open('example.svg', 'r', encoding='utf-8').read()
    print (to_image(svg_string, 'GIF', 300))


if __name__ == '__main__':
    main()
