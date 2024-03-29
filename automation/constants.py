from web3 import Web3

ARB_CHAIN_ID = 42161
BALANCER_GAUGE_URL = (
    "https://api.thegraph.com/subgraphs/name/balancer-labs/balancer-gauges"
)
BALANCER_GRAPH_URL = (
    "https://api.thegraph.com/subgraphs/name/balancer-labs/balancer-arbitrum-v2"
)
BALANCER_GAUGE_CONTROLLER_ADDR = "0xC128468b7Ce63eA702C1f104D55A2566b13D3ABD"
BALANCER_GAUGE_CONTROLLER_ABI = [
    {
        "stateMutability": "view",
        "type": "function",
        "name": "gauge_relative_weight",
        "inputs": [{"name": "addr", "type": "address"}],
        "outputs": [{"name": "", "type": "uint256"}],
    },
    {
        "stateMutability": "view",
        "type": "function",
        "name": "gauge_relative_weight",
        "inputs": [
            {"name": "addr", "type": "address"},
            {"name": "time", "type": "uint256"},
        ],
        "outputs": [{"name": "", "type": "uint256"}],
    },
]

# Query to fetch pool snapshots
POOLS_SNAPSHOTS_QUERY = """
{{
  poolSnapshots(
    first: {first}
    skip: {skip}
    orderBy: timestamp
    orderDirection: desc
    where: {{timestamp_gte: {start_ts}, timestamp_lt: {end_ts}}}
  ) {{
    pool {{
      address
      id
      symbol
    }}
    timestamp
    protocolFee
    swapFees
    swapVolume
    liquidity
  }}
}}
"""

CURRENT_YEAR = 2023

ARBITRUM_BONUS = 10000.0
ARBITRUM_TOTAL = 82285.3

DYNAMIC_BOOST_MULTIPLIER = 3
MIN_BAL_IN_USD_FOR_BOOST = 200
ARBITRUM_TO_DISTRIBUTE = ARBITRUM_TOTAL - ARBITRUM_BONUS  # 100k weekly - bonus

VOTE_CAP_IN_PERCENT = 10  # 10% cap on any single gauge
ARB_GAUGE_WITH_BONUS = Web3.to_checksum_address(
    "0xa14453084318277b11d38FbE05D857A4f647442B"
)
ARB_ROOT_GAUGE = Web3.to_checksum_address("0xBb1a15dfd849bc5a6F33C002999c8953aFA626Ad")

# gauge: poolAddress
GAUGES_WITH_BONUSES = {
    Web3.to_checksum_address("0x62A82FE26E21a8807599374CaC8024fae342eF83"): {
        "recipientGauge": Web3.to_checksum_address(
            "0x050fBe33699E56B577c3D6f090eCE9870A0966bd"
        ),
        "poolAddress": "0x2ce4457acac29da4736ae6f5cd9f583a6b335c27",
        "symbol": "sFRAX-4POOL",
        "bonus": 10000.0,
    },
}
