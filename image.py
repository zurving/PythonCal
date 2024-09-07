import cherrypy

class image(object):

    @cherrypy.expose
    def image(self, nocache=''):
        cherrypy.response.headers['Content-Type'] = 'image/jpeg'
        # Opening the binary file in binary mode as rb(read binary)
        f = open("resources/fall_foliage.jpg", mode="rb")        
        # Reading file data with read() method
        data = f.read()
        # Closing the opened file
        f.close()
        return data
    

