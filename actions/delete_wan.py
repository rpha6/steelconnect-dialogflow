import logging

from flask import json
from actions.list_wans import format_wan_list

def delete_wan(api_auth, parameters, contexts):
    """
    :param api_auth: steelconnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from Dialogflow intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """

    wan_name = parameters["WANName"]
    logging.debug("Attempting to delete WAN named: " + wan_name)
    wan_id = None

    # Make sure this WAN exists, and get its ID if it does.
    res = api_auth.list_wans()
    data = res.json()["items"]
    logging.debug("ASDSA")

    if res.status_code == 200:
        for wan in data:
            if wan["name"] == wan_name:
                wan_id = wan["id"]
                break

        if wan_id is None:
            return "Error: The WAN '{}' does not exist. Valid WANs (use the name not in brackets):" + format_wan_list(data)
    else:
        return "Error: Failed to get the list of WANs"

    logging.debug("The WAN ID for '{}' is '{}'".format(wan_name, wan_id))


    # Now delete the WAN!
    res = api_auth.delete_wan(wan_id)
    if res.status_code == 200:
        speech = "Successfully deleted the WAN named '{}'".format(wan_name)
    elif res.status_code == 500:
        # Deletion failed.
        speech = "The WAN could not be deleted."
    else:
        speech = "Error: Other error while attempting to delete the WAN"


    logging.debug(speech)

    return speech

