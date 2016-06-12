import phantom.rules as phantom
import json

def send_message_cb(action, success, container, results, handle):

    if not success:
        return

    return


def on_start(container):

    pass

    return

def on_finish(container, summary):

    parameters = []
    parameters.append({
        "message": "%s - %s" % (container['severity'], container['description']) ,
        "message_title": container['name']
    })

    # Send an SMS message (Configured on the IFTTT SMS Channel) 
    phantom.act("send message", parameters=parameters, assets=["maker_channel"]) # callback=send_message_cb

    return
