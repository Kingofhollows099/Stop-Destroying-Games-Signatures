import schedule
import time
from scrapeSignatures import scrape_signatures

def job():
    print("Running signature scraping job...")
    scrape_signatures()

# Schedule the job to run every hour
schedule.every().hour.do(job)

print("Scheduler started. The scraping job will run every hour.")
job()

while True:
    schedule.run_pending()
    time.sleep(60)


