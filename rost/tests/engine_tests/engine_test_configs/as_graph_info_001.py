from bgpy.as_graphs import ASGraphInfo
from bgpy.as_graphs.base.links import CustomerProviderLink as CPLink

r"""
Graph:  1   7
        |   |
        2   6
        |   |
        3   5
         \ /
          4
"""


as_graph_info_001 = ASGraphInfo(
    peer_links=frozenset(),
    customer_provider_links=frozenset(
        [
            CPLink(provider_asn=1, customer_asn=2),
            CPLink(provider_asn=2, customer_asn=3),
            CPLink(provider_asn=3, customer_asn=4),
            CPLink(provider_asn=5, customer_asn=4),
            CPLink(provider_asn=6, customer_asn=5),
            CPLink(provider_asn=7, customer_asn=6),
        ]
    ),
)
