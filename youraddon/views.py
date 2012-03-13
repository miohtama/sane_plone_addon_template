"""

	Plone views overrides.

	For more information see

	* http://collective-docs.readthedocs.org/en/latest/views/browserviews.html

"""

from five import grok

from interfaces	import IAddonSpecific, IThemeSpecific

from Products.CMFCore.interfaces import ISiteRoot

grok.templatedir("view-templates")
grok.layer(IThemeSpecific)

class HelloWorld(grok.View):
	"""
	Example view rendering a Plone page in the default Plone framing.
	
	Automatically associates itself with ``helloworld.pt`` templates.
	Make this view available only in Plone site root.

	http://localhost:8080/Plone/@@helloworld
	"""
	grok.context(ISiteRoot)

