"""

    For more information see

    * http://collective-docs.readthedocs.org/en/latest/components/interfaces.html

    * http://collective-docs.readthedocs.org/en/latest/views/layers.html

"""

from zope.interface import Interface
from plone.theme.interfaces import IDefaultPloneLayer


class IThemeSpecific(IDefaultPloneLayer):
    """
    Marker interface that defines a browser layer against which you can register views and viewlets.

    When your theme is selected this layer becomes active and all overrides associated with
    override default Plone render actions.
    """


class IAddonSpecific(Interface):
    """
    Marker interface that defines a browser layer against which you can register views and viewlets.

    When your add-on is installed this layer becomes active and all overrides associated with
    override default Plone render actions.
    """
