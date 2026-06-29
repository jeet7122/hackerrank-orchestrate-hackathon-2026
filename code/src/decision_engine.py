from models.model import (
ClaimTarget,
EvidenceResult,
ImageObservation,
DecisionResult
)

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
                claim_status_justification=(
                    "The claimed object part is not clearly visible."
                ),
                issue_type="unknown",
                object_part=claim_target.object_part,
                severity="unknown",
                supporting_image_ids=[]
            )

        reviewable_ids = set(
            evidence_result.supporting_image_ids
        )

        matching_observations = [
            obs
            for obs in observations
            if obs.image_id in reviewable_ids
        ]

        if not matching_observations:
            return DecisionResult(
                claim_status="not_enough_information",
                claim_status_justification=(
                    "Unable to evaluate claim."
                ),
                issue_type="unknown",
                object_part="unknown",
                severity="unknown",
                supporting_image_ids=[]
            )

        #
        # GENERIC DAMAGE CLAIM
        #
        if claim_target.issue_type == "generic_damage":

            for observation in matching_observations:

                if observation.visible_issue not in {
                    "none",
                    "unknown"
                }:
                    return DecisionResult(
                        claim_status="supported",
                        claim_status_justification=(
                            f"Visible {observation.visible_issue} "
                            f"found on {observation.visible_part}."
                        ),
                        issue_type=observation.visible_issue,
                        object_part=observation.visible_part,
                        severity=observation.severity,
                        supporting_image_ids=[
                            observation.image_id
                        ]
                    )

            contradiction_image = (
                matching_observations[0]
            )

            return DecisionResult(
                claim_status="contradicted",
                claim_status_justification=(
                    "Relevant object part is visible "
                    "but no damage is observed."
                ),
                issue_type="none",
                object_part=contradiction_image.visible_part,
                severity="none",
                supporting_image_ids=[
                    contradiction_image.image_id
                ]
            )

        #
        # SPECIFIC DAMAGE CLAIM
        #
        for observation in matching_observations:

            if (
                observation.visible_issue
                == claim_target.issue_type
            ):
                return DecisionResult(
                    claim_status="supported",
                    claim_status_justification=(
                        f"Visible "
                        f"{claim_target.issue_type} "
                        f"found on "
                        f"{claim_target.object_part}."
                    ),
                    issue_type=observation.visible_issue,
                    object_part=observation.visible_part,
                    severity=observation.severity,
                    supporting_image_ids=[
                        observation.image_id
                    ]
                )

        contradiction_image = (
            matching_observations[0]
        )

        if contradiction_image.visible_issue == "none":

            return DecisionResult(
                claim_status="contradicted",
                claim_status_justification=(
                    f"No visible "
                    f"{claim_target.issue_type} "
                    f"found on "
                    f"{claim_target.object_part}."
                ),
                issue_type="none",
                object_part=contradiction_image.visible_part,
                severity="none",
                supporting_image_ids=[
                    contradiction_image.image_id
                ]
            )

        return DecisionResult(
            claim_status="contradicted",
            claim_status_justification=(
                f"Observed "
                f"{contradiction_image.visible_issue} "
                f"instead of claimed "
                f"{claim_target.issue_type}."
            ),
            issue_type=contradiction_image.visible_issue,
            object_part=contradiction_image.visible_part,
            severity=contradiction_image.severity,
            supporting_image_ids=[
                contradiction_image.image_id
            ]
        )
