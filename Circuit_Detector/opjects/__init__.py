
from .component import Component
from .resistance import Resistance
from .dc_source import DCS
from .inductor import Inductor
from .capacitance import Capac
from .ac_source import ACS
from .ground import Gnd

my_opjects = [Resistance(), DCS(), Gnd()]
#my_opjects = [Resistance(), DCS(), Inductor(), Capac(), ACS(), Gnd()]
NOT_CIR_COMP = [Gnd]