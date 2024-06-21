import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.NotOpenSSLWarning)

# Constants
GITHUB_API_URL = "https://api.github.com"
TOKEN = ""
STUDENTS = {
    "arjun-kshirsagar": "My-Website",
    "UditNayak": "portfolio",
    # Add more students and their repositories
}
CHECK_DATE = "2024-06-19"  # The date to check commits for (YYYY-MM-DD)

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
    for username, repo in students.items():
        commits = get_commits(username, repo, date)
        results[username] = bool(commits)
    return results

# Main execution
if __name__ == "__main__":
    results = check_students_commits(STUDENTS, CHECK_DATE)
    for student, has_commits in results.items():
        status = "made a commit" if has_commits else "did not make a commit"
        print(f"{student} {status} on {CHECK_DATE}")
