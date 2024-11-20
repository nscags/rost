from typing import TYPE_CHECKING, Optional
from copy import deepcopy

from bgpy.shared.enums import Prefixes, Relationships, Timestamps, SpecialPercentAdoptions
from bgpy.simulation_framework.scenarios.scenario import Scenario

if TYPE_CHECKING:
    from bgpy.simulation_engine import Announcement as Ann
    from bgpy.simulation_engine import BaseSimulationEngine

class WSScenario(Scenario): 

    min_propagation_rounds: int = 2

    def _get_announcements(
        self,
        *,
        engine: Optional["BaseSimulationEngine"] = None,
    ) -> tuple["Ann", ...]:
        """
        """

        anns = list()
        for victim_asn in self.victim_asns:
            anns.append(
                self.scenario_config.AnnCls(
                    prefix=Prefixes.PREFIX.value,
                    next_hop_asn=victim_asn,
                    as_path=(victim_asn,),
                    timestamp=Timestamps.VICTIM.value,
                    seed_asn=victim_asn,
                    recv_relationship=Relationships.ORIGIN,
                )
            )
            
        return tuple(anns)
    
    def post_propagation_hook(self, engine=None, propagation_round=0, *args, **kwargs):  # type: ignore
        """Useful hook for post propagation"""

        if propagation_round == 0:
            ann = deepcopy(
                engine.as_graph.as_dict[4].policy.local_rib.get(Prefixes.PREFIX.value)
            )
            object.__setattr__(ann, "withdraw", True)

            engine.as_graph.as_dict[4].policy.local_rib.pop(Prefixes.PREFIX.value, None)
            engine.as_graph.as_dict[4].policy.ribs_out.remove_entry(
                3, Prefixes.PREFIX.value
            )
            engine.as_graph.as_dict[4].policy.send_q.add_ann(3, ann)