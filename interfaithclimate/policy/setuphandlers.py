from collective.grok import gs
from interfaithclimate.policy import MessageFactory as _

@gs.importstep(
    name=u'interfaithclimate.policy', 
    title=_('interfaithclimate.policy import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('interfaithclimate.policy.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
