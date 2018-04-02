import logging

from flask import json

def list_wans(api_auth, parameters, contexts):
    """
    :param api_auth: steelconnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from Dialogflow intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """

    logging.info("Listing WANs")

    res = api_auth.list_wans()

    if res.status_code == 200:
        data = res.json()["items"]

        speech = "All the WANs in your organisation:" + format_wan_list(data)

    else:
        speech = "Error: Could not connect to SteelConnect"

    logging.debug(speech)

    return speech

def format_wan_list(items):
    s = ""

    for wan in items:
        if wan["longname"] is not None:
            s += "\n - " + str(wan["name"]) + " (" + wan["longname"] + ")"
        else:
            s += "\n - " + str(wan["name"])

    return s
