from models.model import ClaimTarget
from utils.patterns import PROMPT_INJECTION_PATTERNS, ISSUE_PATTERNS, PART_PATTERNS

class ClaimExtractor:
    
    def extract(
        self,
        user_claim: str,
        claim_object: str,
    ) -> ClaimTarget:
        
        text = user_claim.lower()
        prompt_injection = self._detect_prompt_injection(text)
        issue_type = self._extract_issue(text)
        object_part = self._extract_part(text)
        
        return ClaimTarget(
            issue_type=issue_type,
            object_part=object_part,
            prompt_injection=prompt_injection
        )
        
     
    
    def _detect_prompt_injection(
        self,
        text: str
    ) -> bool:
        for pattern in PROMPT_INJECTION_PATTERNS:
            if pattern in text:
                return True
        return False   
    
    def _extract_issue(
        self,
        text: str
    ) -> str:
        for issue, patterns in ISSUE_PATTERNS.items():
            for pattern in patterns:
                if pattern in text:
                    return issue
        return "unknown" 
    
    def _extract_part(
        self,
        text: str
    ) -> str:

        for part, patterns in PART_PATTERNS.items():
            for pattern in patterns:
                if pattern in text:
                    return part

        return "unknown"       