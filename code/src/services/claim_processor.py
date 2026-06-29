from models.model import ClaimInput, ClaimResult, UserHistory
from src.claim_extractor import ClaimExtractor
from src.services.claim_image_analyzer import ClaimImageAnalyzer
from src.evidence_evaluator import EvidenceEvaluator
from src.decision_engine import DecisionEngine
from src.risk_engine import RiskEngine

class ClaimProcessor:
    def __init__(
        self,
        claim_extractor: ClaimExtractor,
        claim_image_analyzer: ClaimImageAnalyzer,
        evidence_evaluator: EvidenceEvaluator,
        decision_engine: DecisionEngine,
        risk_engine: RiskEngine
        ):
        self.claim_extractor = claim_extractor
        self.claim_image_analyzer = claim_image_analyzer
        self.evidence_evaluator = evidence_evaluator
        self.decision_engine = decision_engine
        self.risk_engine = risk_engine
        
    def process(
        self,
        claim: ClaimInput,
        user_history: UserHistory
    ) -> ClaimResult:
        claim_target = self.claim_extractor.extract(claim.user_claim)
        observations = self.claim_image_analyzer.analyze_images(claim.image_paths)
        evidence_result = self.evidence_evaluator.evaluate(
            claim.claim_object,
            claim_target,
            observations
        )
        
        decision_result = self.decision_engine.decide(
            claim_target,
            observations,
            evidence_result
        )
        
        risk_result = self.risk_engine.evaluate(
            claim_target,
            observations,
            user_history,
            decision_result
        )
        
        return ClaimResult(
            user_id=claim.user_id,
            image_paths=";".join(claim.image_paths),
            user_claim=claim.user_claim,
            claim_object=claim.claim_object,
            evidence_standard_met=str(evidence_result.evidence_standard_met).lower(),
            evidence_standard_met_reason=evidence_result.evidence_standard_met_reason,
            risk_flags=(";".join(risk_result.risk_flags) if risk_result.risk_flags else "none"),
            issue_type=decision_result.issue_type,
            object_part=decision_result.object_part,
            claim_status=decision_result.claim_status,
            claim_status_justification=decision_result.claim_status_justification,
            supporting_image_ids=( ";".join( decision_result .supporting_image_ids ) if decision_result .supporting_image_ids else "none" ),
            valid_image=str(risk_result.valid_image).lower(),
            severity=decision_result.severity
        )