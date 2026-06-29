from models.model import EvidenceRequirement
import pandas as pd

class EvidenceRequirementsLoader:
    def load(self, file_path: str) -> list[EvidenceRequirement]:
        
        df = pd.read_csv(file_path)
        
        requirements = []
        
        for _, row in df.iterrows():

            requirements.append(
                EvidenceRequirement(
                    requirement_id=str(row["requirement_id"]),
                    claim_object=str(row["claim_object"]),
                    applies_to=str(row["applies_to"]),
                    minimum_image_evidence=str(
                        row["minimum_image_evidence"]
                    )
                )
            )

        return requirements