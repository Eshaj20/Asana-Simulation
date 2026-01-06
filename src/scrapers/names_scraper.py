"""
Simulates realistic human names inspired by
public census datasets.
"""

# Return a list of user names up to the specified limit
def fetch_user_names(limit=50):
    first_names = [
        "Alex", "Jordan", "Taylor", "Morgan", "Riya",
        "Aarav", "Neha", "Daniel", "Chris", "Sofia"
    ]
    last_names = [
        "Smith", "Patel", "Johnson", "Lee", "Brown",
        "Garcia", "Khan", "Singh", "Chen", "Martinez"
    ]

    names = []
    for i in range(limit):
        names.append(
            f"{first_names[i % len(first_names)]} "
            f"{last_names[i % len(last_names)]}"
        )

    return names
