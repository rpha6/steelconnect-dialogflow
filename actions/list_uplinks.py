import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests

def list_uplinks(api_auth, parameters):
    """
    :param parameters: json parameters from Dialogflow intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    
    # Get org name from Entitities
    org = parameters["organisation"]

    # Get all uplinks and return a response based on the number of uplinks
    res = api_auth.list_uplinks()

    if res.status_code == 200:
        data = res.json()["items"]
        num_uplinks = len(data)

        if num_uplinks == 0:
            speech = "There are no uplinks in the {} organisation".format(org)
        elif num_uplinks == 1:
            speech = "There is one uplink in the {} organisation, it is called {}".format(org, data[0]["name"])
        elif num_uplinks > 1:
            speech = "There are {} uplinks in the {} organisation, would you like to list all of them?".format(
                num_uplinks, org)
        else:
            speech = "Unknown error occurred when retrieving uplinks"
    else:
        speech = "Error: Could not connect to SteelConnect"

    logging.debug(speech)

    return speech