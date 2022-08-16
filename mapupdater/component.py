from autobahn.twisted.wamp import ApplicationSession



class MapUpdaterComponent(ApplicationSession):
    def __init__(self, mapUpdater, config=None):
        ApplicationSession.__init__(self, config)
        self.mapUpdater = mapUpdater


    def onConnect(self):
        self.join(self.config.realm)


    def onJoin(self, details):
        print 'Component connected.'
        self.mapUpdater.checkMaps()
        self.subscribe(self.onUploadFinished, 'xyz.tempus2.mapupload.upload_finished')


    def onLeave(self, details):
        print 'Component lost connection.'


    def onUploadFinished(self, mapFilenames):
        print 'Remote update triggered.'
        self.mapUpdater.checkMaps(
            [f for f in mapFilenames if f.endswith('.bsp')])
