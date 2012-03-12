.. :contents: 

Introduction
-------------

A sane Plone 4 theme template. Provides ``yourtheme`` code skeleton.
The skeleton is not limited to visual aspects, but
allow customizing Plone UI aspects beyond simple CSS changes
or HTML transformations easily.

Goals
-------

* EASY

* Well documented, follows best practices, cross-refers to documentation

* Provides basic solution for basic theming and UI customizations needs

* Minimum boilerplate: no ZCML, explicit folder structure, etc. Based on Grok and Dexterity frameworks

* ``main.css`` boilerplate

* ``main.js`` boilderplate

* Documented intructions for basic UI customization tasks

* Multilingual support (i18n)

* Good folder structure: flat is better than nested

This is a barebone code drop and does not depend on more or less
crappy Python templating solutions. There is no need for using code generators,
as actions like adding a view are simple code copy-pastes following
the sane defaults and Dont Repeat Yourself (DRY) principles.

Just clone it, hack and go.

Prerequisites
---------------

* Working UNIX environment (e.g. Cygwin for Windows should be fine)

* Basic command-line usage knowledge

Usage
-------

Get tarball from GitHub.

Extract to ``src/`` folder under your buildout folder::

	cd src
	git clone git@github.com:miohtama/sane_plone4_theme_template.git

Add Dexterity extends line to your ``buildout.cfg``:

* http://plone.org/products/dexterity/documentation/how-to/install

Add the following bits to ``buildout.cfg`` to install add-on::

	develop = 
		src/yourtheme

	eggs =
		...
		yourtheme

Then follow standard Plone add-on installation instructions
of re-running buildout and activating the add-on.

* http://plone.org/documentation/kb/installing-add-ons-quick-how-to

After the add-on is activated, the theme overrides from 
``yourtheme`` become active for views, viewlets.

The defaukt installation comes with 

* a logo override example

* Hello world view which is available at http://localhost:8080/Plone/@@helloworld

Renaming
-----------

For changing the name ``yourtheme`` to something else a simple

TODO

Dive into
-----------

This source code provides Python package (a.k.a egg) ``yourtheme``.
The package can be used as a Plone add-on to override Plone user interface functionality easily.

The folder layout follows Python package layout where you have

* Top level folder with ``setup.py`` package metadata

* ``yourtheme`` Python module

* `Grok static folder <http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/resourcefolders.html#grok-static-media-folder>`_ for images, CSS and Javascript.

* ``views.py`` and ``viewlets.py`` for Plone user interface element declarations

* Standard ``configure.zcml`` Zope 3 boiler-plate (no need to touch here)

' ' 

Tasks
------

How to 

* Automatic Plone restarts

Add a view
============

A HelloWorld view example is provided in ``views.py``. Feel free to copy-paste around.

More info

* 

* Override a view

* Override an old style page template (skins overrides)

* Add a viewlet

* Override a viewlet

* Hide a viewlet

* Changing viewlet manager layout

* Override main template

* Add a portlet

* Override a portlet rendering

* Override CSS styles

* Override a logo

* Add new CSS

* Add new Javascript

* Change content type default view

* Creating new folder-like listing view

* Add a new dynamic view to a folder

Authors
---------

* `Mikko Ohtamaa <http://opensourcehacker.com>`_



