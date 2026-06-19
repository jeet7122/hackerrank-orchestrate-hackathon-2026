import pandas as pd
from models.model import UserHistory

class UserHistoryLoader:
    
    def laod(self, file_path: str) -> dict[str, UserHistory]:
        df = pd.read_csv(file_path) 
        
        history_map = {}
        for _, row in df.iterrows:
            
            flags = []

            history_flags = str(row["history_flags"])

            if history_flags.lower() != "none":
                flags = [
                    flag.strip()
                    for flag in history_flags.split(";")
                ]

            history = UserHistory(
                user_id=str(row["user_id"]),
                history_flags=flags,
                history_summary=str(row["history_summary"])
            )

            history_map[history.user_id] = history
            
        return history_map