# FlowMasters ETL Project

This is a beginner-friendly **retail sales data engineering pipeline** built using Python and PostgreSQL. The goal is to simulate a real-world ETL process from raw retail data to structured insights.

##  Project Structure

```
flowmasters_ent/
├── data/                  # Raw data files (Sales, Purchase, Product, etc.)
├── scripts/               # Python scripts for ingestion and transformation
├── .gitignore             # Files Git should ignore
├── README.md              # Project overview
└── requirements.txt       # Python dependencies (optional)
```
##  Team Members

- Temitope Adedeji (GitHub: [@TemiAdedeji](https://github.com/TemiAdedeji))
- Tobi
- Mohammed (GitHub: [@MLMoh](https://github.com/MLMoh))

##  Tools & Technologies

- Python (`pandas`, `SQLAlchemy`)
- PostgreSQL (raw, staging, warehouse layers)
- Power BI (for dashboards – pending)
- Apache Airflow (for ETL orchestration – planned)
- VS Code (IDE)

##  Datasets Used

- `SalesTransaction.csv` (140MB)  
- `PurchaseTransaction.csv`  
- `Store.csv`  
- `Product.csv`  
- `Vendor.csv`

> Due to GitHub’s 100MB file limit, `SalesTransaction.csv` is not included in this repo.

**Download the full datasets here:** (https://drive.google.com/file/d/1Xrcr2SgB3LA7Jk8iwUD6JZZKrhjuLum9/view?usp=drive_link)

## How to Use This Project

### 1. Clone the repository
```bash
git clone https://github.com/TemiAdedeji/FlowMaster-ETL-project.git
cd FlowMaster-ETL-project
```

### 2. Download the datasets
Get the full data files from the Google Drive link somewhere above and place them in the `data/` folder.

### 3. Install dependencies
```bash
pip install pandas sqlalchemy psycopg2
```
### 4. Run ETL scripts
```bash
python scripts/load_raw_data.py
# (More scripts to come as project progresses)
```
### 5. Connect Power BI (optional)
Use PostgreSQL as a data source and connect to the dimensional model tables for reporting.

## Business Questions We’re Exploring

- What are the top-selling products by store and day?
- What product combinations are frequently bought together?
- Which vendors are the most reliable?
- What are the sales patterns by time of day?

## How to Contribute

- Temitope will add you as a collaborator
- Clone the repo, create a new branch for your work
- Push changes and open a pull request  
  _(or push directly if you’re added)_


## 📄 License

This project is for educational and collaborative learning purposes only.
