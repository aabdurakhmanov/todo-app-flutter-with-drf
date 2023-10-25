# Todo App

This is a simple Todo app built with Flutter for the mobile front-end and Django Rest Framework (DRF) for the backend API.

## Features

- Create, update, and delete tasks.
- Mark tasks as completed.
- List tasks with filters.
- User authentication and registration (optional).

## Technologies Used

- **Flutter**: The mobile app is built using the Flutter framework, allowing for a single codebase for both Android and iOS.
- **Django Rest Framework (DRF)**: The backend API is developed using DRF, which provides powerful tools for building web APIs in Django.
- **SQLite**: The app uses SQLite as the default database for data storage.

## Installation

### Backend (DRF)

1. Clone the backend repository:
  ```shell 
  https://github.com/aabdurakhmanov/todo-app-flutter-with-drf.git
  ```

2. Navigate to the project directory:
  ```shell
  cd your-todo-app-backend
  ```

3. Create a virtual environment (recommended):
  ```shell
  python -m venv venv
  ```

4. Activate the virtual environment:
  ```shell
  source venv/bin/activate
  ```

5. Install dependencies:
  ```shell
  pip install -r requirements.txt
  ```

6. Migrate the database and create a superuser (if needed):
  ```shell
  python manage.py migrate
  python manage.py createsuperuser
  ```

7. Start the server:
  ```shell
  python manage.py runserver
  ```

### Frontend (Flutter)

1. Clone the frontend repository:
  ```shell
  https://github.com/aabdurakhmanov/todo-app-flutter-with-drf.git
  ```

2. Navigate to the project directory:
  ```shell
  cd your-todo-app-frontend
  ```

3. Install dependencies:
  ```shell
  flutter pub get
  ```

4. Run the app:
  ```shell
  flutter run
  ```

## API Endpoints

- List all tasks: `GET /api/tasks/`
- Create a new task: `POST /api/tasks/`
- Retrieve, update, or delete a task: `GET/PUT/DELETE /api/tasks/<task_id>/`

## Authentication (Optional)

You can enable user authentication for your app using DRF's built-in authentication classes. You can then use tokens, JWT, or other authentication mechanisms as per your preference.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For any questions or feedback, please contact [aabdurakhmanov](mailto:https://github.com/aabdurakhmanov).

