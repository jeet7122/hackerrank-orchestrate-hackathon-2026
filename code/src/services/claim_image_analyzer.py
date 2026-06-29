from models.model import ImageObservation
from src.services.image_analyzer import ImageAnalyzer
from src.exceptions.rate_limit_exception import RateLimitException
import traceback

class ClaimImageAnalyzer:
    
    def __init__(self, image_analyzer: ImageAnalyzer):
        self.image_analyzer = image_analyzer
        
    def analyze_images(self, image_paths: list[str]) -> list[ImageObservation]:
        observations = []
        
        for image_path in image_paths:
            try:
                root_image_path = "../dataset/" + image_path
                observation = self.image_analyzer.analyze(root_image_path)
                
                observations.append(observation)
            except RateLimitException:
                raise
            except Exception as ex:
                print(
                    f"Failed to analyze image "
                    f"{image_path}: {ex}"
                )
        return observations
