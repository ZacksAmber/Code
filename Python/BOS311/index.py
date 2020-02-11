from flask import Flask, render_template, redirect, jsonify, json
import requests
import mysql.connector
import datetime
app = Flask(__name__)


def mysql_login(mysql_host, mysql_user, mysql_passwd, mysql_database):
    global mysql_connect

    mysql_connect = mysql.connector.connect(
        host = mysql_host,
        user = mysql_user,
        passwd = mysql_passwd,
        database = mysql_database
    )

@app.route('/')
def index():
   # return render_template('bot.html')
   # return request.url('https://bosbot-codebuilddeploy-1xzee7iv1czjx-webappbucket-ucqqujsmhtll.s3.amazonaws.com/index.html')
   userInfo()
   return redirect('https://bosbot-codebuilddeploy-1xzee7iv1czjx-webappbucket-ucqqujsmhtll.s3.amazonaws.com/index.html')


@app.route('/zack')
def userInfo():
        try:
            requestParam = {
            "dialogState": "ConfirmIntent",
            "intentName": "ReportIncident_getDetails",
            "message": "okay! incident car parking noted. Our respected authorities are on the way to resolve your issue. do you want status update?",
            "messageFormat": "PlainText",
            "responseAttributes": "null",
            "responseCard": "null",
            "sentimentResponse": "null",
            "sessionAttributes": {},
            "sessionId": "2020-02-07T23:49:44.247Z-HUaNiEmX",
            "slotToElicit": "null",
            "location" : "31 Juliette St  Dorchester  MA  02122",
            "email": "test@mail.com",
            "reason": "Housing"
            }
            response = findDuplicate(requestParam)
            return jsonify(response)
        except Exception as e:
            print(e)
            response_object = {"status": "fail", "message": "unable to Extract Token"}
            return response_object, 500  

@app.route('/')
def findDuplicate(userInfo):
      current_date = datetime.datetime.now().date().isoformat()
      userinfo =case(open_dt=current_date,email=userInfo.get('email'),location=userInfo.get('location'),reason=userInfo.get('reason'))
      print(userinfo)
      main_function()
      
# Define a function to collect case information
def case(open_dt, reason, location, case_status = 'Open', case_title = None,  source = 'ChatBot', email = None, priority = 1):
    global case_information

    try:
        case_information
    except NameError:
        pass
    else:
        case_information.clear()

    case_information = {
    'case_enquiry_id': None,
    'open_dt': open_dt,
    'target_dt': None,
    'closed_dt': None,
    'ontime': None,
    'case_status': case_status,
    'closure_reason': None,
    'case_title': case_title,
    'subject': None,
    'reason': reason,
    'type': None,
    'queue': None,
    'department': None,
    'submittedphoto': None,
    'closedphoto': None,
    'location': location,
    'fire_district': None,
    'pwd_district': None,
    'city_council_district': None,
    'police_district': None,
    'neighborhood': None,
    'neighborhood_services_district': None,
    'ward': None,
    'precinct': None,
    'location_street_name': None,
    'location_zipcode': None,
    'latitude': None,
    'longitude': None,
    'source': source,
    'email': email,
    'priority:': priority
    }
    return case_information

def main_function():
    if judge_duplicate():
        if judge_open(): # Situation 4: Open case
            print("Situation 4: This is a duplicate case. You should UPDATE database!")
            mysql_update()
        else: # Must be Closed case
            if judge_date(): # Situation 3: closed today days
                print("Situation 3: This may not be a new case. You should use AWS Rekognition!")
            else: # Situation 2: closed several days ago
                print("Situation 2: This is a new case. You should INSERT database!")
                mysql_insert()
    else: # Situation 1: NOT duplicate case
        print("Situation 1: This is a new case. You should INSERT database!")
        mysql_insert()

# Define a function to judge if the case is duplicate.
def judge_duplicate():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
    mysql_table,
    case_information['reason'],
    case_information['location']
)

    mysql.execute(sql)
    result = mysql.fetchall()

    if len(result) > 0:
        case_information['priority'] = len(result)
        return(result)
    else:
        case_information['priority'] = 1
        return(result) # it should be an empty list

# Define a function to judge if the case is Open.
def judge_open():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}'".format(
        mysql_table,
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    l = []
    for i in result:
        l.append(i[5]) # extract case_status

    if 'Open' in l:
        return(result)
    else:
        return(None)

# Define a function to judge if the case is created today.
def judge_date():
    sql = "SELECT * FROM {0} WHERE reason = '{1}' AND location = '{2}' AND open_dt LIKE '{3}%'".format(
        mysql_table,
        case_information['reason'],
        case_information['location'],
        case_information['open_dt']
    )

    mysql.execute(sql)
    result = mysql.fetchall()

    l = []
    for i in result:
        l.append(i[1][0:10]) # extract date

    if '2020-01-31' in l: # extract the date part from open_dt. e.g, '2020-01-31 14:35:46' > '2020-01-31'
        return(result)
    else:
        return(None)

    """ Replace it in Prodcution Environment
    if datetime.datetime.now().date().isoformat() in l:
        return(result)
    else:
        return(None)
    """

##########################
# Define MySQL Functions #
##########################

# Define the UPDATE function raise the priority
def mysql_update():
    if case_information['priority'] > 5:
        case_information['priority'] = 5
    else:
        case_information['priority']+= 1

    sql = "UPDATE {0} SET priority = {1} WHERE case_status = 'Open' AND reason = '{2}' AND location = '{3}'".format(
        mysql_table,
        case_information['priority'],
        case_information['reason'],
        case_information['location']
    )

    mysql.execute(sql)
    mysql_connect.commit()
    print(mysql.rowcount, "record(s) affected")

# Define the INSERT function to insert new case
def mysql_insert():
    sql = "INSERT INTO " + mysql_table + " (case_enquiry_id, open_dt, target_dt, closed_dt, ontime, case_status, closure_reason, case_title, subject, reason, type, queue, department, submittedphoto, closedphoto, location, fire_district, pwd_district, city_council_district, police_district, neighborhood, neighborhood_services_district, ward, precinct, location_street_name, location_zipcode, latitude, longitude, source, email, priority) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val = (0, case_information['open_dt'], None, None, None, 'Open', None, case_information['case_title'], None, case_information['reason'], None, None, None, None, None, case_information['location'], None, None, None, None, None, None, None, None, None, None, None, None, case_information['source'], case_information['email'], 1)

    mysql.execute(sql, val)
    mysql_connect.commit()
    print(mysql.rowcount, "record inserted.")



###################
# Set Information #
###################
# Set login information
mysql_login(
    mysql_host = "cloud-analytics-db.crmnbmzm85lc.us-east-1.rds.amazonaws.com",
    mysql_user = "admin",
    mysql_passwd = "Test1234",
    mysql_database = "bosbot"
    )

# Set MySQL cursor
mysql = mysql_connect.cursor()
mysql_table = 'sample311'
# Set MySQL table
# mysql_table = 'test_2020'



if __name__ == '__main__':
   app.run(debug = True)