import requests
from bs4 import BeautifulSoup
import json

# Make a request to the URL and get the HTML content
url = "https://dineshpanthi.science/pubtype/jpaper/page/2/"
response = requests.get(url)
html_content = response.content

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find all div elements with class "pubmain"
results = []
for div in soup.find_all("div", class_="pubmain"):

    # Find the first a element inside the div
    link = div.find("a")
    types = div.find("span", class_="label label-warning")
    author = div.find("div", class_="pubauthor")
    cite = div.find("div", class_="pubcite")
    year = div.find("div", class_="pubyear")

    # Extract the text of the elements
    title = link.text
    href = link.get("href")
    typess = types.text
    authors = author.text
    cites = cite.text
    year = year.text

    # Store the results in a dictionary
    result = {
        "Title": title,
        "Authors": authors,
        "Citation": cites,
        "Publication Year": year,
        "Publication Type": typess,
        "url": href
    }
    results.append(result)

# Write the results to a JSON file
with open("Publications2.json", "w") as file:
    json.dump(results, file)

# Confirm that the file has been written
print("Data written to Publication.json")
