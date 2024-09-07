import cv2
import time
import numpy
import subprocess
from sys import platform

class screenmonitor(object):

    def turnOffScreen(self):
        if platform == "linux" or platform == "linux2":
            subprocess.run(["xset", "-display", ":0.0", "dpms", "force", "off"])

    def turnOnScreen(self):
        if platform == "linux" or platform == "linux2":
            subprocess.run(["xset", "-display", ":0.0", "dpms", "force", "on"])

    def monitor(self, actuallyMonitor ):
        if( not actuallyMonitor ):
            print( "dev mode - not monitoring" )
            return
        print( 'screenmonitor starting' )
        cam = cv2.VideoCapture(0)
        print( 'cam initialized' )
        last_mean = 0
        while( True ):
            ret, frame = cam.read()
            if ret: 
                # showing result, it take frame name and image  
                # output 
                gray = cv2.cvtColor( frame, cv2.COLOR_BGR2GRAY )
                result = numpy.abs(numpy.mean(gray) - last_mean)
                print(result)
                last_mean = numpy.mean(gray)
                if( result > 5.5 ):
                    print( "turn on screen" )
                    x, y = (0,0)
                    self.turnOnScreen()
                    time.sleep( 30 ) # keep it on for 5m
                else:
                    print( 'turn off screen')
                    self.turnOffScreen()
                    time.sleep( 5 )
            else:
                print( "unable to capture image... do you have a webcam?" )
                time.sleep( 60 )

# Using the special variable  
# __name__ 
if __name__=="__main__":            
    sm = screenmonitor()
    sm.monitor()
