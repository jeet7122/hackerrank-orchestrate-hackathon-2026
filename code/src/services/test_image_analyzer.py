from dotenv import load_dotenv
import os

from src.services.image_analyzer import ImageAnalyzer

load_dotenv()

analyzer = ImageAnalyzer(
    api_key=os.getenv(
        "GEMINI_API_KEY"
    )
)

for image in [
    "../dataset/images/test/case_001/img_1.jpg",
    "../dataset/images/test/case_001/img_2.jpg",
    "../dataset/images/test/case_001/img_3.jpg"
]:
    result = analyzer.analyze(image)
    print("\n", image)
    print(result)