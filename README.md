# 🚀 How to Run This Django Project Locally

## 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

---

## 2. Create a virtual environment

### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Apply migrations

```bash
python manage.py migrate
```

---

## 4. Run the development server

```bash
python manage.py runserver
```

---

## 5. Open in browser

Go to:

```
http://127.0.0.1:8000/
```

---

## 🛠️ Additional Notes

* Make sure Python (3.x) is installed
* If you face issues, try:

```bash
pip install --upgrade pip
```

---

## 🔐 Environment Variables (if any)

If your project uses `.env`, create one:

```bash
cp .env.example .env
```

Then update values as needed.
