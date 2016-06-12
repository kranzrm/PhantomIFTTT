# -----------------------------------------
# IFTTT Maker Channel Integration APP
# -----------------------------------------

# Phantom App imports
import phantom.app as phantom

from phantom.base_connector import BaseConnector
from phantom.action_result import ActionResult

# Imports local to this App
from ifttt_consts import *

import simplejson as json
import requests

requests.packages.urllib3.disable_warnings()


# Define the App Class
class IFTTTConnector(BaseConnector):

    # ACTION_ID_TRIGGER_ACTION = "trigger_ifttt_action"

    def __init__(self):

        super(IFTTTConnector, self).__init__()

    def _trigger_action(self, event_name, result, value1="", value2="", value3=""):

        config = self.get_config()

        # Get the API Key, it's marked as required in the json, so the platform/BaseConnector will fail if
        # not found in the input asset config
        api_key = config[IFTTT_JSON_APIKEY]

        url = IFTTT_MAKER_BASE_URL.format(event_name, api_key)

        params = {'value1': value1, 'value2': value2, 'value3': value3}
        try:
            r = requests.post(url, params=params)
        except Exception as e:
            return (result.set_status(phantom.APP_ERROR, IFTTT_ERR_SERVER_CONNECTION, e), None)

        # The result object can be either self (i.e. BaseConnector) or ActionResult
        if (hasattr(result, 'add_debug_data')):
            result.add_debug_data({'r_text': r.text if r else 'r is None'})

        # If successfull ifttt returns a string starting with "Congratulations"
        if 'Congratulations' in r.text:
            return (phantom.APP_SUCCESS, r.text)

        # Maker Channel gives back a json in case of error
        try:
            resp = r.json()
            return (result.set_status(phantom.APP_ERROR, resp['errors']), resp)
        except Exception as e:
            pass

        # Usually should not come here _and_ has encountered an HTTP error, but still look for errors
        if (r.status_code != requests.codes.ok):  # pylint: disable=E1101
            return (result.set_status(phantom.APP_ERROR, "Api Call returned error, status_code: {0}, data: {1}".format(r.status_code, r.text)), r.text)

        # Must have been an unknown error
        return (result.set_status(phantom.APP_ERROR, resp.text), resp)

    def _test_connectivity(self, param):
        self.save_progress("Testing IFTTT API Key")
        ret_val, resp = self._trigger_action('test_api_key', self)

        if (not ret_val):
            self.append_to_message(IFTTT_ERR_API_TEST)
            return self.get_status()

        self.append_to_message(IFTTT_ERR_API_TEST)
        self.save_progress(resp)
        return self.set_status_save_progress(phantom.APP_SUCCESS, IFTTT_SUCC_API_TEST)

    def _handle_trigger_action(self, param):
        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Setup Parameters
        ifttt_action = param['action']

        self.save_progress("Triggering Action")
        ret_val, response = self._trigger_action(ifttt_action, action_result,
            param.get('value1', ''), param.get('value2', ''), param.get('value3', ''))

        if (not ret_val):
            return action_result.get_status()

        if (not response):
            # There was an error, no results
            action_result.append_to_message(IFTTT_ERR_TRIGGER)
            return action_result.get_status()

        action_result.set_status(phantom.APP_SUCCESS, "Successfull")
        return self.set_status_save_progress(phantom.APP_SUCCESS, "Action Successfull")

    def _handle_send_message(self, param):
        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Setup Parameters
        self.save_progress("Triggering Action")
        ret_val, response = self._trigger_action('send_sms_message', action_result,
            param.get('message_title', ''), param.get('message', ''), param.get('value3', ''))

        if (not ret_val):
            return action_result.get_status()

        if (not response):
            # There was an error, no results
            action_result.append_to_message(IFTTT_ERR_TRIGGER)
            return action_result.get_status()

        action_result.set_status(phantom.APP_SUCCESS, "Successfull")
        return self.set_status_save_progress(phantom.APP_SUCCESS, "Action Successfull")

    def _handle_save_to_google_drive(self, param):
        # Add an action result to the App Run
        action_result = self.add_action_result(ActionResult(dict(param)))

        # Setup Parameters
        self.save_progress("Triggering Action")
        ret_val, response = self._trigger_action('save_to_google_drive', action_result,
            param.get('value1', ''), param.get('value2', ''), param.get('value3', ''))

        if (not ret_val):
            return action_result.get_status()

        if (not response):
            # There was an error, no results
            action_result.append_to_message(IFTTT_ERR_TRIGGER)
            return action_result.get_status()

        action_result.set_status(phantom.APP_SUCCESS, "Successfull")
        return self.set_status_save_progress(phantom.APP_SUCCESS, "Action Successfull")

    def handle_action(self, param):
        ret_val = phantom.APP_SUCCESS

        # Get the action that we are supposed to execute for this App Run
        action_id = self.get_action_identifier()
        self.debug_print("action_id", self.get_action_identifier())

        if (action_id == ACTION_ID_TRIGGER_ACTION):
            ret_val = self._handle_trigger_action(param)
        elif (action_id == ACTION_ID_SEND_MESSAGE):
            ret_val = self._handle_send_message(param)
        elif (action_id == ACTION_ID_SAVE_TO_DRIVE):
            ret_val = self._handle_save_to_google_drive(param)
        elif (action_id == phantom.ACTION_ID_TEST_ASSET_CONNECTIVITY):
            ret_val = self._test_connectivity(param)

        return ret_val

if __name__ == '__main__':

    import sys
    # import pudb
#    pudb.set_trace()

    if (len(sys.argv) < 2):
        print "No test json specified as input"
        exit(0)

    with open(sys.argv[1]) as f:
        in_json = f.read()
        in_json = json.loads(in_json)
        print(json.dumps(in_json, indent=4))

        connector = IFTTTConnector()
        connector.print_progress_message = True
        ret_val = connector._handle_action(json.dumps(in_json), None)
        print (json.dumps(json.loads(ret_val), indent=4))

    exit(0)
