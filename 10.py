import csv
import numpy as np


followers = []
public_repos = []
path = r'D:\Sakthi_the_mass\IITM\TDS\Project1\pro1 (1)\users.csv'

# Open the users.csv file and read data
with open(path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        # Filter for users in Delhi
        location = row.get('location', '').strip().lower()
        if "chicago" in location:
            # Get followers and public repositories values
            try:
                followers_count = int(row['followers'])
                public_repos_count = int(row['public_repos'])
                
                # Append the valid values to the lists
                followers.append(followers_count)
                public_repos.append(public_repos_count)
            except ValueError:
                # Skip rows with invalid numerical values
                continue

# Ensure there is data for regression
if len(followers) > 1 and len(public_repos) > 1:
    # Perform linear regression: followers ~ public_repos
    slope, intercept = np.polyfit(public_repos, followers, 1)
    
    # Output the slope rounded to 3 decimal places
    print(f"{slope:.3f}")
else:
    print("Insufficient data for regression.")
