import os
import pandas as pd

from dotenv import load_dotenv

from src.writers.output_writer import OutputWriter
from src.loaders.data_loader import DataLoader

from src.claim_extractor import ClaimExtractor

from src.services.image_analyzer import ImageAnalyzer
from src.services.claim_image_analyzer import ClaimImageAnalyzer
from src.services.claim_processor import ClaimProcessor

from src.evidence_evaluator import EvidenceEvaluator
from src.decision_engine import DecisionEngine
from src.risk_engine import RiskEngine

from src.exceptions.rate_limit_exception import (
RateLimitException
)

OUTPUT_FILE = "../dataset/output.csv"

def get_resume_index() -> int:

    if not os.path.exists(
        OUTPUT_FILE
    ):
        return 0

    try:

        existing = pd.read_csv(
            OUTPUT_FILE
        )

        return len(existing)

    except Exception:

        return 0

def main():

    load_dotenv()

    print("Loading data...")

    loader = DataLoader()

    claims, user_histories, requirements = (
        loader.loadAll(
            "../dataset/claims.csv",
            "../dataset/user_history.csv",
            "../dataset/evidence_requirements.csv"
        )
    )

    start_index = get_resume_index()

    print(
        f"Resuming from claim "
        f"{start_index + 1}"
    )

    #
    # Services
    #
    claim_extractor = ClaimExtractor()

    image_analyzer = ImageAnalyzer(
        api_key=os.getenv(
            "GEMINI_API_KEY"
        )
    )

    claim_image_analyzer = (
        ClaimImageAnalyzer(
            image_analyzer=image_analyzer
        )
    )

    evidence_evaluator = (
        EvidenceEvaluator()
    )

    decision_engine = (
        DecisionEngine()
    )

    risk_engine = (
        RiskEngine()
    )

    processor = ClaimProcessor(
        claim_extractor=claim_extractor,
        claim_image_analyzer=(
            claim_image_analyzer
        ),
        evidence_evaluator=(
            evidence_evaluator
        ),
        decision_engine=(
            decision_engine
        ),
        risk_engine=(
            risk_engine
        )
    )

    writer = OutputWriter()

    #
    # Fresh file
    #
    if start_index == 0:

        writer.open(
            OUTPUT_FILE
        )

    #
    # Resume file
    #
    else:

        writer.open_append(
            OUTPUT_FILE
        )

    processed = start_index

    try:

        for index, claim in enumerate(
            claims
        ):

            if index < start_index:
                continue

            user_history = (
                user_histories[
                    claim.user_id
                ]
            )

            try:

                result = (
                    processor.process(
                        claim,
                        user_history
                    )
                )

                writer.write_row(
                    result
                )

                processed += 1

                print(
                    f"[{processed}/{len(claims)}] "
                    f"{claim.user_id} | "
                    f"{result.claim_status}"
                )

            except RateLimitException:

                print(
                    "\nGemini quota exhausted."
                )

                print(
                    f"Stopped at claim "
                    f"{index + 1}"
                )

                print(
                    f"Completed "
                    f"{processed} claims."
                )

                break

            except Exception as ex:

                print(
                    f"Claim failed: "
                    f"{claim.user_id}"
                )

                print(ex)

    finally:

        writer.close()

    print("\nDone.")

    print(
        f"Rows written: "
        f"{processed}"
    )

if __name__ == "__main__":
    main()
