from typing import TYPE_CHECKING

from bgpy.shared.enums import Relationships as Rels
from bgpy.simulation_engine.policies.bgp import BGPFull

if TYPE_CHECKING:
    from bgpy.as_graphs import AS
    from bgpy.simulation_engine import Announcement as Ann


class WithdrawSuppression(BGPFull):
    name: str = "Withdraw Suppression"

    def _valid_ann(self, ann: "Ann", from_rel: Rels) -> bool:
        """returns false if announcement is a withdrawal"""

        return not ann.withdraw and super()._valid_ann(ann, from_rel)
