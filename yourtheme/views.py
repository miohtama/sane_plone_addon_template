"""

	Plone views overrides.

	For more information see

	* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

"""

from five import grok

from interfaces	import IThemeSpecific

grok.templatedir("templates")
grok.layer(IThemeSpecific)

class HelloWorld(grok.View)
	"""
	Example view rendering a Plone page in the default Plone framing.
	
	Automatically associates itself with ``helloworld.pt`` templates.
	"""
