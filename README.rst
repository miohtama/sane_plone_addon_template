.. :contents: 

Introduction
-------------

**A simple Plone add-on / theme skeleton with instructions**

This project is a sane Plone 4 add-on / theme template which provides 
``youraddon`` code skeleton. It allows you to quicky start
developing your own Python, CSS and JS code for Plone. 

The skeleton is not limited to visual aspects, but
allow customizing Plone UI aspects beyond simple CSS changes
or HTML transformations easily. It is intended
to replace the old *ZopeSkel plone* add-on template 
with a version embracing modern development best practices.

Supported Plone versions
----------------------------

Supported Plone versions are 4.1 and above. 
Dexterity pindowns are required, though there is 
no dependency on the ``plone.app.dexterity`` package,
only on ``five.grok``.

Goals
-------

* EASY

* Well documented, follows best practices, references up-to-date documentation

* Provides a basic solution for basic theming and UI customizations needs with documented instructions

* Minimum boilerplate: no unnecessary ZCML or folder structure, etc. Based on Grok and Dexterity frameworks

* ``main.css`` and ``main.js`` where front-end developers can directly copy-paste their code

* Multilingual support (i18n)

* Good folder structure: flat is better than nested

This is a barebone code drop and does not depend on any more or less
crappy Python templating solutions.
There is no need for using code generators,
because actions like adding a view are simple code copy-pastes following
the sane defaults and *Don't Repeat Yourself* (DRY) principles.

Just clone it to your installation as ``src/youraddon``,
make sure the necessary buildout changes have been made, hack and go.

Benefits over through-the-web customizations
==============================================

Old Zope 2 customization methods of using Zope Management Interface
are seriously limited and rarely take you even half-way of your development
needs. But ``youraddon`` template:

* Provides full power of Python.
  File system based editing, giving 100% full access to change everything
  vs. old ZMI based through-the-web overrides. Use real text editor instead
  of <textarea>.

* Your code can go properly under version control

* Embraces modern development practices, like GitHub, jQuery and stuff

* You can still have the speed of instant code changes using the
  `sauna.reload`_ package as described below

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

**Follow these instructions carefully**.
No warranty for users who did not read the instructios.

Get the template source code from GitHub and clone it 
to the ``src/`` folder under your Plone installation folder::

    cd src
    git clone git@github.com:miohtama/sane_plone_addon_template.git youraddon

Add `Dexterity extends line <http://plone.org/products/dexterity/documentation/how-to/install>`_ to your ``buildout.cfg``::

    extends = 
        ...
        some lines here
        ...
        http://good-py.appspot.com/release/dexterity/1.2?plone=4.1.4

Note that this depends on Plone version. Fix to match to your version.

Add the following bits to ``buildout.cfg`` to install the code skeleton add-on::

    develop = 
        src/youraddon

    eggs =
        ...
        youraddon

.. Note:: If you want to call Python package something different than
    ``youraddon`` you can change this by running the ``personalize.py``
    command later.
    Renaming is not necessary for the code skeleton to work and the
    instructions have been written with the original name in mind.

Then follow standard Plone add-on installation instructions
of re-running buildout and activating the add-on:

* http://plone.org/documentation/kb/installing-add-ons-quick-how-to

After the *youraddon* add-on is installed in the Plone control panel you
should see a pony greeting you instead of the 
Plone site logo, showing that the code skeleton examples
are active. 

Now you can proceed to start adding your own code bits.
See the Tasks_ section below for recipes for most common Plone customization needs. 

Bootstrapping the development of your own add-on
--------------------------------------------------

The default ``youraddon`` installation comes with some sample customizations highlighting the best pratices.
These customizations are examples which are referred in documentation how to accomplish 
certain development tasks with Plone.
``youraddon`` installation is usable for tinkering as is.

However, you are supposed to remove these example customizations and rename the add-on 
when you adapt the code skeleton for your own needs.

You can do this with the ``personalize.py`` script.
The script will remove all example view, viewlet, CSS and JS examples by
removing source code lines between ``EXAMPLES START`` and ``EXAMPLES END``
markers.
The script will also give a new name to the Python package.

Before you run ``personalize.py``, 
uninstall the ``youraddon`` add-on from your site if you installed it there.

Then run personalize::

  cd src/youraddon
  # Will create a copy src/mycompanyaddon out of youraddon
  # with all examples removed
  ./personalize.py mycompanyaddon 


Please note that the template discourages usage of namespaces.
Namespaces are not needed for your own customizations and cause extra boilerplate.
If you wish to use namespaces like ``collective`` or ``plone.app`` you can
manually shuffle files and folders around later.

Now ``src/mycompanyaddon`` has been created. ``src/youraddon`` will be still around
for further templating.

You need to do corresponding name changes in ``buildout.cfg`` and re-run buildout.
Then restart Plone, and install the ``mycompanyaddon`` add-on.

*personalize* will also remove the original version control files from the
new add-on.

Note that currently *personalize* is a one-time operation, not incremental,
and you cannot update to more recent version of the code skeleton. 

Theme or add-on
------------------

The difference between Plone theme and Plone add-on is that
only one theme can be active at a time. Resources like views,
static media, etc. depend on whether the theme / add-on layer is active or not.

* The theme layer is activated through the ``portal_skins`` *properties* tab
  (*Default skin* option matches ``configure.zcml`` declaration)

