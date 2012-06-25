"""

    Plone views overrides.

    For more information see

    * http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

"""

# Disable unused imports pylint warning as they are here
# here for example purposes
# W0611: 12,0: Unused import Interface

# pylint: disable=W0611

# Zope imports
from zope.interface import Interface
from five import grok
from Products.CMFCore.interfaces import ISiteRoot

# Local imports
from interfaces import IAddonSpecific, IThemeSpecific

grok.templatedir("templates")
grok.layer(IAddonSpecific)

# EXAMPLES START

class HelloWorld(grok.View):
    """
    Example view rendering a Plone page in the default Plone framing.

    Automatically associates itself with ``helloworld.pt`` templates.
    Make this view available only in Plone site root.

    http://localhost:8080/Plone/@@helloworld
    """


    # use grok.context(Interface) to associate view with every content item
    grok.context(ISiteRoot)

# EXAMPLES END