# Vehicle Information Database

The Vehicle Information Database is a web-based application developed to manage and retrieve information about bikes. It provides a user-friendly interface for users to add new bikes, view existing bikes, and retrieve detailed information about a specific bike by its registration number.

## Features
- User authentication: Users can create an account and log in to the system to access the database functionalities.
- Add new bikes: Users can add new bikes to the database by providing details such as registration number, brand, model, ownership status, year of manufacture, location, kilometers driven, and more.
- View all bikes: Users can view a list of all available bikes in the database, including basic information about each bike.
- Retrieve bike details: Users can retrieve detailed information about a specific bike by providing its registration number.
- User-friendly interface: The application provides a clean and intuitive interface for seamless navigation and interaction.

## Technologies Used
- Python: The backend logic of the application is implemented using Python programming language.
- FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python.
- MongoDB: MongoDB is used as the database management system to store and retrieve bike information.
- Pydantic: Pydantic is used for data validation and modeling the API request and response objects.
- Jinja2Templates: Jinja2Templates is used for rendering HTML templates for the user interface.
- HTML/CSS: HTML and CSS are used for designing and styling the web pages.

## Getting Started
1. Clone the repository: `git clone https://github.com/your-username/vehicle-information-database.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Configure the MongoDB connection in the `config.py` file.
4. Start the application: `uvicorn main:app --reload`
5. Access the application in your browser at `http://localhost:8000`.


