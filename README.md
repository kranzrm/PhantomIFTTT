# IFTTT - Maker Channel connector for Phantom

This App for [Phantom security orchestrator](https://www.phantom.us/product.html) provides integration with IFTTT automation


## Suggested Use-Cases

This app can be used to integrate automations with all the offerings of If-This-Then-That (IFTTT)

For Example:

*   Send an SMS message when playbook actions are complete on a container [Phantom Cyber - SMS Alert](https://ifttt.com/recipes/428641-phantom-cyber-sms-alert)

## Current Actions

* `trigger ifttt action` - Trigger an arbitrary action in the IFTTT Maker Channel

## Future Features


## Setup

1. Download a [Phantom](https://www.phantom.us/product.html) appliance from Phantom Cyber.
2. Select "Import App" from the *Administration / Apps* tab.
   * Select the `ifttt.tgz` file
   * Check "Replace an Existing app" if an older version is installed
3. Obtain an API key from 
4. Configure the IFTTT asset.  
   * Product Vendor = "IFTTT"
   * Product Name  = "IFTTT - Maker Channel"
   * Set the "Maker Channel API Key" field in the phantom "Asset Settings" tab
5. Configure the `api_key` and `asset_id` in the json files located in the `test_json` directory (for CLI debugging)

## References

*   Phantom Cyber Product Page [https://www.phantom.us/product.html](https://www.phantom.us/product.html)
*   Phantom Cyber Product Page [https://www.phantom.us/product.html](https://www.phantom.us/product.html)
