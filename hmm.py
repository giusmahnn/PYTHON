from bs4 import BeautifulSoup
import requests
import time

def scrape_jobberman(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve page. Status code: {response.status_code}")
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all job containers
    jobs = soup.find_all('div', class_="flex flex-grow-0 flex-shrink-0 w-full")
    dates = soup.find_all('p', class_="ml-auto text-sm font-normal text-gray-700 text-loading-animate")
    
    # Stop if no jobs are found on this page
    if not jobs:
        print("No jobs found on this page.")
        return None

    # Loop through each job listing and associated date
    for job, date in zip(jobs, dates):
        title = job.find('p', class_="text-lg font-medium break-words text-link-500")
        company = job.find('p', class_="text-sm text-link-500 text-loading-animate inline-block")
        location = job.find('div', class_="flex flex-wrap mt-3 text-sm text-gray-500 md:py-0")
        job_function = job.find('p', class_="text-sm text-gray-500 text-loading-animate inline-block")
        salary = job.find('span', class_="mr-1")

        # Print job information
        print("Job Title:", title.text.strip() if title else "N/A")
        print("Company:", company.text.strip() if company else "N/A")
        print("Location:", location.get_text(strip=True) if location else "N/A")
        job_function_text = job_function.get_text(" ", strip=True) if job_function else "N/A"
        print("Job Function:", job_function_text.replace("\n", "").strip())
        print("Date Posted:", date.text.strip() if date else "N/A")
        print("Salary:", salary.text.strip() if salary else "N/A")
        print("---------------------------")

    # Find the "Next" button to get the URL of the next page
    next_button = soup.find('a', rel="next")
    if next_button and 'href' in next_button.attrs:
        next_page_url = "https://www.jobberman.com" + next_button['href']  # Construct the full URL for the next page
        return next_page_url
    else:
        return None  # No more pages

# Start URL for the first page
url = "https://www.jobberman.com/jobs"

# Loop through pages until no "Next" button is found
while url:
    print(f"Scraping page: {url}")
    url = scrape_jobberman(url)  # Update the URL to the next page URL
    time.sleep(6)  # Pause to avoid overwhelming the server
