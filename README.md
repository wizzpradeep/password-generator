# Password Generator

A password generator application that allows users to create secure passwords with customizable options. The application supports real-time generation of passwords and stores them in a database for future use. Additionally, users can specify the inclusion of numbers and special characters in the generated passwords.

# Features

- Real-Time Password Generation: Passwords are generated instantly as the user adjusts the settings.
- Customizable Length: Passwords can be generated with lengths ranging from 8 to 40 characters.
- Character Options: Users can include numbers, symbols, or both in the password.
- Save for Later: Generated passwords can be saved in the database for future use.
- WebSocket Integration: Real-time interaction through WebSockets for immediate feedback on password generation.
- Secure Storage: Passwords are saved securely in the database, making it easy to retrieve them later.

# Installation

1. Clone the repository:

```bash
git clone https://github.com/wizzpradeep/password-generator
```

2. Navigate into the project directory:

```bash
cd password-generatorX
```

3. Create and activate a virtual environment:

```bash
python -m venv .env
.\.env\Scripts\activate # On Windows
source .env/bin/activate # On macOS/Linux
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

5. Run the application:

```bash
python manage.py runserver
```

# Usage

- Generate Password: Adjust the length (8–40 characters) and choose whether to include numbers or symbols.
- Save Password: After generating a password, click the "Save" button to store it in the database.
- Retrieve Saved Passwords: Access the database to view your previously saved passwords.
- Real-Time Updates: Passwords are generated in real time based on the selected options.
