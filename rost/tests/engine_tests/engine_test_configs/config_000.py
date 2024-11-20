from bgpy.simulation_engine import BGPFull
from bgpy.simulation_framework import ScenarioConfig, ValidPrefix
from bgpy.tests.engine_tests.utils import EngineTestConfig

from .as_graph_info_000 import as_graph_info_000

desc = "Normal Propagation"

config_000 = EngineTestConfig(
    name="config_000",
    desc=desc,
    scenario_config=ScenarioConfig(
        ScenarioCls=ValidPrefix,
        BasePolicyCls=BGPFull,
        num_attackers=0,
        override_attacker_asns=frozenset(),
        override_victim_asns=frozenset({4}),
    ),
    as_graph_info=as_graph_info_000,
)
