"""
"""

import requests


SESSION = None
BASE_URL = "https://hubski.com"


def _init_session():
    """
    Initializes a requests session.
    """
    global SESSION

    if SESSION is None:
        SESSION = requests.Session()


def login(username, password):
    """
    Logins in to a Hubski account. Not yet implemented.

    Parameters
    ----------
    username : str
    password : str
    """
    raise NotImplemented
    _init_session()

    # Get the fnid, required to POST our information
    get_url = "{}/hubskilogin".format(BASE_URL)

    get_r = SESSION.get(get_url)
    fnid = None

    # POST the username / password to the server
    post_url = "{}/y".format(BASE_URL)

    post_r = SESSION.post(
        post_url,
        {
            "fnid": fnid,
            "u": username,
            "p": password,
        }
    )

    if r.status_code != 200 or r.url != "{}/".format(BASE_URL):
        raise Exception("Unable to log in!") # XXX: Full message?

def list_publications():
    """
    Lists all publications on Hubski.

    Returns
    -------
    list of int
    """
    _init_session()

    url = "{}/api/publications".format(BASE_URL)
    r = SESSION.get(url)
    json = r.json()

    return json


def get_publication(id):
    """
    Gets information associated with a particular post or comment.

    Parameters
    ----------
    id : str or int

    Returns
    -------
    dict
        JSON dict of publication.
    """
    _init_session()

    url = "{}/api/publication/{}".format(BASE_URL, id)
    r = SESSION.get(url)
    json = r.json()

    return json


def get_publication_full(id):
    """
    Retrieves a post and all of its children in one call.

    Parameters
    ----------
    id : str or int

    Returns
    -------
    dict
        JSON dict of publication and its comment.
    """

    _init_session()

    url = "{}/api/publication/{}/tree".format(BASE_URL, id)
    r = SESSION.get(url)
    json = r.json()

    return json


def list_endpoints():
    """
    Lists REST API endpoints.

    Returns
    -------
    list of str
    """
    _init_session()

    url = "{}/api/".format(BASE_URL)
    r = SESSION.get(url)
    json = r.json()

    return json["endpoints"]
