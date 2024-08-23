# Django Quiz Application

A simple Django-based quiz application that allows users to create an account, log in, and take quizzes. The application includes features for administrators to add questions and provides feedback on users' answers.

## Features

- User authentication (sign up, log in, log out)
- Admin interface for adding and managing quiz questions
- Quiz-taking interface for users
- Real-time feedback on quiz performance
- Error handling for unanswered questions
- Tracks how many times a user has taken the quiz

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Joeson-Suomie/quiz_app.git
   cd quiz_app


2. **Set up a virtual environment:**
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`


3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt

   
   
4. **Set up the database:**

   ```bash
   python manage.py makemigrations
   python manage.py migrate

   

5. **Create a superuser to access the admin panel:**

   ```bash
   python manage.py createsuperuse

   
   
6. **Run the development server:**

   ```bash
   python manage.py createsuperuser

   

7. **Access the application:**

   Admin panel: http://127.0.0.1:8000/admin/
   Application: http://127.0.0.1:8000/quiz/


## Usage


## Admin Panel

  - Log in with your superuser credentials.
  - Add questions to the quiz by navigating to the Quiz section in the admin panel.
    
## User Interface

  - Register a new account or log in with an existing one.
  - Start the quiz by clicking on the "Take Quiz" button.
  - Answer all questions and submit the quiz to get feedback on your performance.
  - Visit Profile page to track how many times you have attempt the quiz.
    
## Customization

  - Modify templates/base.html for global styling and layout changes.
  - Update static/styles.css for custom styling of the quiz interface.

## Contributing

Contributions are welcome! Please follow these steps:

  - Fork the repository.
  - Create a new branch (git checkout -b feature-branch).
  - Commit your changes (git commit -m 'Add a feature').
  - Push to the branch (git push origin feature-branch).
  - Open a pull request.



## Contact

For any questions or issues, please open an issue in the repository or contact me directly at joesuomie@gmail.com.


