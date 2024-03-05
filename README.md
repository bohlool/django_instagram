# Instagram Clone Backend

This is the backend of an Instagram clone project developed using Django REST framework. It provides APIs and
functionalities for direct messaging, posts, stories, likes, and comments.

## Technologies Used

- Django
- Django REST framework
- Celery
- Sqlite
- JWT Authentication

## Installation

1. Clone the repository:
   git clone https://github.com/bohlool/django_instagram.git
2. Install dependencies:
   cd django_instagram
   python -m venv venv
   .\venv\Scripts\activate
   pip install -r requirements.txt
3. Set up environment variables by copying `sample_settings.py` to  `local_settings.py`  file and adding the following:
   ADMIN_URL
   SECRET_KEY
   DEBUG
   ALLOWED_HOSTS
   STATIC_ROOT
   MEDIA_ROOT
   SIMPLE_JWT
4. Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5. Start the server:
   python manage.py runserver

## API Endpoints

- [user_profiles.md](doc%2Fuser_profiles.md) : Profile management endpoints
- [content.md](doc%2Fcontent.md) : Content-related endpoints
- [user_activities.md](doc%2Fuser_activities.md) : Like-related and Comment-related endpoints
- [direct.md](doc%2Fdirect.md) : Direct messaging endpoints

## Contributing

If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.

## Acknowledgements

Special thanks to the Django and Django REST framework communities for their contributions to this project.
