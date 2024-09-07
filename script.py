import cherrypy

class script(object):

    @cherrypy.expose
    def script(self):
        cherrypy.response.headers['Content-Type'] = 'application/javascript'
        data = '''
        function fetchData(){
          $.get( "/update/update/", {}, onUpdate );
        }

        function addEvent( evnt, count ){
          var name = $("<div>").addClass("event-name").html( evnt.name );
          var date = $("<div>").addClass("event-date").html( evnt.display_date );
          if( evnt.calendar == "Menu" ){
            name.css("color", "yellow");
          }else{
            name.css("color", "Chartreuse");
          }
          var div = $("<div>").addClass("event-div");
          if( count %2 == 0 ){
            div.addClass( 'event-dark' );
          }else{
            div.addClass( 'event-light' );
          }
          div.append( name ).append( date );
          $("#calendardiv").append( div );
        }

        function requestShutdown(){
          $.get( "/shutdown/shutdown/" );            
        }

        function renderPage(){
          if( $("#clendardiv").length < 1 ){
            var b = $("body");
            b.html("");
            var calendardiv = $("<div id=\\"calendardiv\\"/>" );
            b.append( calendardiv );
            var closediv = $("<div id=\\"closediv\\">X</div>" ).click(requestShutdown);
            b.append( closediv );
            var w = $("<div id=\\"weatherdiv\\"/>");
            b.append( w );
            var imagediv = $("<div id=\\"imagediv\\"/>" );
            b.append( imagediv );
          }
        }

        function onUpdate( data ){
          renderPage();
          var events = data.calendar;
          for( var i=0; i < events.length; i++ ){
            addEvent( events[i], i );
          }
          //alert($("#calendardiv").html());
          $("#weatherdiv").html( data.weather );
          $("#imagediv").css("background-image", "url(/image/image/?nocache=" + Date.now() + ")" );
        }

        function setup(){
          fetchData();
          setInterval(fetchData, 600000);
        }

        $( document ).ready( setup );
        '''

        return data.encode('utf8')
    

