from bgpy.enums import Relationships
from bgpy.simulation_engine.policies.bgp import BGPFull
from bgpy.simulation_framework import Scenario


class WithdrawSuppression(BGPFull):
    name: str = "Withdraw Suppression"

    def process_incoming_anns(
        self,
        *,
        from_rel: Relationships,
        propagation_round: int,
        scenario: Scenario,
        reset_q: bool = True,
    ) -> None:
        for prefix, anns in self.recv_q.items():
            self.recv_q[prefix] = [ann for ann in anns if not ann.withdraw]

        return super().process_incoming_anns(
            from_rel=from_rel, propagation_round=propagation_round, scenario=scenario
        )
