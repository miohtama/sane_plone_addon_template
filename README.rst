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

This is a barebone code drop and does not depend on more or less
crappy Python templating solutions. There is no need for using code generators,
as actions like adding a view are simple code copy-pastes following
the sane defaults and Dont Repeat Yourself (DRY) principles.

Prerequisites
---------------

* ``tar`` UNIX command

* Basic command-line knowledge

Usage
-------

Get tarball from GitHub.

Extract to ``src/`` folder under buildout.

Add Dexterity extends line to your buildout.cfg.

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

Renaming
-----------

For changing the name ``yourtheme`` to something else a simple

TODO

Tasks
------

How to 

* Add a view

* Override a view

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



