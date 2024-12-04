# Password Genie - Your Key to Secure Passwords

A user-friendly and customizable password generator built with **Tkinter** in Python.  
Password Genie allows you to create secure passwords based on your preferences for length, uppercase letters, numbers, and special characters.

## Features
- **Custom Length**: Specify the length of the password.
- **Character Options**: 
  - Include or exclude uppercase letters.
  - Include or exclude numbers.
  - Include or exclude special characters.
- **Live Result Display**: Generated password is displayed instantly.
- **Modern Design**: Responsive, visually appealing UI with interactive buttons.
- **Error Handling**: Validates user input and displays helpful messages.

## Color Scheme
- **Background**: Soft Sky Blue (`#E3F2FD`)
- **Text Colors**:
  - Title: Royal Blue (`#1565C0`)
  - Labels: Deep Gray (`#424242`)
- **Button Colors**:
  - Generate Button: Green (`#4CAF50`) with White text
  - Active Button: Slightly darker Green (`#45A049`) for hover effects

## Screenshot
[Click Here](screenshot.png)

## Getting Started

### Prerequisites
- Python 3.x installed on your system.
- `tkmacosx` module for enhanced button design. Install using:
  ```bash
  pip install tkmacosx
### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/subham0822/passgenie-tkinter.git

2. Navigate to the project directory:
   ```bash
   cd passgenie-tkinter

3. Run the Python script:
   ```bash
   python pass-gen-tkinter.py

## Usage
- Enter the desired length of the password.
- Choose your preferences for including uppercase letters, numbers, and special characters using the radio buttons.
- Click the "Generate Password" button to create a password based on your preferences.
- The generated password will be displayed on the screen.

## Project Structure
  ```bash
  password-genie/
│
├── pass-gen-tkinter.py   # Main Python script
├── screenshot.png      # Sample screenshot
├── pass-gen-icon.png   # Icon file
├── README.md           # Project documentation
└── .gitignore          # Git ignore file
```
## How It Works
1. Password Generation:
  - Combines selected character pools (lowercase, uppercase, numbers, and special characters).
  - Ensures at least one character from each selected category.
  - Randomly fills the remaining length using random.choices().
2. Error Handling:
  - Displays a friendly message for invalid input, such as non-numeric length.

## Contributing
Contributions are welcome! Feel free to submit a pull request or raise an issue for suggestions or improvements.
