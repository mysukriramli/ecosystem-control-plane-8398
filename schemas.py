"""
Ecosystem Control Plane Data Schemas

Authoritative Pydantic schemas for the ecosystem-control-plane governance,
observability, repository registry, architectural intelligence, graph engine,
and H3 spacetime tensor services.
"""
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union
from pydantic import BaseModel, Field

class HealthResponse(BaseModel):
    """Standard health check response model."""
    status: str = 'healthy'
    timestamp: str = '2026-11-06T00:00:00Z'

class ToolItem(BaseModel):
    """Model representing an individual MCP tool capability."""
    name: str = ''
    description: str = ''
    parameters: Dict[str, Any] = Field(default_factory=dict)

class ToolsResponse(BaseModel):
    """Container response model for listing MCP tools."""
    tools: List[Dict[str, Any]] = Field(default_factory=list)

class EcosystemManifest(BaseModel):
    """Standard structure for .ecosystem.json files present in repositories."""
    name: str = ''
    category: str = 'general'
    technologies: List[str] = Field(default_factory=list)
    status: str = 'active'
    dependencies: List[str] = Field(default_factory=list)
    capabilities: List[str] = Field(default_factory=list)
    owner: str = 'ecosystem'

class RepositoryItem(BaseModel):
    """Detailed repository registry metadata entry."""
    id: str = ''
    name: str = ''
    category: str = 'uncategorized'
    owner: str = 'ecosystem'
    status: str = 'active'
    technologies: List[str] = Field(default_factory=list)
    capabilities: List[str] = Field(default_factory=list)
    dependencies: List[str] = Field(default_factory=list)
    health_score: float = 1.0
    influence_score: float = 0.0
    is_mcp: bool = False
    is_fastapi: bool = False
    is_h3: bool = False
    is_duckdb: bool = False
    is_parquet: bool = False
    last_scanned: str = '2026-11-06T00:00:00Z'

class RepositoryQueryRequest(BaseModel):
    """Query parameter container for repository discovery."""
    category: Optional[str] = None
    technology: Optional[str] = None
    status: Optional[str] = None
    has_mcp: Optional[bool] = None
    min_health_score: float = 0.0
    query: str = ''
    limit: int = 100
    offset: int = 0

class RepositoryListResponse(BaseModel):
    """Response payload returning matching repositories."""
    total: int = 0
    repositories: List[RepositoryItem] = Field(default_factory=list)

class OwnershipInfo(BaseModel):
    """Mapping of repository ownership structure."""
    owner: str = 'ecosystem'
    repo_count: int = 0
    repositories: List[str] = Field(default_factory=list)

class CategoryCatalogResponse(BaseModel):
    """Catalog of repository categories across the ecosystem."""
    categories: Dict[str, List[str]] = Field(default_factory=dict)

class GraphNode(BaseModel):
    """Graph node representing a repository or component."""
    id: str = ''
    label: str = ''
    group: str = 'default'
    type: str = 'repository'
    metrics: Dict[str, Any] = Field(default_factory=dict)

class GraphEdge(BaseModel):
    """Graph edge representing dependencies or relationships."""
    source: str = ''
    target: str = ''
    relationship: str = 'depends_on'
    weight: float = 1.0

class ArchitectureGraphRequest(BaseModel):
    """Request query options for architecture graph generation."""
    include_technologies: bool = True
    include_mcp: bool = True
    cluster_by: str = 'category'
    max_depth: int = 10

class ArchitectureGraphResponse(BaseModel):
    """Full ecosystem architecture graph response."""
    nodes: List[GraphNode] = Field(default_factory=list)
    edges: List[GraphEdge] = Field(default_factory=list)
    clusters: Dict[str, List[str]] = Field(default_factory=dict)

class DependencyGraphRequest(BaseModel):
    """Request options for dependency graph analysis."""
    repo_name: Optional[str] = None
    direction: str = 'both'

class DependencyGraphResponse(BaseModel):
    """Dependency tree and relations response."""
    root_repo: str = ''
    nodes: List[GraphNode] = Field(default_factory=list)
    edges: List[GraphEdge] = Field(default_factory=list)
    isolated_repos: List[str] = Field(default_factory=list)

class TopologyGraphRequest(BaseModel):
    """Request payload for topology graph filtering."""
    network_segment: Optional[str] = None

