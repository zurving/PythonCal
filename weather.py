import re
import requests

def fetch_weather():
    weatherText = ""
    #command = "curl --silent \"https://forecast.weather.gov/MapClick.php?lat=42.9353&lon=-72.2791&unit=0&lg=english&FcstType=text&TextType=1\""
    #stream = os.popen(command)
    #output = stream.read()
    x = requests.get('https://forecast.weather.gov/MapClick.php?lat=42.9353&lon=-72.2791&unit=0&lg=english&FcstType=text&TextType=1')
    output = x.text
    if output != "" :
        #print( output )
        weatherText = output
        index = weatherText.find( "https://www.weather.gov/gyx" )
        if( index != -1 ):
            weatherText = weatherText[:index]
            #print( weatherText )
        #index = weatherText.rfind( "<td colspan=\"2\" valign=\"top\" align=\"left\">" ) + 1
        #weatherText = weatherText[index:]
        #index = weatherText.find( "<" )
        weatherText = weatherText.replace( "Last Update:", "" )
        for m in re.finditer("<b>[A-Za-z ]+: </b>",weatherText):
            index = m.start(0)
            break
        weatherText = weatherText[index:]
        #print( weatherText )
        #weatherText = weatherText[index:]
        #weatherText = weatherText.replace( "<br>", "" )
        #weatherText = weatherText.replace( "<b>", "" )
        weatherText = weatherText.replace( "</b>", "</b><br/>" )
        #weatherText = weatherText.replace( "\r\r", "\n" )
        #weatherText = weatherText.replace( "\n\n", "\n" )
        #weatherText = weatherText.replace( "\n", "\r\n" )
        #weatherText = weatherText.replace( " \r\n", "\r\n" )
        index = weatherText.find( "<hr><br>" )
        weatherText = weatherText[:index]
        #print( weatherText )
        #quit()
    return weatherText