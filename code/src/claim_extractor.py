from models.model import ClaimTarget
from utils.patterns import PROMPT_INJECTION_PATTERNS, ISSUE_PATTERNS, PART_PATTERNS

class ClaimExtractor:
    
    
    """
    #########################################################################
    Extracts object s
    #########################################################################
    """
    def extract(
        self,
        user_claim: str,
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
        
     
    """
    #########################################################################
    finds injected prompts in conversations to avoid malware
    #########################################################################
    """
    def _detect_prompt_injection(
        self,
        text: str
    ) -> bool:
        for pattern in PROMPT_INJECTION_PATTERNS:
            if pattern in text:
                return True
        return False   
    
    """
    #########################################################################
    extract issue for provdided classified set of issues
    #########################################################################
    """
    def _extract_issue(
        self,
        text: str
    ) -> str:
        for issue, patterns in ISSUE_PATTERNS.items():
            for pattern in patterns:
                if pattern in text:
                    return issue
        return "unknown" 
    
    """
    #########################################################################
    finds exact part from conversation text
    #########################################################################
    """
    def _extract_part(
        self,
        text: str
    ) -> str:

        for part, patterns in PART_PATTERNS.items():
            for pattern in patterns:
                if pattern in text:
                    return part

        return "unknown"       