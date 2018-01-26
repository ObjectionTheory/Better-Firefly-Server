import json

def processRequest(req):
    
    print(json.dumps(req, indent=4))
    
    if req.get("result").get("action") == "task_number":
        res = taskNumber(req)
    elif req.get("result").get("action") == "testeroo":
        speech = "A great testeroo!"
        return {
            "speech": speech,
            "displayText": speech,
            "source": "webhookdata"
        }
    else:
        speech = "Oops. Something wrong happened..."
        return {
            "speech": speech,
            "displayText": speech,
            "source": "webhookdata"
        }

    return res


def taskNumber(data):
    print("breakAuth?")
    element = data.get("result").get("parameters").get("elementname")
    #taskList = tasks.get_tasks(auth)
    print("break2")
    speech = 'You have ' #+ str(len(taskList)) + ' tasks.'
    print (speech)
    return {
        "speech": speech,
        "displayText": speech,
        "source": "webhookdata"
    }
  
