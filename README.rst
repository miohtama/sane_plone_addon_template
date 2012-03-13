

.. :contents: 

Introduction
-------------

This project is a sane Plone 4 add-om / theme template which provides 
``youraddon`` code skeleton. It allows you to quicky start
developing your own Python, CSS and JS code for Plone. 

The skeleton is not limited to visual aspects, but
allow customizing Plone UI aspects beyond simple CSS changes
or HTML transformations easily. It is indended
to replace old *ZopeSkel plone* add-on template 
with a version embracing modern best development practices.

Supported Plone versions
----------------------------

Supported Plone versions are 4.1 and above. 
Dexterity pindowns are required, though there is 
no dependency to ``plone.app.dexterity`` package,
only ``five.grok``.

Goals
-------

* EASY

* Well documented, follows best practices, cross-refers to up-to-date documentation

* Provides basic solution for basic theming and UI customizations needs with documented instructions

* Minimum boilerplate: no unnecessary ZCML or folder structure, etc. Based on Grok and Dexterity frameworks

* ``main.css`` and ``main.js`` where front-end developers can directly copy-paste their code

* Multilingual support (i18n)

* Good folder structure: flat is better than nested

This is a barebone code drop and does not depend on, more or less,
crappy Python templating solutions. There is no need for using code generators,
as actions like adding a view are simple code copy-pastes following
the sane defaults and Dont Repeat Yourself (DRY) principles.

Just clone it to ``src/`` folder, hack and go.

Benefits over through-the-web customizations
==============================================

Old Zope 2 customization methods of using Zope Management Interface
are seriously limited and rarely take you even half-way of your development
needs. But ``youraddon`` template

* Provides full power of Python. File system based editing, giving 100% full access to change everything vs. old ZMI based through-the-web overrides. Use real text editor instead of <textarea>.

* Your code can go properly under version control

* Embraces modern development practices, like GitHub, jQuery and stuff

* You can still have the speed of instant code changes using *sauna.reload* package
  as described below

NO MORE THROUGH-THE-WEB PYTHON SCRIPTS, EVER, FOR ANYONE.
DO NOT DO ADD NEW... SCRIPT (PYTHON), COMPRENDE? 
NO MORE EDITING IN PUNY TEXTAREA, USE YOUR FAVORITE EDITOR,
WITH SYNTAX HIGHLIGHTING.
NO MORE UNAUTHORIZED EXCEPTION - IMPORT ALL PYTHON MODULES
YOU WISH. NO MORE ZSQL METHODS. FEEL FREE.. OF ALL THAT
LEGACY CRAP. FEEL THE AGILE DEVELOPMENT RUNNING IN YOUR
VEINS. INVENT, CREATE, ENJOY. 
 
Of course, one cannot understand this pain unless
has gone through Plone 2... Plone 4.
Just forget all other tutorials and do as said here.

Prerequisites
---------------

* Working UNIX environment (Cygwin for Windows should be fine)

* Basic command-line usage knowledge

Usage
-------

Get the tempalte source code from GitHub and 
to ``src/`` folder under your Plone installation folder::

	cd src
	git clone git@github.com:miohtama/sane_plone_addon_template.git youraddon

`Add Dexterity extends line <http://plone.org/products/dexterity/documentation/how-to/install>`_ to your ``buildout.cfg``::

	extends = 
		...
		some lines here
		...
		http://good-py.appspot.com/release/dexterity/1.2?plone=4.1.4

Note that this depends on Plone version. Fix to match to your version.

Furthermore, add the following bits to ``buildout.cfg`` to install the code skeleton add-on::

	develop = 
		src/youraddon

	eggs =
		...
		youraddon

Then follow standard Plone add-on installation instructions
of re-running buildout and activating the add-on

* http://plone.org/documentation/kb/installing-add-ons-quick-how-to

After *youraddon* add-on is installed in Plone control panel you should
see a pony greeting you on instead of the 
Plone site logo, showing that the code skeleton examples
are active. 

Now you can proceed to start adding your own code bits.
See Tasks section below for recipes for most common Plone customization needs. 

Bootstrapping the development of your own add-on
--------------------------------------------------

The default ``youraddon`` installation comes with some sample customizations highlighting the best pratices.
These customizations are examples which are referred in documentation how to accomplish 
certain development tasks with Plone.
``youraddon`` installation is usable for tinkering as is.

