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

        # print(ann.withdraw)
        # print(ann)
        return not ann.withdraw and super()._valid_ann(ann, from_rel)
    
    # def _policy_propagate(
    #     self,
    #     neighbor: "AS",
    #     ann: "Ann",
    #     propagate_to: Rels,
    #     send_rels: set[Rels],
    # ) -> bool:
    #     """If propagating to customers and only_to_customers isn't set, set it"""

    #     if ann.withdraw:
    #         return False
    #     else:
    #         self._process_outgoing_ann(neighbor, ann, propagate_to, send_rels)
    #         return True