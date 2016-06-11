import phantom.rules as phantom
import json

def trigger_ifttt_action_cb(action, success, container, results, handle):

    if not success:
        return

    return


def on_start(container):

    pass
    return

def on_finish(container, summary):

    parameters = []

    parameters.append({
        "action": "send_sms_to_soc_mgr",
        "value3": container['status'],      # open/closed/new
        "value2": container['severity'],    # Severity
        "value1": container['name'],        # Name
    })

    phantom.act("trigger ifttt action", parameters=parameters, assets=["maker_channel"])
    # callback=trigger_ifttt_action_cb

    # This function is called after all actions are completed.
    # Summary and/or action results can be collected here.

    # summary_json = phantom.get_summary()
    # summary_results = summary_json['result']
    # for result in summary_results:
            # action_run_id = result['id']
            # action_results = phantom.get_action_results(action_run_id=action_run_id)
    return

