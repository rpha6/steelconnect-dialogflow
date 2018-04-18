import logging

from flask import json
from requests.auth import HTTPBasicAuth
import requests

def rename_site(api_auth, parameters):
    """
    :param api_auth: steelconnect api object
    :type api_auth: SteelConnectAPI
    :param parameters: json parameters from Dialogflow intent
    :type parameters: json
    :return: Returns a response to be read out to user
    :rtype: string
    """

    # Context doesn't actually need to be checked here, just left as an example
    # context = None
    # for item in parameters["results"]["contexts"]:
    #     if item["name"] == "listsites-followup":
    #         context = item
    #         break                                       # break once correct context is found
    #
    # if not context:
    #     logging.error("Error listsites-followup context not found")
    #     return "There was an error fulfilling your request"
    # else:
    #     pass



    # Get all sites and return a response based on the number of sites
    
    try:
        old_name = parameters["OldName"]
        new_name = parameters["NewName"]
        city = parameters["City"]

        # in case city consists of multiple words, strip the whitespace(s) as SCM doesn't allow it.
        # city_clean = city.replace(" ", "")
        country_code = parameters["Country"]["alpha-2"]
        country_name = parameters["Country"]["name"]
        
    except KeyError as e:

        error_string = "Error processing createSite intent. {0}".format(e)

        logging.error(error_string)

        return error_string

    res = api_auth.list_sites()

    if res.status_code == 200:
        data = res.json()["items"]
        num_sites = len(data)
        site_id = "blank"
        speech = "bs"
        for site in data:
            if site["name"] == old_name:
                speech = "{}".format(old_name)
                if site["city"] == city and site["country"] == country_code:
                    # long_name = site["longname"]
                    site_id = site["id"]
                    speech = "{}".format(site_id)
                    break

        res2 = api_auth.rename_site(site_id, new_name, new_name, city)

        if res2.status_code == 200:
            data = res2.json()
            # speech = "name: {}".format(data["name"])
            speech = "Site {} has been successfully renamed to {}".format(old_name, new_name)
        elif res2.status_code == 400:
            # speech = res2.json()
            speech = "Invalid parameters: {}".format(res2.json()["error"]["message"])
        elif res2.status_code == 500:
            speech = "Invalid parameters: {}".format(res2.json()["error"]["message"])
        else:
            speech = "id: {} status: {}".format(site_id, res2.status_code)
            # speech = "oname:{} nname:{} city:{} ct:{} siteid: {}".format(old_name, new_name, city, country_code, site_id)
            # speech = "got in"

            # speech = "{} created in {}, {}".format(site_type.capitalize(), city, country_name)
    elif res.status_code == 400:
        speech = "Invalid parameters: {}".format(res.json()["error"]["message"])
    elif res.status_code == 500:
        speech = "Error: Could not create site"
    else:
        speech = "Error: Could not connect to SteelConnect"



    logging.debug(speech)

    return speech