However, you are supposed to remove these example customizations and rename the add-on 
when you adapt the code skeleton for your own needs.

You can do with ``personalize.py`` script. The script will remove all example view, viewlet, CSS and JS customizations by removing source code lines between ``EXAMPLES START`` and ``EXAMPLES END`` markers.
The script will also give a new name for Python package.

First uninstall ``youraddon`` add-on from your site if you installed it there.

Then run personalize::

	cd src/youraddon
	# Will create a copy src/mycompanyaddon out of youraddon
	# with all examples removed
	./personalize mycompanyaddon 

Now ``src/mycompanyaddon`` has been created. ``src/youraddon`` will be still around
for further templating.

You need to do respective name changes in ``buildout.cfg`` and re-run buildout.
Then restart Plone, install add-on ``mycompanyaddon``.

*personalize* will also clean up the add-on from orignal version control files.

Note that currently *personalize* is one time operation, not incremental, and you cannot
update to more recent version of the code skeleton. 

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

When in development mode, even if not using *sauna.reload* Plone reloads following bits automatically

* .pt page templates

* CSS

* Javascript

* ``profiles/default`` XML files

The following code is not reloaded:

* Python

* ZCML

Add a view
============

Views present functionality or content. Views can be associated with
content types or site root.

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

If you need to touch viewlet Python class code the easiest
approach is to

* Copy-paste the orignal viewlet Python code as a whole

* Copy-paste the orignal viewlet template code as a whole

Then register your own viewlet with the name of the original
using ``grok.name()``.

It's possible, though often suicidal, try to extend the orignal
viewlet and then override.

More info

* http://collective-docs.readthedocs.org/en/latest/views/viewlets.html

Hide a viewlet
======================================================

* http://collective-docs.readthedocs.org/en/latest/views/viewlets.html

Changing viewlet manager layout
======================================================

* http://collective-docs.readthedocs.org/en/latest/views/viewlets.html

Override main template
======================================================

To change Plone main presentation layout

* http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/template_basics.html#main-template

Add a portlet
======================================================

Override a portlet rendering
======================================================

Override CSS styles
======================================================

Override a logo
======================================================

Add a new CSS styles and file
======================================================

Example provided in ``main.css``.

More info

* http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/css.html

Add new Javascript
======================================================

Example provided in ``main.js``.

Plone should automatically reload CSS files 
in the development mode when you hit *Refresh*. 
in the browser.

More info

* http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/javascript.html

Change content type default view
======================================================

Creating new folder-like listing view
======================================================

Add a new dynamic view to a folder
======================================================

Add translated strings
===========================

You can add multilingual strings to user interface which are
translated using *gettext*.

More info

* http://collective-docs.readthedocs.org/en/latest/i18n/internalization.html

Adding new language
===========================

You can include new languages to the translation mix.

More info

* http://collective-docs.readthedocs.org/en/latest/i18n/internalization.html

Best practices
-----------------

Here are listed some best practices which are recommended when working 
with Plone, Python and web development source code.

No tabs
============

All text editors: set save tabs as spaces, never use hard tabs.

Dynamically generated files
=============================

*Never* import the following files to version control:

* Various .egg-info folders (automatically generated when buildout runs)

* .mo files (compiled gettext files recreated on Plone start-up)

JSLint
============

* http://opensourcehacker.com/2011/09/23/using-javascript-jslint-validator-in-eclipse-and-aptana-studio/

PEP8
============

* TODO 

PyFlaks
============

* TODO

Troubleshooting
------------------

If you get this::

	PicklingError: Can't pickle <class 'youraddon.interfaces.IAddonSpecific'>: import of module youraddon.interfaces failed 

This means that you did not follow uninstall instructions carefully. 
Re-add ``youraddon`` in ``buildout.cfg``, re-run buildout, then uninstall it in Plone control panel
and then re-remove from ``builout.cfg``.	

Authors
---------

* `Mikko Ohtamaa <http://opensourcehacker.com>`_

* `Érico Andrei  <https://twitter.com/#!/ericof>`_

* Pony by `Lili / novotnaci <http://openclipart.org/detail/102193/foal-by-novotnaci>`_

