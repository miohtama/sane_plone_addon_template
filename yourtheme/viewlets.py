"""

	For more information see

	* http://collective-docs.readthedocs.org/en/latest/views/viewlets.html	

"""

from five import grok

from interfaces	import IAddonSpecific, IThemeSpecific

grok.templatedir("viewlet-templates")
grok.layer(IAddonSpecific)

