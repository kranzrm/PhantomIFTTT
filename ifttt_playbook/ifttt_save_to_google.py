import phantom.rules as phantom
import json

def save_to_google_drive_cb(action, success, container, results, handle):

    if not success:
        return

    return


def on_start(container):

    pass

    return

def on_finish(container, summary):

    # This function is called after all actions are completed.
    # Summary and/or action results can be collected here.

    parameters = []
    parameters.append({
        "value3": "label: {label}, name: {name}, creatiion_time: {create_time}, owner: {owner}, status: {status}".format(**container),
        "value2": container['severity'],
        "value1": container['id']
    })

    phantom.act("save to google drive", parameters=parameters, assets=["maker_channel"]) # callback=save_to_google_drive_cb

    return
