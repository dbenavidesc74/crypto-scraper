import subprocess
from scraper import run_scraper

def main():
    # 1. Run the scraper
    print("Running scraper...")
    file = run_scraper()

    # 2. If the CSV file was generated, launch the dashboard
    if file:
        print("Launching dashboard in browser...")
        subprocess.run(["streamlit", "run", "analysis.py"])

if __name__ == "__main__":
    main()
