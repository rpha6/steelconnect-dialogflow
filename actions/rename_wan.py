import logging

from flask import json

def rename_wan(api_auth, parameters, contexts):
    """
    Changes the short name of a WAN.

    :param api_auth: steelconnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from Dialogflow intent
    :type parameters: json
    :param contexts: json contexts from Dialogflow intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """

    original_name = parameters["OriginalName"]
    new_name = parameters["NewName"]

    res = api_auth.update_wan()

    if res.status_code == 200:
        speech = "{} created".format(WAN_type)
    elif res.status_code == 400:
        speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
    elif res.status_code == 500:
        speech = "Error: Could not create WAN"
    else:
        speech = "Error: Could not connect to SteelConnect"

    logging.debug(speech)

    return speech

