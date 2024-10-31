from bs4 import BeautifulSoup
import requests
import time


def scrape_jobberman(url): #function with a parameter url
    with open("jobs.txt", "w") as j: #write our output directly into a file
        for i in range(5): # Loops over the number of pages in the site 
            response = requests.get(url)
            if response.status_code != 200:
                print(f"Failed to retrieve page. Status code: {response.status_code}")
                return None

            soup = BeautifulSoup(response.text, 'html.parser')


            jobs = soup.find_all('div', class_="flex flex-grow-0 flex-shrink-0 w-full")
            dates = soup.find_all('p', class_="ml-auto text-sm font-normal text-gray-700 text-loading-animate")
            if not jobs:
                print("No jobs found.")
                return None
        
            for job, date in zip(jobs, dates):
                    
                title = job.find('p', class_="text-lg font-medium break-words text-link-500")
                company = job.find('p', class_="text-sm text-link-500 text-loading-animate inline-block")
                location = job.find('div', class_="flex flex-wrap mt-3 text-sm text-gray-500 md:py-0")
                job_function = job.find('p', class_="text-sm text-gray-500 text-loading-animate inline-block")
                salary = job.find('span', class_="mr-1")

                # Write job information to file
                j.write("Job Title: " + (title.text.strip() if title else "N/A") + "\n")
                j.write("Company: " + (company.text.strip() if company else "N/A") + "\n")
                j.write("Location: " + (location.get_text(strip=True) if location else "N/A") + "\n")
                job_function_text = job_function.get_text(" ", strip=True) if job_function else "N/A"
                j.write("Job Function: " + job_function_text.replace("\n", "").strip() + "\n")
                j.write("Date Posted: " + (date.text.strip() if date else "N/A") + "\n")
                j.write("Salary: " + (salary.text.strip() if salary else "N/A") + "\n")
                j.write("---------------------------\n")
        

            next_button = soup.find('a', rel="next")
            if next_button and 'href' in next_button.attrs:
                url = next_button['href']  # Use the relative URL for the next page
                if not url.startswith("http"):
                    url = f"https://www.jobberman.com{url}"  # Ensure it's an absolute URL
            else:
                print("No more pages found.")
                break  # Exit the loop if there is no "Next" button

            # Pause to avoid overwhelming the server
            time.sleep(2) 

url = "https://www.jobberman.com/jobs"
scrape_jobberman(url) #call our function to scrape