import json

from pathlib import Path
from PIL import Image
from google import genai

from models.model import ImageObservation

from src.prompts.image_analysis_prompt import (
    IMAGE_ANALYSIS_PROMPT
)

from utils.normalizer import (
    ObservationNormalizer
)

from src.exceptions.rate_limit_exception import (
    RateLimitException
)


class ImageAnalyzer:

    def __init__(
        self,
        api_key: str,
        model: str = "gemini-2.5-flash"
    ):

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = model

    def analyze(
        self,
        image_path: str
    ) -> ImageObservation:

        image = Image.open(image_path)

        try:

            response = (
                self.client.models.generate_content(
                    model=self.model,
                    contents=[
                        IMAGE_ANALYSIS_PROMPT,
                        image
                    ]
                )
            )

        except Exception as ex:

            error = str(ex)

            #
            # STOP ENTIRE PIPELINE
            #
            if (
                "429" in error
                or
                "RESOURCE_EXHAUSTED" in error
            ):
                raise RateLimitException(
                    error
                )

            raise

        parsed_response = (
            self._parse_response(
                response.text
            )
        )

        normalized_response = (
            ObservationNormalizer.normalize(
                parsed_response
            )
        )

        return ImageObservation(
            image_id=Path(image_path).stem,

            visible_object=(
                normalized_response[
                    "visible_object"
                ]
            ),

            visible_part=(
                normalized_response[
                    "visible_part"
                ]
            ),

            visible_issue=(
                normalized_response[
                    "visible_issue"
                ]
            ),

            severity=(
                normalized_response[
                    "severity"
                ]
            ),

            valid_image=(
                normalized_response[
                    "valid_image"
                ]
            ),

            risk_flags=(
                normalized_response[
                    "risk_flags"
                ]
            )
        )

    def _parse_response(
        self,
        response_text: str
    ) -> dict:

        response_text = (
            response_text.strip()
        )

        if response_text.startswith(
            "```json"
        ):

            response_text = (
                response_text
                .replace(
                    "```json",
                    ""
                )
                .replace(
                    "```",
                    ""
                )
                .strip()
            )

        try:

            return json.loads(
                response_text
            )

        except Exception:

            #
            # Gemini returned invalid JSON
            #
            return {
                "visible_object": "unknown",
                "visible_part": "unknown",
                "visible_issue": "unknown",
                "severity": "unknown",
                "valid_image": False,
                "risk_flags": [
                    "manual_review_required"
                ]
            }