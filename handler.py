import weather
import zcalendar
import cherrypy

class handler(object):

    @cherrypy.expose  
    @cherrypy.tools.json_out()  
    def update(self):
        w = weather.fetch_weather()
        c = zcalendar.fetch_calendar()
        return { "weather": w, "calendar": c }
