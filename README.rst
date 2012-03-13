.. :contents: 

Introduction
-------------

A sane Plone 4 theme template. Provides ``youraddon`` code skeleton.
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

* File system based editing, giving 100% full access to change everything vs. old ZMI based through-the-web overrides

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
		src/youraddon

	eggs =
		...
		youraddon

Then follow standard Plone add-on installation instructions
of re-running buildout and activating the add-on.

* http://plone.org/documentation/kb/installing-add-ons-quick-how-to

After the add-on is activated, the theme overrides from 
``youraddon`` become active for views, viewlets.

The defaukt installation comes with 

* a logo override example

* Hello world view which is available at http://localhost:8080/Plone/@@helloworld

Theme or add-on
------------------

The difference between Plone theme and Plone add-on is that
only one theme can be active at a time. Resources like views,
static media, etc. depend on whether the theme / add-on layer is active or not.

* Theme layer becomes activated through portal_skins properties tab (*Default skin* option matches configure.zcml declaration)

* Add-on layer becomes activated when add-on is installed (activated via ``browserlayers.xml``)

The code skeleton default behavior is add-on like.
You can change it to theme-like by 

* Uncommenting directives in ``profiles/defaul/skins.xml``.

* Changing ``grok.layer()`` directives from ``IAddonSpecific`` to ``IThemeSpecific``

More info

* http://collective-docs.readthedocs.org/en/latest/views/layers.html

Renaming / personalize
-------------------------

For changing the name ``youraddon`` package name to something else
there exist ``personalize.py``.

Example::

	cd src/youraddon
	./personalize yourfancyaddonname # Will create a copy src/yourfancyaddonname out of youraddon

Dive into
-----------

This source code provides Python package (a.k.a egg) ``youraddon``.
The package can be used as a Plone add-on to override Plone user interface functionality easily.

The folder layout follows Python package layout where you have

* Top level folder with ``setup.py`` package metadata

* ``youraddon`` Python module 

* ``static`` `Grok static folder <http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/resourcefolders.html#grok-static-media-folder>`_ for images, CSS and Javascript.

* ``views.py`` and ``viewlets.py`` for Plone user interface element declarations

* Standard ``configure.zcml`` Zope 3 boiler-plate - no need to touch here

Tasks
------

Here are quick pointers for common theming / Plone UI customization related development tasks. 

Automatic Plone restarts
===========================

Use `sauna.reload <http://pypi.python.org/pypi/sauna.reload>`_ on UNIX systems to reload your code automatically.
This will considerably raise your working effectiveness.

Add a view
============

A HelloWorld view example is provided in ``views.py``. Feel free to copy-paste around.

More info

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

Override a view template
===========================

z3c.jbot override.

Override a view class
===========================

Same as the add view, but you simply use ``grok.name()``
to declare the view name you want to override.

More info

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

Override an old style page template (skins overrides)
======================================================

Add a viewlet
======================================================

Override a viewlet
======================================================

Hide a viewlet
======================================================

Changing viewlet manager layout
======================================================

Override main template
======================================================

Add a portlet
======================================================

Override a portlet rendering
======================================================

Override CSS styles
======================================================

Override a logo
======================================================

Add new CSS file
======================================================

Add new Javascript
======================================================

Change content type default view
======================================================

Creating new folder-like listing view
======================================================

Add a new dynamic view to a folder
======================================================

Best practices
-----------------

All text editors: set save tabs as spaces, never use hard tabs.

JSLint

* http://opensourcehacker.com/2011/09/23/using-javascript-jslint-validator-in-eclipse-and-aptana-studio/

PEP8

* TODO 

PyFlaks

* TODO

Authors
---------

* `Mikko Ohtamaa <http://opensourcehacker.com>`_

* `Érico Andrei  <https://twitter.com/#!/ericof>`_

