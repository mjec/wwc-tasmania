wwc-tasmania
============

Automate Tasmanian working with children check verification

Simply automates submitting data to and parsing responses from
https://wwcforms.justice.tas.gov.au/RegistrationSearch.aspx

Methods
---

`wwctas.card_is_valid(card_number, surname)`

Returns `True` if and only if the card status is Registered. Returns False on
invalid card numbers or mismatching surname.


`wwctas.check_card(card_number, surname)`

Returns a dictionary with two elements:

 * `status` -- the card's status ("Registered")
 * `name`   -- the card owner's full name (as returned, all caps)

Raises InvalidCardException if `card_number` is invalid or does not match `surname`.

Exceptions
----------

`wwctas.InvalidCardException`

Raised by `check_card` if the card number is invalid or does not match the name.
Inherits from `ValueError`.


