import logging

from flask import json

def list_uplinks_followup(api_auth, parameters):
    """
    :param api_auth: steelconnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from Dialogflow intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """

    # Get all uplinks and return a response based on the number of uplinks
    res = api_auth.list_uplinks()

    if res.status_code == 200:
        data = res.json()["items"]
        num_uplinks = len(data)

        if parameters:
            try:
                number = int(parameters["number"])
                position = parameters["position"]
            except KeyError as e:
                logging.error("Error processing list_uplinks_followup intent. {0}".format(e))

                return "There was an error fulfilling your request"
        else:
            number = num_uplinks
            position = "all"

        speech = ""

        if number > num_uplinks:
            number = num_uplinks

        if position == "first":
            data = data[:number]
        elif position == "last":
            data = data[-number:]
        elif position == "all":
            pass
        else:
            logging.error("Error processing list_uplinks_followup intent. Unrecognised positon: {}".format(position))
            return "There was an error fulfilling your request"

        for uplink in data:
            site = uplink["site"].split("-")[1]
            name = uplink["name"]
            wan = uplink["wan"].split("-")[1]
            
            speech += ", {}/{}/{}".format(site, name, wan)

        speech = speech[2:] + "."

    else:
        speech = "Error: Could not connect to SteelConnect"

    logging.debug(speech)

    return speech
