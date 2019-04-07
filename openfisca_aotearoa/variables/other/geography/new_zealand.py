from openfisca_core.model_api import *
from openfisca_aotearoa.entities import Person

"""
16 New Zealand

(1) New Zealand means—
(a) the North Island, the South Island, Stewart Island, the Chatham Islands,
  and all other land territories, islands, and islets lying
  between the 162nd degree of east longitude and the 173rd degree of west longitude and between the 33rd and 53rd parallels of south latitude; and
(b) those islands situated in the South Pacific Ocean lying between the 177th and 180th degrees of west longitude and between the 29th and 32nd parallels of south latitude, commonly known as the Kermadec Group; and
(c) those parts of the internal waters of New Zealand (as defined by section 4 of the Territorial Sea, Contiguous Zone, and Exclusive Economic Zone Act 1977) adjacent to the land territories, islands, and islets referred to in paragraphs (a) and (b); and
(d) those parts of the territorial sea of New Zealand (as defined by section 3 of the Territorial Sea, Contiguous Zone, and Exclusive Economic Zone Act 1977) adjacent to the land territories, islands, and islets referred to in paragraphs (a) and (b); and
(e) any installation or drilling rig that—
(i) is constructed, erected, placed, or used in, on, or above those parts of the continental shelf adjacent to the land territories, islands, and islets referred to in paragraphs (a) and (b); and
(ii) has the purpose of the exploration of the continental shelf or the exploitation of the mineral or other natural non-living resources of the continental shelf.

(2) In subsection (1)﻿(e),—
(a) continental shelf has the meaning given to it in section 2(1) of the Continental Shelf Act 1964:
(b) installation and drilling rig include—
(i) any installation or drilling rig, whether permanent or temporary:
(ii) any aircraft, floating platform, ship, or other device that is for the time being in, on, or above the continental shelf and is being used in connection with any installation or drilling rig.

(3) A person remains in New Zealand when he or she—
(a) embarks in New Zealand on an aircraft or ship or some other means of conveyance by air or sea—
(i) to travel from one place in New Zealand to another place in New Zealand; or
(ii) to return to his or her place of embarkation without disembarking at any other place; and
(b) does not go beyond a limit of 300 nautical miles from any point or points in New Zealand.
"""


class longitude(Variable):
    value_type = float
    entity = Person
    definition_period = DAY


class latitude(Variable):
    value_type = float
    entity = Person
    definition_period = DAY


class in_the_north_island(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "In the North Island"


class in_the_south_island(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "In the South Island"


class on_stewart_island(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "on Stewart Island"


class in_the_chatham_islands(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "in the Chatham Islands"


class within_the_internal_waters_of_new_zealand(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "within the internal waters of New Zealand"


class within_territorial_sea_of_new_zealand_adjacent(Variable):
    value_type = bool
    entity = Person
    definition_period = DAY
    label = "those parts of the territorial sea of New Zealand (as defined by section 3 of the Territorial Sea, Contiguous Zone, and Exclusive Economic Zone Act 1977) adjacent to the land territories, islands, and islets referred to in paragraphs (a) and (b);"
