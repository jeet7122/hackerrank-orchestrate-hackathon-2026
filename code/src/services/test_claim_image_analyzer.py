import os

from dotenv import load_dotenv

from src.services.image_analyzer import ImageAnalyzer
from src.services.claim_image_analyzer import (
    ClaimImageAnalyzer
)

load_dotenv()

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

results = (
    claim_image_analyzer.analyze_images(
        [
            "../dataset/images/test/case_001/img_1.jpg",
            "../dataset/images/test/case_001/img_2.jpg",
            "../dataset/images/test/case_001/img_3.jpg"
        ]
    )
)

for result in results:
    print(result)