class TopologyGraphResponse(BaseModel):
    """Ecosystem topology graph payload."""
    topology_type: str = 'ecosystem-mesh'
    nodes: List[GraphNode] = Field(default_factory=list)
    edges: List[GraphEdge] = Field(default_factory=list)

class DuplicateItem(BaseModel):
    """Single detected code duplication entry."""
    item_type: str = 'class'
    name: str = ''
    occurrences: int = 0
    repo_locations: List[str] = Field(default_factory=list)
    similarity_score: float = 1.0
    sample_code_hash: str = ''

class DuplicationScanRequest(BaseModel):
    """Request for running duplicate code detection."""
    scan_target: str = 'all'
    min_occurrences: int = 2
    min_similarity: float = 0.85

class DuplicationScanResponse(BaseModel):
    """Detailed duplication scan results."""
    total_duplicates_found: int = 0
    duplicate_classes: List[DuplicateItem] = Field(default_factory=list)
    duplicate_functions: List[DuplicateItem] = Field(default_factory=list)
    duplicate_patterns: List[DuplicateItem] = Field(default_factory=list)
    consolidation_candidates: List[Dict[str, Any]] = Field(default_factory=list)

class FrameworkCandidate(BaseModel):
    """Identified shared component candidate for extraction into SDK."""
    candidate_name: str = ''
    category: str = 'sdk-candidate'
    occurrence_count: int = 0
    impact_score: float = 0.0
    recommended_target_package: str = 'ecosystem-sdk'
    source_repositories: List[str] = Field(default_factory=list)

class FrameworkScanRequest(BaseModel):
    """Request payload for framework extraction engine."""
    threshold_count: int = 3

class FrameworkScanResponse(BaseModel):
    """Framework extraction candidates response."""
    total_candidates: int = 0
    framework_candidates: List[FrameworkCandidate] = Field(default_factory=list)
    recommended_libraries: List[Dict[str, Any]] = Field(default_factory=list)

class MCPServiceInfo(BaseModel):
    """Information regarding a registered MCP service."""
    repo_name: str = ''
    service_name: str = ''
    tool_count: int = 0
    tools: List[ToolItem] = Field(default_factory=list)
    protocol_version: str = '2024-11-05'
    status: str = 'active'

class MCPCatalogRequest(BaseModel):
    """Query parameter container for MCP catalog scanner."""
    search_term: str = ''
    include_tools: bool = True

class MCPCatalogResponse(BaseModel):
    """MCP Catalog query output."""
    total_mcp_services: int = 0
    total_tools: int = 0
    services: List[MCPServiceInfo] = Field(default_factory=list)

class ServiceCatalogRequest(BaseModel):
    """Request options for service classification catalog."""
    service_type: Optional[str] = None

class ServiceCatalogResponse(BaseModel):
    """Catalog of classified services across the ecosystem."""
    fastapi_services: List[str] = Field(default_factory=list)
    mcp_services: List[str] = Field(default_factory=list)
    earth_intelligence_services: List[str] = Field(default_factory=list)
    h3_services: List[str] = Field(default_factory=list)
    duckdb_services: List[str] = Field(default_factory=list)
    parquet_services: List[str] = Field(default_factory=list)
    cyber_intelligence_wires: List[str] = Field(default_factory=list)
    execution_infrastructure: List[str] = Field(default_factory=list)

class GovernanceRuleViolation(BaseModel):
    """Record of a governance standard policy violation."""
    repo_name: str = ''
    rule_id: str = ''
    rule_name: str = ''
    severity: str = 'warning'
    details: str = ''

class GovernanceAuditRequest(BaseModel):
    """Request options for running governance compliance audits."""
    repo_name: Optional[str] = None
    enforce_contract: bool = True

class GovernanceAuditResponse(BaseModel):
    """Governance compliance audit results."""
    repositories_checked: int = 0
    compliant_count: int = 0
    violations_count: int = 0
    violations: List[GovernanceRuleViolation] = Field(default_factory=list)
    overall_compliance_score: float = 100.0

class HealthScoreItem(BaseModel):
    """Health breakdown for a repository."""
    repo_name: str = ''
    overall_health: float = 1.0
    activity_score: float = 1.0
    maintenance_score: float = 1.0
    dependency_risk_score: float = 0.0
    bus_factor_score: float = 1.0
    architecture_risk_score: float = 0.0

