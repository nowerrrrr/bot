import requests
import datetime
import time
import os

# GitHub API URL and personal access token
github_api_url = "https://api.github.com/repos/your-username/your-repo-name"
access_token = "your-github-token"

# Start date of your Python learning journey
start_date = datetime.date(YYYY, MM, DD)

# Define special day counts and their corresponding messages
special_days = {
    100: "Yay, 100 days!",
    200: "Another milestone at 200 days!",
    365: "One year of learning Python!",
}

def update_github_description():
    # Calculate the number of days since you started learning Python
    current_date = datetime.date.today()
    days_learning_python = (current_date - start_date).days

    # Check for special days and update the GitHub repository description
    new_description = f"Day {days_learning_python} of learning Python."
    if days_learning_python in special_days:
        new_description += f"\n\n{special_days[days_learning_python]}"

    headers = {"Authorization": f"token {access_token}"}
    payload = {"description": new_description}
    response = requests.patch(github_api_url, headers=headers, json=payload)

    if response.status_code == 200:
        print("GitHub description updated successfully.")
    else:
        print(f"Error updating GitHub description. Status code: {response.status_code}")

if __name__ == "__main__":
    # Check if it's the first run (or a daily run) based on a marker file
    marker_file = "bot_marker.txt"

    if not os.path.exists(marker_file):
        # This is the first run or a new day
        update_github_description()

        # Create or update the marker file
        with open(marker_file, "w") as f:
            f.write(str(datetime.date.today()))

    while True:
        # Check if the current date is different from the marker file date
        with open(marker_file, "r") as f:
            last_run_date = datetime.date.fromisoformat(f.read())

        if datetime.date.today() != last_run_date:
            update_github_description()

            # Update the marker file
            with open(marker_file, "w") as f:
                f.write(str(datetime.date.today()))

        # Sleep for a while (e.g., 1 hour) before checking again
        time.sleep(3600)