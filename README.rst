flake8-snippets
===============

A flake8 extension to find any code snippets you don't like.

Flake8 is a tool to combine different apps (like pep8) and therefore to
guarantee clean Python code.

Read more: http://flake8.readthedocs.org/en/latest/

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    $ pip install flake8-snippets

To get the latest commit from GitHub

.. code-block:: bash

    $ pip install -e git+git://github.com/bitmazk/flake8-snippets.git#egg=flake8_snippets


Usage
-----


Contribute
----------

If you want to contribute to this project, please perform the following steps

.. code-block:: bash

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 flake8-snippets
    $ python setup.py install
    $ pip install -r test_requirements.txt

    $ git co -b feature_branch master
    # Implement your feature and tests
    $ git add . && git commit
    $ git push -u origin feature_branch
    # Send us a pull request for your feature branch
