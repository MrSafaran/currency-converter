# 💱 Currency Converter
A simple and interactive **Currency Converter** built with [Streamlit](https://streamlit.io/) and Python.  
This tool lets you quickly convert between different world currencies using **real-time exchange rates** fetched from [ExchangeRate-API](https://www.exchangerate-api.com/).

With its clean dashboard, you can:
- 🔢 Enter an amount to convert  
- 🌐 Select base and target currencies  
- 📊 Instantly view the converted value  
- 🔄 Get up-to-date rates from the API  

Perfect for educational demos, financial dashboards, or quick daily conversions.


## Features 
- **Real-time Exchange Rates**: Fetches live rates from ExchangeRate-API.  
- **Streamlit Dashboard**: Clean and user-friendly interface.  
- **Currency Support**: Choose from 150+ world currencies.  
- **Instant Conversion**: See results immediately after entering an amount.  
- **Command-Line Option**: Run directly from terminal for quick checks.  
- **Caching**: Uses in-memory caching to reduce redundant API calls.  


## Project Structure
```
.
├── LICENSE
├── README.md
├── requirements.txt
└── src
    ├── app.py       # Streamlit dashboard
    ├── main.py      # Core logic 
    └── constants.py  
```
## 📦 Requirements

- Python 3.9+ (recommended)
- Streamlit >= 1.25.0  
- requests >= 2.31.0  
- cachetools >= 5.6.0

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## ⚙️ Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/currency-converter.git
   cd currency-converter
    ```
2. **(Optional) Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Linux / Mac
    venv\Scripts\activate      # On Windows
    ```
3. **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4. **Set up environment variable for API key**
    ```bash
    export EXCHANGERATE_API_KEY=your_api_key_here  # On Linux / macOS
    setx EXCHANGERATE_API_KEY "your_api_key_here"  # On Windows

    ```
> Get a free API key from [ExchangeRate-API](https://www.exchangerate-api.com/)


## 🚀 Usage

### 1. Run with Streamlit (Web Dashboard)
```bash
streamlit run src/app.py
```
Opens an interactive dashboard in your default browser.

Enter the amount, select base and target currencies, and view the converted value instantly.

### 2. Run from Command-Line Interface (CLI)
```bash
python src/main.py
```
Follow the prompts to input:

- Base currency
- Target currency
- Amount to convert

The converted value will be printed directly in the terminal.

## 📝 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for more details.


## 👤 Authors 

- **Mohammadreza Safaran** – [GitHub](https://github.com/MrSafaran)