from openfisca_core.model_api import *
# Import the entities specifically defined for this tax and benefit system
from openfisca_aotearoa.entities import Person


class TypesPartnershipStatus(Enum):
    __order__ = 'not_specified never married civil_union dissolved separated de_facto surviver'  # Needed to preserve the enum order in Python 2
    not_specified = u'Not specified'
    never = 'Never married and never in a civil union'
    married = u'Marriage'
    civil_union = u'Civil Union'
    dissolved = u'Dissolved marriage or civil union, in the case of marriage, also known as divorced'
    separated = u'Separated (in both marriage and civil unions)'
    de_facto = u'De facto'
    surviver = u'Widower, widow, surviving civil union partner'


class partnership_status(Variable):
    value_type = Enum
    possible_values = TypesPartnershipStatus  # defined in model/base.py
    default_value = TypesPartnershipStatus.Not
    entity = Person
    label = u"Partnership status"
    definition_period = MONTH
    set_input = set_input_dispatch_by_period