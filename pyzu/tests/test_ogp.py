import pytest
from pyzu import OGP

ogp_data = """
<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns#">
    <meta property="og:title" content="Open Graph protocol">
    <meta property="og:type" content="website">
    <meta property="og:url" content="http://ogp.me/">
    <meta property="og:image" content="http://ogp.me/logo.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="300">
    <meta property="og:image:height" content="300">
    <meta property="og:image:alt" content="The Open Graph logo">
    <meta property="og:description" content="The Open Graph protocol enables any web page to become a rich object in a social graph."> # noqa
  </head>
  <body>
  </body>
</html>
"""
ogp_results = {
    'title': "Open Graph protocol",
    'type': "website",
    'url': "http://ogp.me/",
    'image': "http://ogp.me/logo.png",
    'image:type': "image/png",
    'image:width': '300',
    'image:height': '300',
    'image:alt': "The Open Graph logo",
    'description': "The Open Graph protocol enables any web page to become a "
                   "rich object in a social graph.",
}

multiple_images_data = """
<!DOCTYPE html>
<html>
  <head prefix="og: http://ogp.me/ns#">
    <meta property="og:title" content="Open Graph protocol">
    <meta property="og:type" content="website">
    <meta property="og:url" content="http://ogp.me/">
    <meta property="og:image" content="http://ogp.me/logo.png">
    <meta property="og:image:type" content="image/png">
    <meta property="og:image:width" content="300">
    <meta property="og:image:height" content="300">
    <meta property="og:image:alt" content="The Open Graph logo">
    <meta property="og:image" content="http://ogp.me/logo2.png">
    <meta property="og:image:width" content="600">
    <meta property="og:image:height" content="600">
    <meta property="og:description" content="The Open Graph protocol enables any web page to become a rich object in a social graph."> # noqa
  </head>
  <body>
  </body>
</html>
"""


def test_ogp_is_valid():
    ogp = OGP(data=ogp_data)
    assert ogp.is_valid


def test_ogp_results():
    ogp = OGP(data=ogp_data)
    for k, v in ogp_results.items():
        assert getattr(ogp, k) == v


def test_ogp_properties():
    ogp = OGP(data=ogp_data)
    assert sorted(list(ogp_results.keys())) == sorted(ogp.properties)


def test_ogp_data_no_exist():
    ogp = OGP(data=ogp_data)
    with pytest.raises(AttributeError):
        ogp.nonexistant


def test_get_already_existing_property():
    ogp = OGP(data=ogp_data)
    ogp._properties['new_data'] = 'foo'
    assert ogp.new_data == 'foo'


def test_multiple_images():
    ogp = OGP(data=multiple_images_data)
    assert type(ogp.image) == list
