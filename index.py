import cherrypy

class index(object):

    @cherrypy.expose
    def index(self):
        data = '''
        <html>
          <head>
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js"></script>
            <script src="/script/script/"></script>
            <title>PythonCal</title>
            <style>
              body{
                background-color: black;
                color: white;
              }

              #calendardiv{
                border: solid 1px white;
                border-radius: 3px;
                position: absolute;
                top: 47px;
                bottom: 10px;
                left: 10px;
                width: 250px;
                overflow:scroll;
                -ms-overflow-style: none;  /* IE and Edge */
                scrollbar-width: none;  /* Firefox */
              }
              /* Hide scrollbar for Chrome, Safari and Opera */
              #calendardiv:-webkit-scrollbar {
                display: none;
              }              

              .event-name{
                font-size: 18px;
                font-weight: bold;
                width: 100%
              }

              .event-div{
                padding: 5px;
                border-radius: 5px;
              }

              .event-dark{
                background-color: #242424;
              }

              .event-date{
                text-align: right;
              }

              #closediv{
                border: solid 1px white;
                border-radius: 3px;
                position: absolute;
                top: 10px;
                height: 32px;
                right: 10px;
                width: 32px;
                overflow:hidden;
                font-size: 30px;
                text-align:center;
              }

              #weatherdiv{
                border: solid 1px white;
                border-radius: 3px;
                position: absolute;
                top: 47px;
                bottom: 380px;
                right: 10px;
                left: 270px;
                overflow-y:scroll;
                font-size: 18px;
                -ms-overflow-style: none;  /* IE and Edge */
                scrollbar-width: none;  /* Firefox */
                padding:5px;
              }

              /* Hide scrollbar for Chrome, Safari and Opera */
              #weatherdiv:-webkit-scrollbar {
                display: none;
              }

              #imagediv{
                border: solid 1px white;
                border-radius: 3px;
                position: absolute;
                height: 360px;
                bottom: 10px;
                right: 10px;
                left: 270px;
                overflow:hidden;
                background-repeat: no-repeat;
                background-size: cover;
              }

            </style>
          </head>
          <body>
            <p>loading...</p>
          </body>
        </html>
        '''

        return data
