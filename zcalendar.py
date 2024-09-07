#!/usr/bin/python3
# -*- coding: UTF-8 -*-
#  @author dlaw
#
#
#  install requests:
#   python -m pip install requests
#   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
#   pip install python-dateutil
#################################################################
from datetime import datetime
import datetime
import pickle
import os.path
import dateutil.parser
import os
#import dateutil.parser
#from PIL import Image,ImageDraw,ImageFont
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def get_events_from_calendar( srv, calendarName ):
    retval = []
    t = datetime.datetime.now()
    ucl = srv.calendarList().list().execute()
    cl = ucl['items'] #  cal.calendarList().list().execute();
    calendarId = ""
    for id in cl :
        if id['summary'] == calendarName :
            calendarId = id['id']
    #print( calendarId )
    if calendarId == "" :
        print("calendar id is null")
        return []
    #colors = srv.colors().get().execute()
    events = srv.events().list(calendarId=calendarId,orderBy='startTime',singleEvents=True,maxResults=30,timeMin=t.isoformat()+'Z').execute() #,,maxResults=20,,timeMin=t).execute()
    for item in events['items']:
            #print( item['summary'] )
            allDay = False
            s = datetime.datetime.now()
            e = datetime.datetime.now()
            #date = item['start']['dateTime']
            if 'dateTime' in item['start']:
                date = item['start']['dateTime'][0:19]
                #print( date )
                s = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S")
                e = datetime.datetime.strptime(item['end']['dateTime'][0:19], "%Y-%m-%dT%H:%M:%S")
            else:
                date = item['start']['date']
                s = datetime.datetime.strptime(date, "%Y-%m-%d")
                e = s
                allDay = True

            #color := colors['calendar'][item['colorid']]['foreground']
            #bgcolor := colors.Calendar[item.ColorId].Background
            #
            #colorID := item.ColorId
            #if calendarName == "Menu" {
            #   colorID = "5"
            #}

            #fmt.Println(fmt.Sprintf("%v (%v)", item.Summary, date))
            startDate = dateutil.parser.isoparse( s.isoformat() )
            dt = ""
            if( allDay == True ):
                dt = startDate.strftime( "%A" )
            else:
                dt = startDate.strftime( "%A, %I:%M-" )
                endDate = dateutil.parser.isoparse( e.isoformat() )
                de = endDate.strftime( "%I:%M" )
                dt = dt + de
            newEvent = { 'name': item['summary'], 'allday': allDay, 'display_date': dt,
                'start': s.isoformat(), 'end': e.isoformat(), 'calendar': calendarName }
            
            retval.append(newEvent)
    return retval

def fetch_calendar():
    global events
    print( "fetching calendar" )
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    familyEvents = get_events_from_calendar( service, "Family Calendar")
    menuEvents = get_events_from_calendar( service, "Menu" )
    events = menuEvents + familyEvents
    events.sort( key=sortKey )
    #print( events )
    return events

def sortKey(e):
    return e['start']
