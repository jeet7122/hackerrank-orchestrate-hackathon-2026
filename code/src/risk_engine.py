from models.model import ClaimTarget, ImageObservation, UserHistory, DecisionResult, RiskResult

class RiskEngine:
    
    def evaluate(
        self,
        claim_target: ClaimTarget,
        observations: list[ImageObservation],
        user_history: UserHistory,
        decision_result: DecisionResult
    ) -> RiskResult:
        risk_flags = set()
        
        if claim_target.prompt_injection:
            risk_flags.add("text_instruction_present")
        
        for flag in user_history.history_flags:
            if flag != "none":
                risk_flags.add(flag)

        for observation in observations:

            for flag in observation.risk_flags:
                risk_flags.add(flag)

        if (
            decision_result.claim_status
            == "contradicted"
            and
            decision_result.issue_type == "none"
        ):
            risk_flags.add(
                "damage_not_visible"
            )

        valid_image = True

        for observation in observations:

            if (
                "possible_manipulation"
                in observation.risk_flags
            ):
                valid_image = False

            if (
                "non_original_image"
                in observation.risk_flags
            ):
                valid_image = False

        return RiskResult(
            risk_flags=sorted(list(risk_flags)),
            valid_image=valid_image
        )