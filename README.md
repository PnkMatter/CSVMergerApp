# 📊 CSV Merger App

A simple and interactive web app built with [Streamlit](https://streamlit.io) to merge multiple CSV files with the same structure into a single file.

---

## 🚀 Features

- Upload multiple `.csv` files
- Automatically merges data, keeping **only the header from the first file**
- Preview of the combined data
- Download the final unified CSV file

---

## 🧰 Technologies Used

- Python 3.x
- [Streamlit](https://streamlit.io)
- Pandas
- NumPy

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/PnkMatter/CSVMergerApp.git
cd CSVMergerApp
```
### 2. (Optional) Create a virtual environment

python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # Linux/Mac

### 3. Install dependencies

pip install -r requirements.txt

## ▶️ How to Run

Use the command below:

streamlit run main.py

## 📁 Example Usage

    Upload two or more .csv files

    Preview the merged data table

    Download the unified CSV file

## 📝 Notes

    All CSV files must have the same columns in the same order.

    Only the header from the first file is preserved.

    Files with different structures may cause merge errors.

## 📄 License

This project is licensed under the MIT License.

## 🤝 Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## 👨‍💻 Author

Gabriel Ramalho Resende
📫 LinkedIn | 🐙 GitHub

