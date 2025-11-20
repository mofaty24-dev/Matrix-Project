# Matrix Web Project

This project is a web application that allows users to interact with matrix operations through a user-friendly interface. It is built using Python and the Flask web framework.

## Project Structure

```
matrix-web-project
├── src
│   ├── app.py               # Main entry point for the web application
│   ├── matrix_project.py     # Contains the MatrixProject class and methods
│   ├── static
│   │   ├── css
│   │   │   └── styles.css    # CSS styles for the web application
│   │   └── js
│   │       └── main.js       # JavaScript for client-side interactions
│   └── templates
│       └── index.html        # HTML template for the main webpage
├── requirements.txt          # Python dependencies for the project
├── .gitignore                # Files and directories to ignore by Git
└── README.md                 # Documentation for the project
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd matrix-web-project
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python src/app.py
   ```

5. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000`.

## Usage

- Enter the number of rows and columns for the matrix.
- Input the elements of the matrix as prompted.
- Verify the matrix and proceed with operations as needed.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.

## License

This project is licensed under the MIT License.