from frozendict import frozendict

from bgpy.simulation_engine import BGPFull
from bgpy.simulation_framework import ScenarioConfig
from bgpy.tests.engine_tests.utils import EngineTestConfig

from rost.scenarios import WSScenario
from rost.policies import WithdrawSuppression

from .as_graph_info_000 import as_graph_info_000

desc = "Withdraw Suppression"

config_002 = EngineTestConfig(
    name="config_002",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=WSScenario,
        BasePolicyCls=BGPFull,
        num_attackers=0,
        propagation_rounds=2,
        override_attacker_asns=frozenset(),
        hardcoded_asn_cls_dict=frozendict({3: WithdrawSuppression}),
        override_victim_asns=frozenset({4}),
    ),
    as_graph_info=as_graph_info_000,
)
