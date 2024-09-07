import cherrypy
import handler
import index
import image
import screenmonitor
import script
import shutdown
import threading
import sys
import os
import view


def startServer( window, config ):
    cherrypy.tree.mount(handler.handler(), "/update/", config )
    cherrypy.tree.mount(index.index(), '/index/', config)
    cherrypy.tree.mount(script.script(), "/script/", config)
    cherrypy.tree.mount(image.image(), "/image/", config)
    s = shutdown.shutdown()
    s.setWindow( window )
    cherrypy.tree.mount(s, "/shutdown/", config )
    cherrypy.quickstart(handler.handler(), '/zurv/ing', config)


# Using the special variable  
# __name__ 
if __name__=="__main__":
    isFrozen = False
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        isFrozen = True
    elif __file__:
        application_path = os.path.dirname(__file__)
    datadir = os.path.join( application_path, "data" )

    print( datadir )

    config = {
        '/': {
            'tools.gzip.on': True,
            'tools.encode.text_only': False,
            'tools.encode.on': True,
            'tools.encode.encoding': 'utf-8',
        }
    }


    window = view.view()

    threading.Thread( target=startServer, daemon=True, args=[window, config ] ).start()

    sm = screenmonitor.screenmonitor()

    threading.Thread( target=sm.monitor, daemon=True, args=[True] ).start()

    window.wait()



