from dataclasses import dataclass, field

"""
############################################################################
--------------------------------MODULE ONE----------------------------------
############################################################################
"""


@dataclass
class ClaimInput:
    user_id: str
    image_paths: list[str]
    user_claim: str
    claim_object: str
    
@dataclass
class UserHistory:
    user_id: str
    history_flags: list[str]
    history_summary: str
    
@dataclass
class EvidenceRequirement:
    requirement_id: str
    claim_object: str
    applies_to: str
    minimum_image_evidence: str

@dataclass
class ClaimTarget:
    issue_type: str
    object_part: str
    prompt_injection: bool
    
"""
############################################################################
--------------------------------MODULE TWO----------------------------------
############################################################################
"""
    
    
@dataclass
class ImageObservation:
    image_id: str
    visible_object: str
    visible_part: str
    visible_issue: str
    severity: str
    valid_image: str
    risk_flags: list[str]
    

"""
############################################################################
--------------------------------MODULE FOUR---------------------------------
############################################################################
"""
@dataclass
class ClaimResult:
    user_id: str
    image_paths: str
    user_claim: str
    claim_object: str
    evidence_standard_met: str
    evidence_standard_met_reason: str
    risk_flags: str
    issue_type: str
    object_part: str
    claim_status: str
    claim_status_justification: str
    supporting_image_ids: str
    valid_image: str
    severity: str

@dataclass
class EvidenceResult:
    evidence_standard_met: bool
    evidence_standard_met_reason: str
    supporting_image_ids: list[str]
    

@dataclass
class DecisionResult:
    claim_status: str
    claim_status_justification: str
    issue_type: str
    object_part: str
    severity: str
    
@dataclass
class RiskResult:
    risk_flags: list[str]
    valid_image: bool
    