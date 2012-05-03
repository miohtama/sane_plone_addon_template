"""

        For more information see

        * http://collective-docs.readthedocs.org/en/latest/views/viewlets.html  

"""

# Zope imports
from zope.interface import Interface
from zope.component import getMultiAdapter
from five import grok

# Plone imports
from plone.app.layout.viewlets.interfaces import IPortalFooter

# Local imports
from interfaces import IAddonSpecific, IThemeSpecific

grok.templatedir("templates")
grok.layer(IAddonSpecific)

# By default, set context to zope.interface.Interface
# which matches all the content items.
# You can register viewlets to be content item type specific
# by overriding grok.context() on class body level 
grok.context(Interface)

# EXAMPLES START
class MyFooter(grok.Viewlet):
        """
        An example viewlet.
        """

        # For available viewlet managers see
        # https://github.com/plone/plone.app.layout/blob/master/plone/app/layout/viewlets/configure.zcml
        grok.viewletmanager(IPortalFooter)

        def update(self):
                """
                Set member variables before rendering the template.

                These variables are exposed via ``viewlet/`` traversing in page template code.
                """

                # See 
                # http://collective-docs.readthedocs.org/en/latest/misc/context.html
                # how to acquire various helper utilities related to self.context
                self.portal_state = getMultiAdapter((self.context, self.request), name="plone_portal_state")
                self.context_state = getMultiAdapter((self.context, self.request), name="plone_context_state")

# EXAMPLES END
