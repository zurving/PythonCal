import cherrypy
import sys

class shutdown(object):
    
    def setWindow( self, window ):
        self.window = window

    @cherrypy.expose
    def shutdown(self):
        cherrypy.engine.exit()
        self.window.destroy()
        return {}
