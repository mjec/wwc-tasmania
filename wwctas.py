import requests
from lxml import html

WWCURL = 'https://wwcforms.justice.tas.gov.au/RegistrationSearch.aspx'

class InvalidCardException(ValueError):
    pass

def card_is_valid(card_number, surname):
    """Returns True if the card status is 'Registered' or False otherwise"""

    try:
        return ('Registered' == check_card(card_number, surname)['status'])
    except InvalidCardException:
        return False
    
def check_card(card_number, surname):
    """Returns a dictionary with two elements:
            status  --  the card's status ("Registered" if current)
            name    --  the card owner's full name

        Raises an InvalidCardExceptionException if card_number is invalid
        or the does not match surname."""

    session = requests.Session()
    page = session.get(WWCURL)
    tree = html.fromstring(page.text)
    inputs = tree.xpath('//input')
    post_to = tree.xpath('//form')[0].attrib['action']

    payload = {}

    for i in inputs:
        if 'value' in i.attrib:
            payload[i.attrib['name']] = i.attrib['value']
        else:
            payload[i.attrib['name']] = ''

    payload['ctl00$MainContent$txtCardNumber'] = card_number
    payload['ctl00$MainContent$txtSurname'] = surname

    resp = session.post(WWCURL, data=payload, headers={'User-Agent': 'Automated WWC checker/0.1 (see http://mjec.net/ for contact details)'})

    tree = html.fromstring(resp.text)

    error_t1 = tree.xpath("//span[@id='ctl00_MainContent_lblSearchResult']")    # Incorrect name
    error_t2 = tree.xpath("//td[@class='Paging']/ul/li")                        # Invalid card number

    if len(error_t1) > 0:
        raise InvalidCardException(error_t1[0].text)
    elif len(error_t2) > 0:
        raise InvalidCardException(error_t2[0].text)
    else:
        return {
            'name': tree.xpath("//span[@id='ctl00_MainContent_lblClientFullName']")[0].text,
            'status': tree.xpath("//span[@id='ctl00_MainContent_lblRegistrationStatus']")[0].text
        }
