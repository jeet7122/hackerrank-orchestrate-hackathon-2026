from src.loaders.data_loader import DataLoader

loader = DataLoader()

claims, histories, requirements = loader.loadAll(
    "../dataset/claims.csv",
    "../dataset/user_history.csv",
    "../dataset/evidence_requirements.csv"
)

print(f"Claims Loaded: {len(claims)}")
print(f"Users Loaded: {len(histories)}")
print(f"Requirements Loaded: {len(requirements)}")

for claim in claims[:10]:
    print(claim.user_id)
    print(claim.user_claim)
    print()