* Add-on layer is activated when add-on is *installed* (activated via
  ``browserlayers.xml``)

The code skeleton default behavior is add-on like.
You can change it to theme-like behavior by:

* Uncommenting directives in ``profiles/defaul/skins.xml``.

* Changing ``grok.layer()`` directives from ``IAddonSpecific`` to
  ``IThemeSpecific``.

More info

* http://collective-docs.readthedocs.org/en/latest/views/layers.html

Theory of add-on development
------------------------------

You do not replace Plone functionality by messing with Plone files directly.
Instead you:

* extend Plone to add new functionality;

* override Plone to customize out-of-the-box functionality.

Overrides and extensions become effective when your add-on is installed
and the effect disappears when your add-on is uninstalled.

This way you keep your own customizations separate from Plone core.
You do not ever edit Plone core source code files directly.
If you do this, your edited files will be replaced by updated versions
when Plone is updated.
This holds true for all CMSes, not just for Plone.
Never edit anything under the ``parts/`` or ``eggs/`` folders
in your Plone installation.

Plone has a mechanism called *layers*, specifying which add-on / theme
parts are effective. Once your add-on is installed,
its layer takes the highest priority in the Plone installation,
overriding functionality with lower priority. 

Layers are the central element of well-functioning 
plug-in architecture, ensuring that add-ons don't
step on each others toes, resulting in code conflicts.

Dive into
-----------

This source code provides the Python package (a.k.a. *egg*) ``youraddon``.
The package can be used as a Plone add-on to override Plone user interface functionality easily.

The folder layout follows Python package layout where you have:

* a top-level folder with ``setup.py`` package metadata;

* ``youraddon`` Python module;

* ``static`` `Grok static folder <http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/resourcefolders.html#grok-static-media-folder>`_ for images, CSS and Javascript;

* ``views.py`` and ``viewlets.py`` for Plone user interface element declarations;

* standard ``configure.zcml`` Zope 3 boiler-plate - no need to touch here.

Tasks
------

Here are quick pointers for common theming / Plone UI customization related development tasks. 

Automatic Plone restarts
===========================

Use `sauna.reload`_ on UNIX systems to reload your code automatically.
This will considerably increase your working effectiveness.

When in development mode, even if not using ``sauna.reload``, Plone reloads
the following bits automatically:

* ``.pt`` page templates

* CSS

* Javascript

* ``profiles/default`` XML files

The following code is not reloaded:

* Python

* ZCML

Validating source files
============================

`VVV <http://pypi.python.org/pypi/vvv>`_ is used to provide validation support for

* CSS

* Javascript 

* Python 

* Restructured text files

Please consult *VVV* documentation how to install pre-commit hooks which
prevent you to accidentally committing files containing validation or linting errors.

Add a view
============

Views present functionality or content. Views can be associated with
content types or site root.

A *HelloWorld* view example is provided in ``views.py``.
Feel free to copy-paste around.

More info

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

Finding view source code to override
=======================================

Plone views can be:

* view classes (new style): these come from Python packages.

* Pure page templates, no Python code attached (old style): these come from
  the ``plone_skins`` tool

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
template in the ``templates`` folder.

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
template in the ``templates`` folder.

More info

* http://collective-docs.readthedocs.org/en/latest/templates_css_and_javascripts/skin_layers.html#nested-folder-overrides-z3c-jbot

* http://pypi.python.org/pypi/z3c.jbot

Add a viewlet
======================================================

An example provided in ``viewlets.py`` to adding a custom footer viewlet.

More info:

* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

* http://grok.zope.org/doc/current/reference/components.html?highlight=viewlet#grok-viewlet

Override a viewlet template
====================================================== 

``z3c.jbot`` override example provided for the site logo in ``templates``.

More info:

* http://pypi.python.org/pypi/z3c.jbot

Override a viewlet
======================================================

If you need to touch viewlet Python class code the easiest
approach is to:

* copy-paste the orignal viewlet Python code as a whole;
* copy-paste the orignal viewlet template code as a whole.

Then register your own viewlet with the name of the original
using ``grok.name()``.

It's possible, though often suicidal, to try to extend the original
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

More info:

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

You can include new languages in the translation mix.

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

*Never* add the following files to version control:

* Various ``.egg-info`` folders (automatically generated when buildout runs)

* ``.mo`` files (compiled gettext files recreated on Plone start-up)

JSLint
============

* http://opensourcehacker.com/2011/09/23/using-javascript-jslint-validator-in-eclipse-and-aptana-studio/

PEP8
============

* TODO 

PyFlakes
============

* TODO

Troubleshooting
------------------

If you get this::

    PicklingError: Can't pickle <class 'youraddon.interfaces.IAddonSpecific'>: import of module youraddon.interfaces failed 

This means that you did not follow uninstall instructions carefully. 
Re-add ``youraddon`` in ``buildout.cfg``, re-run buildout,
then uninstall it in Plone control panel
and then re-remove from ``buildout.cfg``.   

Authors
---------

* `Mikko Ohtamaa <http://opensourcehacker.com>`_

* `Érico Andrei  <https://twitter.com/#!/ericof>`_

* Pony by `Lili / novotnaci <http://openclipart.org/detail/102193/foal-by-novotnaci>`_


.. _sauna.reload: http://pypi.python.org/pypi/sauna.reload
