# IFTTT - Maker Channel connector for Phantom

This App for [Phantom security orchestrator](https://www.phantom.us/product.html) provides integration with IFTTT automation


<img src="https://github.com/kranzrm/PhantomIFTTT/wiki/images/ifttt-phantom.png" width="400">

## Suggested Use-Cases

This app can be used to integrate automations with all the offerings of If-This-Then-That (IFTTT)

For Example:

*   Send an SMS message when playbook actions are complete on a container [Phantom Cyber - SMS Alert](https://ifttt.com/recipes/428641-phantom-cyber-sms-alert)
*   Save Container/Incident details to a Google Drive spreadsheet [Phantom/IFTTT Google Drive Recipe](https://ifttt.com/recipes/428980-save-phantom-incident-details-to-google-drive-spreadsheet)

## Current Actions

* `trigger ifttt action` - Trigger an arbitrary action via the IFTTT Maker Channel
* `send message` - Send and SMS Message [Phantom/IFTTT SMS Recipe)](https://ifttt.com/recipes/428641-phantom-cyber-sms-alert)
* `save to google drive` - Send container details to a Google Drive Spreadsheet [Phantom/IFTTT Google Drive Recipe](https://ifttt.com/recipes/428980-save-phantom-incident-details-to-google-drive-spreadsheet)

## Future Features

* Turn Philips Hue LED red when executing playbooks

## Setup

> See the [Wiki](https://github.com/kranzrm/PhantomIFTTT/wiki) for more detailed setup instructions.

1. Download the latest [Phantom](https://www.phantom.us/product.html) virtual appliance from Phantom Cyber.
2. Select "Import App" from the *Administration / Apps* tab.
   * Select the `ifttt.tgz` file
   * Check "Replace an Existing app" if an older version is installed
3. Create an IFTTT Account ([https://ifttt.com/join](IFTTT Sign-Up Page))
4. Obtain a free API key from the [https://ifttt.com/maker](Maker Channel)
5. Configure the IFTTT asset.  
   * Product Vendor = "IFTTT"
   * Product Name  = "IFTTT - Maker Channel"
   * Set the "Maker Channel API Key" field in the phantom "Asset Settings" tab
6. Configure any channels you want to use (on IFTTT)
7. (Optional) Configure the `api_key` and `asset_id` in the json files located in the `test_json` directory (for CLI debugging)

## References

*   Phantom Cyber Product Page [https://www.phantom.us/product.html](https://www.phantom.us/product.html)
*   PhantomIFTTT [Wiki](https://github.com/kranzrm/PhantomIFTTT/wiki)
*   IFTT - If This Then That Website [https://ifttt.com/maker](https://ifttt.com/maker)
*   IFTT - Maker Channel [https://ifttt.com/maker](https://ifttt.com/maker)
*   IFTT - SMS Channel [https://ifttt.com/sms](https://ifttt.com/sms)
*   IFTT - Google Drive Channel [https://ifttt.com/google_drive](https://ifttt.com/google_drive)
