# DA JOB MARKET SCRAPER — Internshala

# Scrapes page 1 across 8 Indian cities + remote

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# Create data folder

os.makedirs("data", exist_ok=True)

# Headers
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": (
        "text/html,application/xhtml+xml,"
        "application/xml;q=0.9,*/*;q=0.8"
    ),
    "Referer": "https://internshala.com/",
}

# Search URLs
SEARCH_URLS = {
    "Bangalore":  "https://internshala.com/jobs/data-analyst-jobs-in-bangalore/",
    "Delhi":      "https://internshala.com/jobs/data-analyst-jobs-in-delhi/",
    "Mumbai":     "https://internshala.com/jobs/data-analyst-jobs-in-mumbai/",
    "Hyderabad":  "https://internshala.com/jobs/data-analyst-jobs-in-hyderabad/",
    "Chennai":    "https://internshala.com/jobs/data-analyst-jobs-in-chennai/",
    "Pune":       "https://internshala.com/jobs/data-analyst-jobs-in-pune/",
    "Kolkata":    "https://internshala.com/jobs/data-analyst-jobs-in-kolkata/",
    "Ahmedabad":  "https://internshala.com/jobs/data-analyst-jobs-in-ahmedabad/",
    "Remote":     "https://internshala.com/jobs/work-from-home-data-analyst-jobs/",
}

# Skills list
SKILL_KEYWORDS = [
    "python", "sql", "excel", "power bi", "tableau",
    "r programming", "machine learning", "statistics",
    "pandas", "numpy", "mysql", "postgresql", "mongodb",
    "azure", "aws", "google cloud", "git",
    "data visualization", "communication", "spark",
    "scikit-learn", "deep learning", "nlp", "powerpoint"
]

# Start session

session = requests.Session()

print("Initialising session...")

session.get(
    "https://internshala.com",
    headers=HEADERS,
    timeout=10
)

time.sleep(2)

# Storage

all_jobs = []
seen_titles_companies = set()

# Main scraping loop
for city, url in SEARCH_URLS.items():

    print(f"\nScraping: {city}...")

    try:
        response = session.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        print(f"  Status : {response.status_code}")

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        job_cards = soup.find_all(
            "div",
            class_="individual_internship"
        )

        print(f"  Cards  : {len(job_cards)}")

        # Process each job card
        for card in job_cards:

            # Job Title
            try:
                title = card.find(
                    "a",
                    class_="job-title-href"
                ).get_text(strip=True)

            except:
                title = "N/A"

            # Company
            try:
                company_div = card.find(
                    "div",
                    class_="company-name"
                )

                if company_div:
                    company = company_div.get_text(
                        strip=True
                    )

                else:
                    company = card.find(
                        "div",
                        class_="generic_company"
                    ).get_text(strip=True)

                # Remove accidental title duplication
                company = company.replace(
                    title,
                    ""
                ).strip()

            except:
                company = "N/A"

            # Deduplication
            dedup_key = f"{title}|{company}"

            if dedup_key in seen_titles_companies:
                continue

            seen_titles_companies.add(dedup_key)

            # Location
            try:
                loc = card.find(
                    "a",
                    id="location_names"
                )

                if loc:
                    location = loc.get_text(
                        strip=True
                    )

                else:
                    location = city

            except:
                location = city

            # Experience
            try:
                experience = "N/A"

                exp_items = card.find_all(
                    "div",
                    class_="row-1-item"
                )

                for item in exp_items:

                    text = item.get_text(
                        " ",
                        strip=True
                    )

                    if (
                        "year" in text.lower()
                        or
                        "fresher" in text.lower()
                    ):
                        experience = text
                        break

            except:
                experience = "N/A"

            # Date Posted
            try:
                date_div = card.find(
                    "div",
                    class_="status-inactive"
                )

                if date_div:
                    date_posted = date_div.get_text(
                        " ",
                        strip=True
                    )

                else:
                    date_posted = "N/A"

            except:
                date_posted = "N/A"

            # Skills Extraction

            card_text = card.get_text(
                separator=" ",
                strip=True
            ).lower()

            found_skills = [
                skill
                for skill in SKILL_KEYWORDS
                if skill in card_text
            ]

            skills = (
                ", ".join(found_skills)
                if found_skills
                else "N/A"
            )

            # Save row

            all_jobs.append({
                "Job Title":   title,
                "Company":     company,
                "Location":    location,
                "Search City": city,
                "Experience":  experience,
                "Date Posted": date_posted,
                "Skills":      skills,
            })

    except Exception as e:
        print(f"  Error: {e}")

    # Ethical scraping delay
    time.sleep(2)

# Create DataFrame
df = pd.DataFrame(all_jobs)

# Final Output
print(f"\n{'='*50}")
print(f"Total unique jobs : {len(df)}")
print(f"Cities covered    : {df['Search City'].nunique()}")
print(f"{'='*50}")

print("\nSample rows:")
print(
    df[
        [
            "Job Title",
            "Company",
            "Location",
            "Experience",
            "Date Posted"
        ]
    ].head(10).to_string()
)

print("\nJobs per city:")
print(
    df["Search City"]
    .value_counts()
    .to_string()
)

# Save CSV
df.to_csv(
    "data/raw_jobs.csv",
    index=False
)

print("\n✅ Saved to data/raw_jobs.csv")
