# Legal Case Articles - Flask Application

A Flask-based web application for creating, managing, and displaying articles about legal cases. This application transforms the static HTML site into a dynamic platform where you can add multiple articles with the same professional design and structure.

## Features

- **Dynamic Article Management**: Add, view, and manage multiple legal case articles
- **Beautiful UI**: Maintains the original professional design with dark/light theme support
- **Structured Content**: Organized sections for case details, timeline, arguments, analysis, and verdict
- **Easy Article Creation**: User-friendly form for adding new articles with all necessary fields
- **JSON-Based Storage**: Simple file-based storage system for articles
- **Responsive Design**: Works seamlessly on desktop and mobile devices

## Project Structure

```
html-site-for-articles/
├── app.py                      # Flask application main file
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── data/
│   └── articles.json          # Articles data storage
├── templates/
│   ├── base.html              # Base template with styling
│   ├── index.html             # Homepage listing all articles
│   ├── article.html           # Individual article display
│   └── add_article.html       # Form for adding new articles
└── static/                    # Static assets (CSS, JS) - optional
```

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone <repository-url>
   cd html-site-for-articles
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask development server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. **Stop the server**:
   Press `Ctrl+C` in the terminal

## Usage Guide

### Viewing Articles

- Navigate to the homepage (`/`) to see a list of all articles
- Click on any article to view its full content
- Use the navigation controls at the top to browse
- Toggle between light and dark themes using the switch in the navigation bar

### Adding a New Article

1. Click the **"+ Add New Article"** button on the homepage
2. Fill in the article form with the following sections:

   - **Basic Information**: Title, delivery date, bench size, introduction
   - **Case Details**: Plaintiff, defendant, case type, year range, ruling
   - **Judges**: Add multiple judges with their names, initials, and opinions
   - **Timeline Events**: Add key events in the case progression
   - **Acts & Citations**: List relevant acts and legal citations
   - **Arguments**: Petitioner's and respondent's arguments
   - **Analysis & Verdict**: Court's analysis, verdict points, and ratio decidendi
   - **Additional Metadata**: Case number, counsel, hearing dates

3. Click **"Submit Article"** to save
4. You'll be redirected to the homepage where your new article appears

### Editing the Design

The application uses inline CSS in the base template (`templates/base.html`). To customize:

- **Colors**: Modify the CSS variables in the `:root` selector
- **Fonts**: Change the Google Fonts import or font-family properties
- **Layout**: Adjust the container widths, padding, and margins
- **Dark Mode**: Customize colors in the `body.dark-mode` selector

## Data Storage

Articles are stored in `data/articles.json` as a JSON array. Each article contains:

- Basic information (title, dates, bench size)
- Case details (plaintiff, defendant, type)
- Judge information (names, opinions)
- Timeline of events
- Legal arguments from both sides
- Court's analysis and verdict
- Metadata (case number, counsel, etc.)

### Sample Article Structure

```json
{
  "title": "Case Name v. Respondent",
  "delivered_date": "January 1, 2024",
  "bench_size": "5-Judge",
  "intro": "Brief introduction...",
  "judges": [
    {
      "name": "Judge Name",
      "initials": "JN",
      "opinion": "yes"
    }
  ],
  ...
}
```

## Customization

### Changing the Secret Key

For production deployment, change the secret key in `app.py`:

```python
app.secret_key = 'your-secure-secret-key-here'
```

### Modifying the Port

To run on a different port, edit the last line in `app.py`:

```python
app.run(debug=True, host='0.0.0.0', port=5000)  # Change 5000 to your preferred port
```

### Database Integration

Currently, the app uses JSON file storage. To use a database:

1. Install SQLAlchemy: `pip install flask-sqlalchemy`
2. Create database models in `app.py`
3. Replace `load_articles()` and `save_articles()` functions

## Deployment

### Production Considerations

1. **Set debug mode to False**:
   ```python
   app.run(debug=False)
   ```

2. **Use a production server** (e.g., Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn app:app
   ```

3. **Set environment variables**:
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   ```

4. **Use a proper database** instead of JSON files

### Deployment Platforms

- **Heroku**: Create a `Procfile` with `web: gunicorn app:app`
- **PythonAnywhere**: Upload files and configure WSGI
- **AWS/GCP**: Deploy using their respective app services
- **Docker**: Create a Dockerfile for containerization

## Troubleshooting

### Common Issues

1. **Port already in use**:
   - Change the port in `app.py` or stop the process using that port

2. **Module not found**:
   - Ensure virtual environment is activated
   - Run `pip install -r requirements.txt`

3. **Articles not saving**:
   - Check file permissions for the `data` directory
   - Ensure the directory exists

4. **Template not found**:
   - Verify the `templates` directory exists
   - Check template file names match the routes

## Contributing

Feel free to fork this project and submit pull requests for improvements!

## License

See the LICENSE file for details.

## Original Design

This application is based on a professionally designed HTML template for legal case articles. The Flask conversion maintains all the original styling and functionality while adding dynamic content management capabilities.

## Support

For issues or questions, please open an issue in the repository.
