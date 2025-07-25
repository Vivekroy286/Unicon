# 🎵 UNItune - Music Composer Company Platform

[![Live Site](https://unicon-0t5q.onrender.com)


**UNITUNE** is a Django-based web platform for a music composer company, offering a clean, user-friendly interface to showcase musical talent, videos, and albums. Inspired by platforms like T-Series, UNICON serves as a digital stage for music distribution and promotion.

---

## 🔗 Live Demo

👉 [Click to Visit UNITUNE](https://unicon-0t5q.onrender.com/)

---

## 🚀 Features

- 🎵 Homepage with beautiful branding layout
- 🎬 Embedded music/video content
- 🧑‍🎤 Artist and album pages (static/dynamic as per implementation)
- 📄 Clean UI with responsive design (HTML + Tailwind CSS)
- ⚙️ Django-powered backend
- 🌐 SEO-friendly HTML templates
- 🔐 (Optional scope) User login & admin panel

---

## 🛠️ Tech Stack

| Layer         | Technology             |
|---------------|-------------------------|
| Backend       | Python Django           |
| Templates     | HTML, Tailwind CSS      |
| Database      | SQLite3 (default Django DB) |
| Hosting       | Render.com              |
| Versioning    | Git + GitHub            |

---

## 🏗️ Project Structure
unicon/
├── unicon/                 # Main project folder (settings, URLs)
├── core/                   # Main app: views, models, templates
│   ├── templates/
│   └── static/
├── media/                  # Uploaded media (if applicable)
├── manage.py
├── requirements.txt
└── README.md

---

## 🧑‍💻 Getting Started Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Vivekroy286/Unicon.git
cd Unicon

### 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

### 3.Install Dependencies
pip install -r requirements.txt

### 4. Run Migrations
python manage.py runserver


Then visit http://127.0.0.1:8000/ in your browser.

Deployment

UNICON is deployed on Render:
	•	Just push to GitHub → Render auto-deploys your Django project.
	•	Static files handled using WhiteNoise or Render’s static setup.
Contributing

Have an idea or found a bug?
Please open an issue in the GitHub Issues section. Pull requests are also welcome!


License

This project is open-source under the MIT License.



Author

Developed by Vivek Roy
Let’s build more music tech together! 🎧🎹
