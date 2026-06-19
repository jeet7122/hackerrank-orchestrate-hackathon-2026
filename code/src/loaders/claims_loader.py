import pandas as pd
from models.model import ClaimInput

class ClaimsLoader:
    def load(self, path: str) -> list[ClaimInput]:
        df = pd.read_csv(path)
        
        claims = []
        
        for _,row in df.iterrows:
            claims.append(
                ClaimInput(
                    user_id=row["user_id"],
                    image_paths=row["image_paths"].split(";"),
                    user_claim=row["user_claim"],
                    claim_object=row["claim_object"]
                )
            )
        
        return claims
