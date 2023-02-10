import requests
from bs4 import BeautifulSoup
import json

# Make a request to the URL and get the HTML content
url = "https://github.com/gohugoio/hugoThemes"
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all div elements with the specified class
results = []
for div in soup.find_all("span", class_="css-truncate css-truncate-target d-block width-fit"):
    # Find the first a element inside the div
    link = div.find("a")

    # Check if the link was found
    if link is not None:
        # Extract the text of the div
        element_text = div.text

        # Extract the href of the link
        href = link.get("href")

        # Store the results in a dictionary
        result = {
            "Name": element_text,
            "Github Repo": "https://github.com"+href
        }
        results.append(result)

# Write the results to a JSON file
with open("themes.json", "w") as file:
    json.dump(results, file)

# Confirm that the file has been written
print("Data written to themes.json")
