from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import time
from flask_app import db, app, get_customers, add_customer


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
service = None

def authenticate_and_create_service():

  global service 

  # authenticate
  flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)

  creds = flow.run_local_server(port=0)
  
  # define service
  service = build('sheets', 'v4', credentials=creds)


def create_sheet():

  global service 

  # initialize new spreadsheet
  sheet = service.spreadsheets().create(body={ 'properties': { 'title': 'Customers' }}).execute()

  # get and return spreadsheet id
  return sheet['spreadsheetId']

def set_sheet_name(sheet_id):
  requests = [
        {
            'updateSheetProperties': {
                'properties': {'sheetId': 0, 'title': 'customer'},
                'fields': 'title'
            }
        }
    ]
  
  body = {'requests': requests}
  service.spreadsheets().batchUpdate(spreadsheetId=sheet_id, body=body).execute()


def add_data_to_sheet(sheet_id, data):

  global service 

  values = data
  body = { 'values': values }
  range_name = 'customer'

  add_result = service.spreadsheets().values().update(
        spreadsheetId=sheet_id,
        range=range_name,
        valueInputOption='RAW',
        body=body).execute()

  print(f'Customer data added to spreadsheet. Number of updated cells: { add_result.get("updatedCells") } ')


if __name__ == '__main__':
  
  # authenticate
  authenticate_and_create_service()
  time.sleep(2)


  # create and set sheet name to "customer"
  sheet_id = create_sheet()
  set_sheet_name(sheet_id=sheet_id)

  with app.app_context():
    
    db.create_all()

  # OPTIONAL -- add few records to db  
    # add_customer('bob', 'builder', 'bb@gmail.com')
    # add_customer('sonic', 'hedgehog', 'sh@gmail.com')
    # add_customer('clifford', 'dog', 'cd@gmail.com')

    # retrieve data via db endpoint
    customer_data = get_customers()

    # add data to the google spreadsheet
    add_data_to_sheet(sheet_id=sheet_id, data=customer_data)

    db.session.close()
