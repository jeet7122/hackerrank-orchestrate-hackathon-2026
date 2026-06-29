from src.loaders.claims_loader import ClaimsLoader
from src.loaders.user_history_loader import UserHistoryLoader
from src.loaders.evidence_requirement_loader import EvidenceRequirementsLoader

class DataLoader:
    def __init__(self):
        self.claims_loader = ClaimsLoader()
        self.user_history_loader = UserHistoryLoader()
        self.requirements_loader = EvidenceRequirementsLoader()
    
    def loadAll(self, claims_path, user_history_path, requirements_path):
        claims = self.claims_loader.load(claims_path)
        user_history = self.user_history_loader.load(user_history_path)
        requirements = self.requirements_loader.load(requirements_path)
        return (claims, user_history, requirements)