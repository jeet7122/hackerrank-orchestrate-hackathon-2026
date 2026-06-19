from models.model import ClaimTarget, EvidenceResult, ImageObservation, DecisionResult

class DecisionEngine:
    
    def decide(
        self,
        claim_target: ClaimTarget,
        observations: list[ImageObservation],
        evidence_result: EvidenceResult
    ) -> DecisionResult:
        
        if not evidence_result.evidence_standard_met:
            return DecisionResult(
                claim_status="not_enough_information",
                claim_status_justification="The claimed object part is ot clearly visible.",
                issue_type="unknown",
                object_part=claim_target.object_part,
                severity="unknown"
            )
            
        supporting_images = set(evidence_result.supporting_image_ids)
        
        for observation in observations:
            if observation.image_id not in supporting_images:
                continue
            
            if observation.visible_issue == claim_target.issue_type:
                return DecisionResult(
                    claim_status="supported",
                    claim_status_justification=(
                        f"Visible {claim_target.issue_type} found on "
                        f"{claim_target.object_part}."
                    ),
                    issue_type=observation.visible_issue,
                    object_part=observation.visible_part,
                    severity=observation.severity
                )
        
        first_image = next((obs for obs in observations if obs.image_id in supporting_images), None)
        
        if first_image:
            return DecisionResult(
                claim_status="contradicted",
                claim_status_justification=(
                    f"Observed issue does not match claimed "
                    f"{claim_target.issue_type}."
                ),
                issue_type=first_image.visible_issue,
                object_part=first_image.visible_part,
                severity=first_image.severity
            )
        
        return DecisionResult(
            claim_status="not_enough_information",
            claim_status_justification="Unable to evaluate claim.",
            issue_type="unknown",
            object_part="unknown",
            severity="unknown"
        )
    

 