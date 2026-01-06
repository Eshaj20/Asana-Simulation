"""
Simulates scraping company names from public sources
(e.g., YC directory, Crunchbase).
"""

# Return a list of company names up to the specified limit
def fetch_company_names(limit=10):
    companies = [
        "Acme Technologies",
        "Nimbus Labs",
        "Vertex Solutions",
        "Orbit Systems",
        "BlueRiver Analytics",
        "NovaSoft",
        "CloudForge",
        "Zenith AI",
        "Pulse Innovations",
        "Atlas Digital"
    ]
    return companies[:limit]
