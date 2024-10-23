
# Polling Application

## Description

The Polling Application is a web-based platform that allows users to create and participate in polls. Users can register, log in, create questions, add options, and vote on their preferred options. This application aims to provide a simple and intuitive interface for gathering opinions and feedback through polling.

## Features

- User Registration and Authentication
- Create and Manage Poll Questions
- Add Options to Polls
- Vote on Poll Options
- View Poll Results
- Delete Poll Questions and Options

## Technologies Used

- Python 3.x
- Django 5.x
- HTML, CSS (Materialize CSS)
- JavaScript
- SQLite (default database)

## Getting Started

### Prerequisites

- Python 3.x
- Django 5.x
- Virtual Environment (recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/polling-application.git
   cd polling-application
   ```

2. Create and activate a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):

   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

7. Open your web browser and go to `http://127.0.0.1:8000` to access the application.

## Usage

- Register for an account to create and manage polls.
- Log in to vote on existing polls or to create new ones.
- Users can view poll results and manage their created polls.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-YourFeature`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-YourFeature`.
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


