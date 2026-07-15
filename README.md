# 🌦️ Weather API Django Project

A weather web application built using Django that allows users to search for weather information, view search history, and manage user accounts.

## 🚀 Features

- User registration and login
- Search weather details by city
- View current temperature, humidity, and weather conditions
- Store weather search history
- User authentication system
- Responsive user interface using HTML and CSS

## 🛠️ Tech Stack

- Python
- Django
- HTML5
- CSS3
- SQLite
- Weather API

## 📂 Project Structure

```
weather-project/
│── weatherapi/
│── weatherapp/
│── templates/
│── manage.py
│── .gitignore
│── README.md
```

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Aaradhana964/weather-project.git
```

### 2. Navigate to the project folder

```bash
cd weather-project
```

### 3. Create a virtual environment

```bash
python -m venv weather
```

### 4. Activate the virtual environment

#### Windows

```bash
weather\Scripts\activate
```

#### macOS/Linux

```bash
source weather/bin/activate
```

### 5. Install dependencies

```bash
pip install django requests python-dotenv
```

### 6. Create a `.env` file

```env
API_KEY=your_weather_api_key
```

### 7. Apply migrations

```bash
python manage.py migrate
```

### 8. Run the server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 📌 Future Improvements

- Five-day weather forecast
- Dark mode
- Profile page
- Weather analytics dashboard

## 👩‍💻 Author

**Aaradhana Prajapati**

GitHub: https://github.com/Aaradhana964

---

⭐ If you like this project, give it a star.
