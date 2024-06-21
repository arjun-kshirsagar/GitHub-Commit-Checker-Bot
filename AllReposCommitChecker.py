import requests
import urllib3
import warnings
from datetime import datetime

urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)
warnings.simplefilter('ignore', urllib3.exceptions.InsecureRequestWarning)

# Constants
GITHUB_API_URL = "https://api.github.com"
TOKEN = ""
STUDENTS = [
    "arjun-kshirsagar",
    "UditNayak",
    "AbhinavGupta-de",
    "charanbhatia",
    "Thrishalmadasu",
    "Vishesh-Paliwal",
    "kohantikanath",
    "harshinireddy05",
    "sanjanaynvsdl",
    "satish-rathod",
    "KKartikay-27",
    "Krupakar-Reddy-S",
    "BHAV0207",
    "Arnavya",
    "Ajai-Sharan",
    "kananarora1",
    "Beserker-356",
    "nobitaN0bi",
    "abhinav26966",
    "Swarnim114",
    "HackerXeroid",
    "mayank-vashishtt",
    "poojatalele",
    "GSRK-BZA",
    "attaditya",
    "tamanna1809",
    "TanviAgarwal-14",
    "Rudrakc",
    "Manan21st",
    "sachan13harshit",
    "kumarprince7999",
    "mayank1365",
    "kumarprince7999",
    "mayank1365",
    "harshinireddy05",
    "its-harshitgoel",
    "Yash020405",
    "sanjanaynvsdl",
    "DevMhrn",
    "BarryByte",
    "MrPhenomenal3110",
    "kumarprince7999",
    "rushil-118",
    "sgnhyperion",
    "purvanshh",
    "H-A-R-S-H-K",
    "harsh-791",
    "harsh-kumar-patwa",
    "amlanxbghn",
    "VinayakPaka",
    "neeldholiya04",
    "nullHawk",
    "Suryansh-D",
    "lokendra005",
    "Vijaygaurav2004",
    "shailendra-jurel",
    "shrimay18",
    "Dipti0704",
    "Shreshthaaa",
    "hemkeshkantawala11",
    "sailingsam"
    # Add more students' GitHub usernames
]
CHECK_DATE = "2024-06-21"  # The date to check commits for (YYYY-MM-DD)

# Function to get repositories for a specific user
def get_repositories(username):
    url = f"{GITHUB_API_URL}/users/{username}/repos"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        repositories = response.json()
        return [repo['name'] for repo in repositories]
    else:
        print(f"Error fetching repositories for {username}: {response.status_code}")
        return []

# Function to get commits for a specific repo on a specific date
def get_commits(username, repo, date):
    url = f"{GITHUB_API_URL}/repos/{username}/{repo}/commits"
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    params = {
        "since": f"{date}T00:00:00Z",
        "until": f"{date}T23:59:59Z"
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    if response.status_code == 200:
        commits = response.json()
        return commits
    else:
        print(f"Error fetching commits for {username}/{repo}: {response.status_code}")
        return []

# Check commits for each student
def check_students_commits(students, date):
    results = {}
    for username in students:
        repositories = get_repositories(username)
        user_has_commits = False
        for repo in repositories:
            commits = get_commits(username, repo, date)
            if commits:
                user_has_commits = True
                break
        results[username] = user_has_commits
    return results

# Main execution
if __name__ == "__main__":
    results = check_students_commits(STUDENTS, CHECK_DATE)
    for student, has_commits in results.items():
        status = "made a commit" if has_commits else "did not make a commit"
        print(f"{student} {status} on {CHECK_DATE}")
