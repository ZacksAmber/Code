from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#    return render_template('botUI.html')

@app.route('/')
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
            "slots": {
            "Location": "12 smith street 02115",
            "email": "test@mail.com",
            "reason": "illegal car parking"
            }
            }
            response = findDuplicate(requestParam)
            return response
        except Exception as e:
            print(e)
            response_object = {"status": "fail", "message": "unable to Extract Token"}
            return response_object, 500   

def findDuplicate(userdetails):
  
    return userdetails

if __name__ == '__main__':
   app.run()