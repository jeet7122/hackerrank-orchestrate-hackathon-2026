from models.model import ClaimTarget, ImageObservation, EvidenceResult
from utils.patterns import RISK_FLAGS

class EvidenceEvaluator:
    
    def evaluate(
        self,
        claim_object: str,
        claim_target: ClaimTarget,
        observations: list[ImageObservation]
    ) -> EvidenceResult:
        supporting_image_ids = []
        for observation in observations:
            
            if observation.visible_object != claim_object:
                continue
            
            if observation.visible_object != claim_target.object_part:
                continue
            
            if any(
                flag in RISK_FLAGS
                for flag in observation.risK_flags
            ): continue
            
            supporting_image_ids.append(observation.image_id)
        
        if not supporting_image_ids:
            return EvidenceResult(
                evidence_standard_met=False,
                evidence_standard_met_reason="No Image cleary shows claimed object and relevant part.",
                supporting_image_ids=[]
            )
        
        return EvidenceResult(
            evidence_standard_met=True,
            evidence_standard_met_reason="Claimed object and relevant part are visible and reviewable.",
            supporting_image_ids=supporting_image_ids
        )