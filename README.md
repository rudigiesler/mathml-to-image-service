# mathml-to-image-service

## Installing and running svgtex (requires phantomjs)
```shell
sudo apt-get install phantomjs
git clone https://github.com/agrbin/svgtex.git
cd svgtex
phantomjs main.js
```

## Installing prerequisites
```shell
sudo apt-get install librsvg2-bin
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
