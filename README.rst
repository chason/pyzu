=================
pyzu 🐍図
=================

A Python class for retrieving `Open Graph`_ metadata from a website.

Overview
----------

There's a fair number of Open Graph metadata libraries for Python, but all of
the currently active ones use an HTML parser like BeautifulSoup to extract the
metadata. There's nothing wrong with that, and it comes with some advantages
but I wanted one that parses the webpage as RDFa, and so here we are.

This library extracts the Open Graph metadata and makes it available via the
object's properties. Most of the other libraries I've encountered that do this
take a website's URI and download the data there but this library takes the
text of the website as the data instead. This was done because I've found that
various websites like to hide their OGM data behind user agents so this allows
you to get the data however you need to. It is also much easier to test.

See the TODO.rst file for information about features that I will be adding to
this library.

Basic Usage
---------------

You can get the website source any way you like but in these examples I will be
using Requests_.

First initialize the object with the data from Requests::

    import requests
    from pyzu import OGP

    r = requests.get('http://ogp.me/')
    ogp_me = OGP(r.text)

After this we can check the validity of the data (essentially does it contain
the four required attributes as specified by the `OGP spec`_ [title, type,
image, and url]::

    >>> ogp_me.is_valid
    True

and finally we can look at the properties individually or see all the properties
that we were able to extract from the page::

    >>> ogp_me.title
    'Open Graph protocol'
    >>> ogp_me.properties
    ['description', 'url', 'image:height', 'image:alt', 'type', 'image', 'image:width', 'title', 'image:type']


.. _Open Graph: http://ogp.me/
.. _Requests: http://docs.python-requests.org/en/master/
.. _OGP spec: http://ogp.me/#metadata
