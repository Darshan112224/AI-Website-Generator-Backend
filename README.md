# AI-Website-Generator-Backend

This is the backend for the AI Website Generator, a tool that automatically generates websites based on user inputs and selected technologies. The backend is built using Django and Flask with Transformers-based AI models for code generation.

# 📌Features
✅ RESTful API for handling website generation requests
✅ AI-powered code generation using StarCoder2
✅ User authentication and project management
✅ Database integration with PostgreSQL / MongoDB
✅ Error handling and request validation

# 🛠️Tech Stack
Backend: Django + Flask
AI Model: bigcode/starcoder2-15b
Database: PostgreSQL / MongoDB
## Libraries:
transformers (for AI model)
torch (for deep learning)
Flask / Django REST framework
gunicorn (for deployment)
🔧 Installation
1️⃣ Clone the Repository
git clone https://github.com/Darshan112224/AI-Website-Generator-Backend.git  
cd AI-Website-Generator-Backend
2️⃣ Set Up a Virtual Environment
python -m venv env  
source env/bin/activate  # Mac/Linux  
env\Scripts\activate     # Windows  
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Set Up the Database
PostgreSQL
Create a database and update the DATABASES setting in settings.py.
5️⃣ Run the Server
python manage.py runserver  # Django    
The backend will start at http://127.0.0.1:5000/.

# 🎯Usage
Generate a Website
Endpoint: POST /api/generate_website/
Request Body (JSON):

json
Copy
Edit
{
  "title": "E-commerce Website",
  "framework": "React.js",
  "features": ["Login", "Payment Gateway", "Dashboard"]
}
Response:

json
Copy
Edit
{
  "status": "success",
  "message": "Website generated successfully.",
  "download_url": "http://127.0.0.1:5000/static/generated_site.zip"
}

# 📜API Endpoints
Method	Endpoint	Description
POST	/api/generate_website/	Generates a website using AI
GET	/api/status/	Checks API status
POST	/api/auth/register/	Registers a new user
POST	/api/auth/login/	Logs in a user
# 🔥Contributing
Want to improve this project? Feel free to fork and submit a pull request!
git clone https://github.com/Darshan112224/AI-Website-Generator-Backend.git
git checkout -b feature-branch
git commit -m "Added a new feature"
git push origin feature-branch
