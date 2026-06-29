from models.model import (
ClaimTarget,
ImageObservation,
EvidenceResult
)

class EvidenceEvaluator:

    UNREVIEWABLE_FLAGS = {
        "blurry_image",
        "cropped_or_obstructed",
        "low_light_or_glare",
        "wrong_angle",
        "wrong_object",
        "wrong_object_part"
    }

    def evaluate(
        self,
        claim_object: str,
        claim_target: ClaimTarget,
        observations: list[ImageObservation]
    ) -> EvidenceResult:

        supporting_image_ids = []

        for observation in observations:

            #
            # Wrong object
            #
            if observation.visible_object != claim_object:
                continue

            #
            # Wrong part
            #
            if (
                claim_target.object_part != "unknown"
                and
                observation.visible_part
                != claim_target.object_part
            ):
                continue

            #
            # Unreviewable image
            #
            if any(
                flag in self.UNREVIEWABLE_FLAGS
                for flag in observation.risk_flags
            ):
                continue

            #
            # Generic damage claim
            #
            if claim_target.issue_type == "generic_damage":

                if observation.visible_issue not in {
                    "none",
                    "unknown"
                }:
                    supporting_image_ids.append(
                        observation.image_id
                    )

                continue

            #
            # Specific damage claim
            #
            if (
                observation.visible_issue
                == claim_target.issue_type
            ):
                supporting_image_ids.append(
                    observation.image_id
                )

        #
        # No supporting images found
        #
        if not supporting_image_ids:

            reviewable_images = [
                observation
                for observation in observations
                if (
                    observation.visible_object
                    == claim_object
                )
            ]

            if reviewable_images:

                return EvidenceResult(
                    evidence_standard_met=True,
                    evidence_standard_met_reason=(
                        "Claimed object and relevant part "
                        "are visible and reviewable."
                    ),
                    supporting_image_ids=[]
                )

            return EvidenceResult(
                evidence_standard_met=False,
                evidence_standard_met_reason=(
                    "No image clearly shows the claimed "
                    "object and relevant part."
                ),
                supporting_image_ids=[]
            )

        return EvidenceResult(
            evidence_standard_met=True,
            evidence_standard_met_reason=(
                "Claimed object and relevant part "
                "are visible and reviewable."
            ),
            supporting_image_ids=supporting_image_ids
        )
