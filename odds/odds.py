import requests
from bs4 import BeautifulSoup


def get_odds(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        odds_data = soup.find_all(
            "div", id="game_category_Passing Props" #data-testid as source?
        )  # Adjust class or tag based on website structure
        odds = [float(odds.get_text()) for odds in odds_data]
        return odds
    else:
        print("Failed to fetch data")
        return []


# URLs of different sportsbooks
sportsbook_urls = [
    "https://sportsbook.draftkings.com/leagues/football/nfl?_gl=1*g64evk*_ga*NDA0MzAyODQuMTY5MzMyODM3MA..*_ga_QG8WHJSQMJ*MTY5ODg4MDc2MS4xLjEuMTY5ODg4MTQyMi41OS4wLjA.&_ga=2.47005607.1016180974.1698880762-40430284.1693328370&category=passing-props-",
    "https://sportsbook.fanduel.com/navigation/nfl?tab=player-props",
    # Add more sportsbook URLs as needed
]

all_odds = []
for url in sportsbook_urls:
    odds = get_odds(url)
    all_odds.append(odds)

# Compare the odds from different sportsbooks
if all_odds:
    for i, odds in enumerate(all_odds):
        print(f"Odds from sportsbook {i + 1}: {odds}")
else:
    print("No odds data found")
