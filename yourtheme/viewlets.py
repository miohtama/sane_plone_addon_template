"""

	For more information see

	* http://collective-docs.readthedocs.org/en/latest/views/viewlets.html	

"""

from five import grok

from interfaces	import IThemeSpecific

grok.templatedir("templates")
grok.layer(IThemeSpecific)

