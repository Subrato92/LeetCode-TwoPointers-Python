import enum
from . import ArrangeChar
from . import ThreeSumClosest
from . import FourSum
from . import RemoveDuplicatesFromSortedArray
from . import TrappingRainWater

class Factory(enum.Enum):
    ARRANGE_CHAR = ArrangeChar.Problem
    THREE_SUM_CLOSEST = ThreeSumClosest.Problem
    FOUR_SUM = FourSum.Problem
    REMOVE_DUP_FRM_SORTED_ARRAY = RemoveDuplicatesFromSortedArray.Problem
    TOTAL_TRAPPED_RAINWATER = TrappingRainWater.Problem