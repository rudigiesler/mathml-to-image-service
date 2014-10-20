[![Build Status](https://travis-ci.org/rudigiesler/mathml-to-image-service.svg?branch=master)](https://travis-ci.org/rudigiesler/mathml-to-image-service)
[![Documentation Status](https://readthedocs.org/projects/mathml-to-image-service/badge/?version=latest)](https://readthedocs.org/projects/mathml-to-image-service/?badge=latest)

# mathml-to-image-service

## Requirements
 - ``python == 3.4``

## Installing prerequisites
```shell
sudo apt-get install librsvg2-bin phantomjs
```

## Installing and running svgtex
```shell
git clone https://github.com/agrbin/svgtex.git
cd svgtex
phantomjs main.js
```

## Usage:
```shell
pip install -r requirements.txt
python mathml_to_image_service/service.py
```

## Running tests:
```shell
python -m unittest discover mathml_to_image_service
```
