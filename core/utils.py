"""
General utilitaries
"""
from random import choice


# this logic was originally writen by limebrains: https://github.com/limebrains/scrapper-helpers/blob/master/scrapper_helpers/utils.py#L121
# im using the code alone because the virtualenv doesnt recognized the "scrapper_helpers" installation ¯\_(ツ)_/¯
USER_AGENTS = [
    'Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    '42.0.2311.135 Safari/537.36 Edge/12.246',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/'
    '9.0.2 Safari/601.3.9',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:15.0) Gecko/20100101 Firefox/15.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36'
]


def get_random_user_agent():
    """ Randoms user agent to prevent "python" user agent
    :return: Random user agent from USER_AGENTS
    :rtype: str
    """
    return choice(USER_AGENTS)
