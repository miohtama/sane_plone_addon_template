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

* Embrases modern development practices (GitHub and stuff)

This is a barebone code drop and does not depend on more or less
crappy Python templating solutions. There is no need for using code generators,
as actions like adding a view are simple code copy-pastes following
the sane defaults and Dont Repeat Yourself (DRY) principles.

Just clone it, hack and go.

Prerequisites
---------------

* Working UNIX environment (Cygwin for Windows should be fine)

* Basic command-line usage knowledge

Usage
-------

Get tarball from GitHub.

Extract to ``src/`` folder under your buildout folder::

	cd src
	git clone git@github.com:miohtama/sane_plone_addon_template.git

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

Bootstrapping the development
---------------------------------

The default installation comes with some sample customizations highlighting the best pratices.
``youraddon`` is usable as is for tinkering.

However, you are supposed to remove these customizations and rename the add-on 
when you adapt the code skeleton for your own needs.

You can do with ``personalize.py`` script. The script will remove all example view, viewlet, CSS and JS customizations by removing source code lines between ``EXAMPLES START`` and ``EXAMPLES END`` markers.
The script will also give a new name for Python package.

Example::

	cd src/youraddon
	# Will create a copy src/mycompanyaddon out of youraddon
	# with all examples removed
	./personalize mycompanyaddon 


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

Finding view source code to override
=======================================

Plone views can be

* View classes (new style): this come from Python packages

* Pure page templates, no Python code attached (old style): these come from plone_skins tool

More info

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html#finding-a-view-to-override

Refer to static resources in page templates
==============================================

Example::

    <img tal:attributes="src string:${context/portal_url}/++resource++youraddon/pony.png" alt="" />

More info:

* http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/resourcefolders.html

* http://collective-docs.readthedocs.org/en/latest/images/templates.html

Override a view template
===========================

Use ``z3c.jbot`` override by dropping a corresponding 
template to ``templates`` folder.

More info

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html 

Override a view class
===========================

Same as the add view, but you simply use ``grok.name()``
to declare the view name you want to override.

More info

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

Override an old style page template (skins overrides)
======================================================

Use ``z3c.jbot`` override by dropping a corresponding 
template to ``templates`` folder.

More info

* http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/skin_layers.html#nested-folder-overrides-z3c-jbot

* http://pypi.python.org/pypi/z3c.jbot

Add a viewlet
======================================================

An example provided in ``viewlets.py`` to adding a custom footer viewlet.



More info

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

* http://grok.zope.org/doc/current/reference/components.html?highlight=viewlet#grok-viewlet

Override a viewlet template
====================================================== 

z3c.jbot override example provided for the site logo in ``templates``.

More info

* http://pypi.python.org/pypi/z3c.jbot

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

Example provided in ``main.css``.

Add new Javascript
======================================================

Example provided in ``main.js``.

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

* Pony by `Lili / novotnaci <http://openclipart.org/detail/102193/foal-by-novotnaci>`_

