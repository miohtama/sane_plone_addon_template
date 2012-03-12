"""

	For more information see

	* http://collective-docs.readthedocs.org/en/latest/components/interfaces.html

"""

from plone.theme.interfaces import IDefaultPloneLayer

class IThemeSpecific(IDefaultPloneLayer):
    """
    Marker interface that defines a browser layer against which you can register views and viewlets.

    When your theme is selected this layer becomes active and all overrides associated with
    override default Plone render actions.
    """