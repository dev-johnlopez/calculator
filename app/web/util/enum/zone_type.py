import enum
from form_enum import FormEnum

class ZoneType(FormEnum):
    POSTAL_CODE = "Postal Code"
    STATE_CODE = "State Code"
    COUNTY_NAME = "County"
