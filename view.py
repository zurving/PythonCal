import platform

class view(object):
        
    def __init__(self):
        self.window = None
        self.process = None
        if( not platform.system() == 'Linux' ):
            import webview  
            self.window = webview.create_window( 'Python Calendar', 'http://localhost:8080/index/index', 
                                        width=800, height=1200, min_size=(800, 1000), fullscreen=False )

        else:
            import subprocess
            self.process = subprocess.Popen( ['firefox',
				'--no-remote',
                                '--kiosk',
                                'http://localhost:8080/index/index'])
#                                '-no-remote',

    def wait(self):
        if( self.window != None ):
            import webview
            webview.start()
        else:
            self.process.wait()
            print( 'exit' )

    def destroy(self):
        if( self.window != None ):
            self.window.destroy()
        else:
            self.process.terminate()
