import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests

org = "Monash"

def list_sites(parameters):
    """
    :param parameters: json parameters from API.AI intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """
    # Get all sites and return a response based on the number of sites
    res = requests.get("https://monash.riverbed.cc/api/scm.config/1.0/org/org-Monash-d388075e40cf1bfd/sites",
                       auth=HTTPBasicAuth("Finn", "Kalapuikot"))
    data = res.json()

    num_sites = len(data)
    speech = ""

    if res.status_code == 200:
        if num_sites == 0:
            speech = "There are no sites in the {} organisation".format(org)
        elif num_sites == 1:
            speech = "There is one site in the {} organisation, it is called {}".format(org, data[0]["name"])
        elif num_sites > 1:
            speech = "There are {} sites in the {} organisation, would you like to list all of them?".format(
                num_sites, org)
        else:
            speech = "Unknown error occurred when retrieving sites"
    else:
        speech = "Error: Could not connect to Steelconnect"

    logging.debug(speech)

    return speech