Getting Started
=======================

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

Using the API
-------------

First make sure svgtex and the Flask server are running.

Then::

    curl -X POST 127.0.0.1:5000 -d mathml='<math xmlns="http://www.w3.org/1998/Math/MathML" display="block"><msup><mi>x</mi><mn>2</mn></msup><msup><mi>y</mi><mn>2</mn></msup></math>' -d image_format=gif -d max_size=500

Service returns::

    < HTTP/1.0 302 FOUND
    < Content-Type: application/json
    < Content-Length: 59
    < Location: http://127.0.0.1:5000/static/7c83babcdc8b4758bfc82e0b4729a310.gif
    {
      "url": "/static/5b7f34b736504aa89fb5e556de097871.gif"
    }

Which redirects to:

.. image::_static/Example2.gif

Required fields
^^^^^^^^^^^^^^^

============  =====================
Field         Expected value
============  =====================
mathml        Any valid MathML
image_format  GIF or PNG
max_size      Any size below 1000px
============  =====================

Possible Errors
^^^^^^^^^^^^^^^

======================  ======================================
Error (Status code)     Response
======================  ======================================
Missing Field (400)     {'error': 'Missing field: ...'}
Invalid MathML (400)    {'error': 'Invalid MathML ...'}
Conversion error (400)  {'error': 'Conversion error'}
======================  ======================================
