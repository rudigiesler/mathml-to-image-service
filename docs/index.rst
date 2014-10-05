MathML to Image Service
=======================

HTTP Rest API for converting MathML to various image formats.

Converting MathML::

    <math xmlns="http://www.w3.org/1998/Math/MathML"><mrow><msup><mi>e</mi><mrow><mi>i</mi><mi>x</mi></mrow></msup><mo>=</mo><mi>cos</mi><mi>x</mi><mo>+</mo><mi>i</mi><mi>sin</mi><mi>x</mi></mrow></math>

Into images:

.. math::
    :nowrap:

    \begin{equation}
        e^{ix} = \cos x + i\sin x
    \end{equation}

Requirements
------------

Installing prerequisites::

    sudo apt-get install librsvg2-bin phantomjs

Installing and running svgtex::

    git clone https://github.com/agrbin/svgtex.git
    cd svgtex
    phantomjs main.js

Python requirments::

    pip install -r requirements.txt

Usage
-----

Running server::

    python mathml_to_image_service/service.py

Running tests::

    python -m unittest discover mathml_to_image_service

Contribute
----------

- Issue Tracker: https://github.com/rudigiesler/mathml-to-image-service/issues
- Source Code: https://github.com/rudigiesler/mathml-to-image-service

Support
-------

If you are having issues, please log them on Github.

License
-------

The project is licensed under the MIT license.
