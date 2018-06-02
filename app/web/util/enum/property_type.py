import enum
from form_enum import FormEnum

class PropertyType(FormEnum):
    TBD = "TBD"
    RESIDENTIAL_MULTI_FAMILY = "Residential Multi-Family (2-4 Units)"
    MEDIUM_MULTI_FAMILY = "Residential Multi-Family (2-4 Units)"
    LARGE_MULTI_FAMILY = "Large Multi-Family (25-50 Units)"
    MULTI_FAMILY_COMPLEX = "Multi-Family Complexes (50-200 Units)"
    SELF_STORAGE = "Self Storage"
    RETAIL = "Retail"

    @classmethod
    def choices(cls):
        print([(choice.value, choice.name) for choice in cls])
        return [(choice, choice.value) for choice in cls]

    @classmethod
    def coerce(cls, item):
        return cls(str(item)) if not isinstance(item, cls) else item

    def __str__(self):
        return str(self.value)
