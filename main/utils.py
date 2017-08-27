import requests
from adhack.settings import GODADDY_KEY, GODADDY_SECRET, GODADDY_API

def check_domain(name):
    """
    r = requests.get(GODADDY_API+name, headers={
                                "Accept": "application/json",
                                "Authorization": "sso-key {}:{}".format(
                                                                        GODADDY_KEY,
                                                                        GODADDY_SECRET
                                                                        )
                                                })
    """
    return True
