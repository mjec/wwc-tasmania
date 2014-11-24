wwc-tasmania
============

Automate Tasmanian working with children check verification

Simply automates submitting data to and parsing responses from
https://wwcforms.justice.tas.gov.au/RegistrationSearch.aspx

Depends on [requests](http://python-requests.org/) and [lxml](http://lxml.de/).

Methods
-------

`wwctas.card_is_valid(card_number, surname)`

Returns `True` if and only if the card status is Registered. Returns `False` on
invalid card numbers or mismatching surname.

Note that there may be values other than Registered which should return True in
some circumstances (e.g. a conditional registration). This is currently not
supported.


`wwctas.check_card(card_number, surname)`

Returns a dictionary with two elements:

 * `status` -- the card's status ("Registered" if valid; other potential values unknown)
 * `name`   -- the card owner's full name (as returned, all caps)

Raises InvalidCardException if `card_number` is invalid or does not match `surname`.

Exceptions
----------

`wwctas.InvalidCardException`

Raised by `check_card()` if the card number is invalid or does not match the name.
Inherits from `ValueError`.

Todo
----

 * Figure out other possible statuses (let me know if you get one!)
 * More graceful error requests handling
 * Maybe do some data cleaning
 * Expand to other jurisdictions:
    * VIC: https://online.justice.vic.gov.au/wwccu/checkstatus.doj
    * WA:  http://www.checkwwc.wa.gov.au/checkwwc/Pages/ValidateCard.aspx?ValidateNo=Enter%20Card%20Number
    * NT:  https://forms.pfes.nt.gov.au/safent/CheckValidity.aspx?IsValidityCheck=true
    * NSW: https://wwccheck.ccyp.nsw.gov.au/Verifiers/Search (see also http://www.kidsguardian.nsw.gov.au/Working-with-children/Working-With-Children-Check/apply/apply)
    * QLD: https://www.bluecard.qld.gov.au/onlinevalidation/validation.aspx
    * ACT: (no online validation)
    * SA:  (no online validation)
