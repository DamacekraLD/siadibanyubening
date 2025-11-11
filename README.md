# README

## Project Overview
This is a Flask-based web application for managing pharmacy, doctor, and patient data.

## Project Structure

```
.
├── app.py                              # Main Flask application
├── env/                                # Python virtual environment
├── static/                             # Static files (CSS, JavaScript, images)
│   ├── bootstrap/                      # Bootstrap framework files
│   │   ├── css/
│   │   └── js/
│   ├── css/
│   │   └── styles.css                  # Custom stylesheets
│   ├── img/                            # Image assets
│   └── js/                             # JavaScript files
└── templates/                          # HTML templates
    ├── base.html                       # Base template
    ├── index.html                      # Home page
    ├── navbar.html                     # Navigation bar component
    ├── scripts.html                    # Scripts component
    ├── test.html                       # Test page
    ├── apotek591/                      # Pharmacy management
    │   ├── data_apotek.html
    │   └── form_apotek.html
    ├── dokter598/                      # Doctor management
    │   ├── data_dokter.html
    │   └── form_dokter.html
    └── pasien616/                      # Patient management
        ├── data_pasien.html
        └── form_pasien.html
```

## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. **Activate the virtual environment:**
   ```bash
   # On Windows
   env\Scripts\activate
   
   # On macOS/Linux
   source env/bin/activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

```bash
python app.py
```

The application will start and be accessible at `http://localhost:5000` (or the configured port).

## Features

- **Pharmacy Management (apotek591)** - View and manage pharmacy data
- **Doctor Management (dokter598)** - View and manage doctor information
- **Patient Management (pasien616)** - View and manage patient records

## Project Structure Details

- **app.py** - Main Flask application entry point
- **templates/** - HTML templates for different modules
  - Base layout templates for consistent UI
  - Module-specific data display and forms
- **static/** - Static assets
  - Bootstrap for responsive design
  - Custom CSS styles
  - JavaScript utilities

## License
[Add your license information here]

## Support
[Add support/contact information here]