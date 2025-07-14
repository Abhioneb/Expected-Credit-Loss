# Expected Credit Loss App

This is a minimal working prototype for computing and visualizing an Expected Credit Loss (ECL) curve by segment, with a simple action recommendation.

## Setup (Windows)

1. **Install Python** (3.10+), ensure `python --version` works.
2. **Clone or download** this repo 

3. Open PowerShell, `cd` into the folder, then:
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   pip install --upgrade pip
   pip install -r requirements.txt