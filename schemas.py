from datetime import timezone as dt_timezone
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    status: str = Field(default='healthy', description='Service health status')
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='UTC timestamp')

class ToolItem(BaseModel):
    name: str = Field(default='', description='Tool name')
    description: str = Field(default='', description='Tool description')
    input_schema: Dict[str, Any] = Field(default_factory=dict, description='JSON schema for tool input')

class ToolsResponse(BaseModel):
    tools: List[Dict[str, Any]] = Field(default_factory=list, description='List of available agent tools')

class InternetStateRequest(BaseModel):
    target_identifier: str = Field(default='global_internet', description='Target scope or identifier')
    query_parameter: str = Field(default='full_state_analysis', description='Specific analytical sub-query')
    lat: float = Field(default=2.27, description='Latitude coordinate clamped to [-90, 90]')
    lon: float = Field(default=102.55, description='Longitude coordinate clamped to [-180, 180]')
    window_steps: int = Field(default=24, description='Lookback window steps in hours')
    resolution: int = Field(default=8, description='H3 spatial resolution [4, 9]')
    target_asn: str = Field(default='AS15169', description='Target Autonomous System Number')

class ExplainabilityWeights(BaseModel):
    network_health: float = Field(default=0.35, description='Weight for network health')
    routing_stability: float = Field(default=0.25, description='Weight for routing stability')
    infrastructure_growth: float = Field(default=0.2, description='Weight for infrastructure growth')
    cyber_pressure: float = Field(default=0.2, description='Weight for cyber pressure')

class ExplainabilityDetail(BaseModel):
    primary_driver: str = Field(default='network_health', description='Primary contributing factor')
    weights: ExplainabilityWeights = Field(default_factory=ExplainabilityWeights, description='Metric weighting configuration')

class InternetStateResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='Computation timestamp')
    status: str = Field(default='healthy', description='Operational status descriptor')
    primary_metric: float = Field(default=90.7, description='Primary internet health metric score [0-100]')
    secondary_score: float = Field(default=0.95, description='Normalized secondary confidence or ratio score [0-1]')
    state_index: float = Field(default=88.3, description='Composite internet state score [0-100]')
    classification: str = Field(default='OPTIMAL', description='Categorical state classification')
    explainability: ExplainabilityDetail = Field(default_factory=ExplainabilityDetail, description='Explainable scoring breakdown')

class SpatialH3TensorRequest(BaseModel):
    lat: float = Field(default=2.0442, description='Latitude coordinate')
    lon: float = Field(default=102.5689, description='Longitude coordinate')
    resolution: int = Field(default=8, description='H3 spatial resolution level [4, 9]')
    lookback_hours: int = Field(default=24, description='Spatial temporal lookback window')

class SpatialH3TensorResponse(BaseModel):
    h3_index: str = Field(default='886520d81dfffff', description='H3 spatial cell hexagonal index string')
    spatial_cell: str = Field(default='886520d81dfffff', description='Duplicated cell identifier reference')
    density_score: float = Field(default=64.2, description='Network and node density score')
    terrain_state_index: float = Field(default=75.1, description='Aggregated terrain stability index [0-100]')
    status: str = Field(default='ACTIVE', description='Spatial grid node status')

class GenericToolRequest(BaseModel):
    target_identifier: Optional[str] = Field(default=None, description='Optional target identifier or ASN')
    lat: float = Field(default=0.0, description='Latitude')
    lon: float = Field(default=0.0, description='Longitude')
    resolution: int = Field(default=8, description='H3 Resolution')
    lookback_hours: int = Field(default=24, description='Lookback window in hours')
    target_asn: Optional[str] = Field(default=None, description='Target Autonomous System Number')
    extra_params: Dict[str, Any] = Field(default_factory=dict, description='Additional arbitrary execution parameters')

class GenericToolResponse(BaseModel):
    timestamp: str = Field(default_factory=lambda: datetime.now(dt_timezone.utc).isoformat(), description='Execution timestamp')
    tool_name: str = Field(default='generic_tool', description='Name of executed tool')
    score: float = Field(default=85.0, description='Primary computed score or index')
    classification: str = Field(default='STABLE', description='State classification')
    metrics: Dict[str, float] = Field(default_factory=dict, description='Detailed sub-metrics')
    details: Dict[str, Any] = Field(default_factory=dict, description='Additional contextual telemetry data')