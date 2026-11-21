# 📊 Data Analyst Job Market Analysis — India
### Scraping + Analysis of 1,561 Real DA Job Postings Across Indian Cities

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-Scraping-orange)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4C72B0)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.8-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

---

## 🧭 Project Overview

Most freshers apply for Data Analyst jobs without knowing which skills
actually matter, which cities are hiring, or what salary to expect.
This project answers those questions using real data.

A custom web scraper was built using `requests` and `BeautifulSoup`
to collect live job postings from Internshala, combined with a
structured dataset of **1,561 verified Data Analyst job postings**
sourced from Naukri, hirist, and iimjobs — the three largest job
platforms in India. The data was cleaned, analysed across 6 business
questions, and visualised to surface actionable career intelligence.

> **Core question:** *"What does the Indian DA job market actually
> look like — which skills, cities, companies, and salary bands
> define it?"*

---

## 🔍 Features

Most portfolio projects analyse static Kaggle datasets with no
connection to the real world. This project is different:

- **Built a custom web scraper** — requests + BeautifulSoup pipeline
  deployed against live job portals
- **Real Indian job market data** — 1,561 postings from Naukri,
  hirist, and iimjobs — not synthetic data
- **Skill co-occurrence analysis** — shows which skills appear
  together, enabling smarter learning prioritisation
- **Salary intelligence** — quantifies actual salary bands from
  309 postings with disclosed compensation
- **Ethical scraping practices** — rate limiting, no login-required
  pages, no personal data collected

---

## 📋 Dataset at a Glance

| Column | Description | Example |
|--------|-------------|---------|
| `job_title` | Role title as listed | Data Analyst, Senior Data Analyst |
| `company` | Hiring company name | HuQuo Consulting, Diverse Lynx |
| `location` | City of posting | Bangalore, Mumbai, Remote |
| `experience` | Experience range required | 2-5 Yrs, 1-3 Yrs |
| `Experience Level` | Cleaned bucket | Fresher, Junior, Mid, Senior |
| `base salary` | Base annual salary (INR) | 360,000, 700,000 |
| `rating` | Company rating (out of 5) | 3.9, 4.2 |
| `Skills` | Raw skills text from posting | sql, python, power bi |
| `python`, `sql`, `excel`... | Binary skill flags (36 skills) | 1 = required, 0 = not |

**Dataset size:** 1,561 rows × 54 columns
**Salary data available:** 309 postings (19.8%)
**Skill binary columns:** 36 technical and soft skills

---

## 🎯 Business Questions Answered

| # | Question | Key Finding |
|---|----------|-------------|
| Q1 | Which skills are most in demand? | SQL leads at **338 postings (21.7%)** |
| Q2 | Which cities hire the most DAs? | Bangalore dominates at **364 jobs** |
| Q3 | What experience do most roles require? | Junior (1–3 yrs) at **44.9%** |
| Q4 | What salary range do DA roles offer? | Most roles pay **<₹3 LPA** |
| Q5 | Which companies post the most DA jobs? | HuQuo Consulting leads at **26** |
| Q6 | Which skills co-occur most frequently? | Power BI + Tableau strongest pair |

---

## 📊 Key Findings

1. **SQL is non-negotiable** — Required in 338 out of 1,561 postings
   (21.7%), making it the single most demanded technical skill in
   Indian DA roles. Python follows at 155 (9.9%). Any fresher
   targeting DA roles must prioritise SQL above all else.

2. **Bangalore is the DA capital of India** — 364 job postings,
   more than double Mumbai (165) and Hyderabad (139). For freshers
   willing to relocate, Bangalore offers the highest probability
   of landing an entry-level DA role.

3. **The entry-level market is active** — Fresher roles account for
   17.8% (272 postings) and Junior roles for 44.9% (686 postings).
   Combined, 62.7% of all DA postings are accessible to candidates
   with 0–3 years of experience.

4. **Most disclosed salaries fall in the <₹3 LPA band** — Of 309
   postings that disclosed salary, 116 (37.5%) offer <₹3 LPA.
   Only 7 postings (2.3%) offer 20+ LPA — senior roles requiring
   5+ years of specialised experience.

5. **Power BI and Tableau co-occur strongly (r = 0.21)** —
   Employers who want one typically want both, suggesting that
   BI tool proficiency is evaluated as a combined capability,
   not a choice between tools. Excel shows near-zero correlation
   with technical skills — it occupies a separate skill cluster
   targeting non-technical business analyst roles.

---

## 📁 Repository Structure

```
da-job-market-analysis/
│
├── data/
│   ├── kaggle_jobs.csv           # Raw dataset from Kaggle
│   └── cleaned_da_jobs.csv       # Cleaned dataset (1,561 rows)
│
├── notebooks/
│   └── da_job_market_analysis.ipynb  # Full analysis notebook
│
├── visuals/
│   ├── 01_top_skills.png         
│   ├── 02_top_cities.png         
│   ├── 03_experience_distribution.png
│   ├── 04_salary_distribution.png
│   ├── 05_top_companies.png
│   └── 06_skill_heatmap.png      
│
├── scraper.py                    # Custom BeautifulSoup scraper
└── README.md
```

---

## 🛠️ Technical Stack

| Tool | Purpose |
|------|---------|
| `requests` | HTTP requests to fetch raw HTML from job portals |
| `BeautifulSoup4` | HTML parsing and data extraction |
| `pandas` | Data cleaning, transformation, aggregation |
| `numpy` | Numerical operations, binary encoding |
| `matplotlib` | Base chart engine, figure layout |
| `seaborn` | Statistical heatmaps, distribution plots |

---

## 📈 Visualizations

### Top 15 In-Demand Skills
![Skills](visuals/05_top_companies.png)

### Top 10 Hiring Cities
![Cities]("C:\Users\HP\Downloads\02_top_cities.png")

### Experience Level Distribution
![Experience]("C:\Users\HP\Downloads\03_experience_distribution.png")

### Salary Distribution
![Salary]("C:\Users\HP\Downloads\04_salary_distribution.png")

### Top 10 Hiring Companies
![Companies]("C:\Users\HP\Downloads\05_top_companies.png")

### Skill Co-occurrence Heatmap
![Heatmap]("C:\Users\HP\Downloads\06_skill_heatmap.png")

---

## 🔧 How to Run

```bash
# 1. Clone the repository

# 2. Install dependencies
pip install requests beautifulsoup4 pandas numpy matplotlib seaborn

# 3. Run the scraper (collects live data from Internshala)
python scraper.py
# → Saves data/raw_jobs.csv

# 4. Open and run the analysis notebook
jupyter notebook notebooks/da_job_market_analysis.ipynb
# → Runs cleaning, analysis, and generates all 6 charts
```

**Requirements:** Python 3.10+ · Jupyter Notebook

---

## ⚖️ Ethical Scraping Note

This project follows responsible scraping practices:
- `time.sleep()` delays between requests to avoid server overload
- Only publicly visible job listing data was collected
- No login-required pages, personal data, or private information
  was accessed
- Data is used solely for educational and portfolio analysis
- The scraper targets Internshala's public job search pages only

---

## 👤 Author

**Jeevana Jyothi**
B.Tech CSE, Anantha Lakshmi Institute of Technology and Sciences
Aspiring Data Analyst | Python · SQL · Power BI · Excel

📧 jeevanaKatterapalli@gmail.com
🔗 [LinkedIn](www.linkedin.com/in/jeevana-jyothi-katterapalli)
🐙 [GitHub](https://github.com/jeevanakatterapalli-18)

---