class HealthScanRequest(BaseModel):
    """Request options for health scoring engine."""
    repo_name: Optional[str] = None

class HealthScanResponse(BaseModel):
    """Ecosystem health scan response."""
    average_ecosystem_health: float = 1.0
    health_scores: List[HealthScoreItem] = Field(default_factory=list)

class InfluenceScoreRequest(BaseModel):
    """Request options for ecosystem influence score calculations."""
    repo_name: Optional[str] = None

class InfluenceScoreResponse(BaseModel):
    """Calculated ecosystem influence score payload."""
    repo_name: str = ''
    influence_score: float = 0.0
    incoming_dependencies: int = 0
    tool_usage_count: int = 0
    cross_repo_references: int = 0
    adoption_weight: float = 1.0

class MetricsOverviewRequest(BaseModel):
    """Request for overall dashboard metrics."""
    timeframe: str = 'current'

class MetricsOverviewResponse(BaseModel):
    """Dashboard metrics overview."""
    total_repositories: int = 100
    fastapi_count: int = 39
    mcp_count: int = 23
    earth_intelligence_count: int = 7
    h3_count: int = 55
    duckdb_count: int = 28
    parquet_count: int = 29
    intelligence_wires_count: int = 15
    governance_repositories_count: int = 1
    ecosystem_health_score: float = 0.95
    architecture_risk_score: float = 0.08

class LLMContextRequest(BaseModel):
    """Request to generate LLM context documentation."""
    format: str = 'llms.txt'
    repo_name: Optional[str] = None

class LLMContextResponse(BaseModel):
    """Generated LLM context payload."""
    context_type: str = 'llms.txt'
    content: str = ''
    token_count_estimate: int = 0

class EcosystemSummaryRequest(BaseModel):
    """Request options for ecosystem markdown summary generation."""
    include_graphs: bool = False

class EcosystemSummaryResponse(BaseModel):
    """Ecosystem markdown summary response."""
    title: str = 'Ecosystem Architecture Overview'
    summary_markdown: str = ''
    repo_summaries: Dict[str, str] = Field(default_factory=dict)

class H3SpacetimeTensorQueryRequest(BaseModel):
    """Request for H3 spatial tensor and earth intelligence queries."""
    h3_index: str = '8828308281fffff'
    resolution: int = 8
    time_horizon_seconds: int = 3600
    bounding_box: List[float] = Field(default_factory=list)
    temporal_timestamp: str = '2026-11-06T00:00:00Z'

class SpatialGeometryProof(BaseModel):
    """Proof structure for spatial geometry wire validation."""
    proof_id: str = ''
    h3_index: str = ''
    verified: bool = True
    hash_signature: str = ''

class H3SpacetimeTensorQueryResponse(BaseModel):
    """Response containing H3 spacetime tensor data."""
    h3_index: str = ''
    resolution: int = 8
    spatial_tensor_values: Dict[str, Any] = Field(default_factory=dict)
    geometry_proof: SpatialGeometryProof = Field(default_factory=SpatialGeometryProof)
    active_earth_nodes: List[str] = Field(default_factory=list)

class EarthGridStateRequest(BaseModel):
    """Request query for Earth presence intelligence grid."""
    grid_id: str = 'earth-presence-intelligence-grid-1552'
    h3_resolution: int = 7

class EarthGridStateResponse(BaseModel):
    """Earth grid state response."""
    grid_id: str = ''
    active_cell_count: int = 0
    grid_data: Dict[str, Any] = Field(default_factory=dict)

class EcosystemAgentTaskRequest(BaseModel):
    """Request task execution by Mother Bot ecosystem_agent."""
    task_type: str = 'audit'
    target_repo: Optional[str] = None
    parameters: Dict[str, Any] = Field(default_factory=dict)

class EcosystemAgentTaskResponse(BaseModel):
    """Mother Bot execution result response."""
    task_id: str = ''
    task_type: str = 'audit'
    status: str = 'completed'
    recommendations: List[str] = Field(default_factory=list)
    logs: List[str] = Field(default_factory=list)

class EcosystemGenomeResponse(BaseModel):
    """Detailed ecosystem genome & inheritance model."""
    repository_dna: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
    shared_components: List[str] = Field(default_factory=list)
    inheritance_graph: List[GraphEdge] = Field(default_factory=list)
    evolution_report: str = ''