

---

# 🌦️ Django Weather App

A sleek and easy-to-use weather web application built with **Django** that allows users to check the current weather of any city around the world. The app fetches real-time data from **OpenWeatherMap** to provide weather information like temperature, humidity, wind speed, and more.

---

## 🌟 Features

- 🌍 **Search Weather by City**: Easily search for any city around the world and get up-to-date weather details.
- 🌡️ **Detailed Weather Data**: Includes temperature, weather conditions, humidity percentage, wind speed, and more to give a full overview of the current weather.
- 🎨 **User-Friendly Interface**: The app has a clean and easy-to-navigate design, providing a smooth experience even for new users.

---

## 🛠️ Requirements

To run this project on your local machine, you'll need the following:

- **Python 3.x**: Python is the programming language used for this app.
- **Django 4.x**: Django is the web framework used to build the app. It is already included in the project, but if needed, you can install it manually.

---

## 🚀 Installation

Follow these detailed steps to set up and run the app locally on your machine:

### 1️⃣ Clone the Repository

First, you need to clone the project repository to your local machine. Open your terminal (command prompt) and run the following commands:

```bash
# Clone the repository to your local machine
git clone https://github.com/paradox974333/djangoweatherapp.git

# Navigate into the project directory
first do:
cd djangoweatherapp
then do:
cd weather_project
```

This will download the project files from GitHub and open the project folder on your local machine.

### 2️⃣ Set Up a Virtual Environment

A virtual environment is important because it isolates the project's dependencies from your global Python setup. To create and activate the virtual environment, run:

```bash
# Create a virtual environment named 'myenv'
python -m venv myenv

# Activate the virtual environment
# On MacOS/Linux:
source myenv/bin/activate

# On Windows:
myenv\Scripts\activate
```

Once activated, the virtual environment will ensure that any Python packages you install will only affect this project and not other Python projects you may have.

### 3️⃣ Install Django and Other Dependencies

Since this project does not include a `requirements.txt` file, you'll need to install Django manually. Run the following command to install Django in your virtual environment:

```bash
# Install Django
pip install django
pip install requests

```

You may need additional dependencies in the future, depending on the project's updates, but for now, Django is the only required package.

### 4️⃣ Apply Migrations

Django uses a database to store data, and applying migrations sets up the necessary database tables for the app. Run this command to apply the migrations:

```bash
# Apply migrations to set up the database schema
python manage.py migrate
```

This step is essential to ensure that the app has the correct database structure for things like user sessions, data storage, and other features.

### 5️⃣ Run the Development Server

Now that everything is set up, you can run the Django development server to start using the app. Run the following command:

```bash
# Start the development server
python manage.py runserver
```

This will start the app on your local machine. You can access it by opening a web browser and navigating to:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 🎯 Usage

Once the server is running, you can start using the app by following these simple steps:

1. **Search for a City**: In the search bar at the top of the page, type the name of any city you'd like to check the weather for.
2. **View the Weather**: After entering the city, the app will display live weather information, including:
   - **Temperature**: Current temperature in Celsius or Fahrenheit.
   - **Weather Conditions**: Whether it's sunny, cloudy, rainy, etc.
   - **Humidity**: The percentage of moisture in the air.
   - **Wind Speed**: How fast the wind is blowing in meters per second (or other units).

---

## ✅ Running Tests

To ensure that the application is working as expected, it's a good idea to run the tests that come with the project. Running tests helps verify that all features and functionalities are working correctly. You can run the tests with the following command:

```bash
# Run the test suite to check for errors
python manage.py test
```

If the tests pass, everything is set up correctly!

---

## 🤝 Contributing

We welcome contributions! If you want to improve the app, follow these steps:

1. **Fork the Repository**: Click on the "Fork" button at the top-right of the repository page on GitHub to create a copy of the project under your own account.
2. **Create a New Branch**: Open your terminal and create a new branch for the changes you want to make:

   ```bash
   git checkout -b feature-name
   ```

3. **Make Your Changes**: Edit the files and make your desired improvements or fixes.
4. **Commit Your Changes**: After making the changes, commit them with a message describing the changes:

   ```bash
   git commit -m 'Add feature or fix issue'
   ```

5. **Push Your Branch**: Push the changes to your GitHub repository:

   ```bash
   git push origin feature-name
   ```

6. **Submit a Pull Request**: Go to your GitHub repository and click "Compare & Pull Request." Provide a description of your changes and submit the pull request.

---

## 📄 License

This project is licensed under the **MIT License**. You can freely use, modify, and distribute the project, but please refer to the [LICENSE](LICENSE) file for detailed terms.

---

## 👨‍💻 Author

This project was developed with ❤️ by **[MANOJ L](https://github.com/paradox974333)**.

---

