# Portfolio Application

A modern, responsive portfolio website built with Flask and Bootstrap 5.

## Features

- **Responsive Design**: Mobile-first design that works across all devices
- **Modern UI**: Clean, professional interface with smooth transitions
- **Card-based Layout**: Organized sections for skills, projects, experience, and education
- **Carousel Navigation**: Interactive carousel for browsing different content sections
- **Customizable**: Easy configuration through environment variables and config files

## Quick Start

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Setup

1. **Clone and Navigate**
   ```bash
   cd portfolio-app
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv me2u-venv-flask
   source me2u-venv-flask/bin/activate  # On Windows: me2u-venv-flask\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -e .
   ```

4. **Run the Application**
   ```bash
   python main.py
   ```

5. **Access Your Portfolio**
   Open your browser to `http://localhost:5000`

## Configuration

### Environment Variables

Configure your application using environment variables:

```bash
export FLASK_ENV=development
export FLASK_DEBUG=True
export PORT=5000
```

### Application Settings

Edit `app/config.py` to customize:

- **App Name**: Change the application title
- **Debug Settings**: Toggle debug mode
- **Port Configuration**: Set the server port

### Content Customization

#### Personal Information
Update your details in `app/data/personal_data.py`:
- Name, title, and contact information
- Social media links
- Professional summary

#### Skills and Technologies
Modify `app/data/skills_data.py`:
- Technical skills with proficiency levels
- Tools and frameworks
- Certifications

#### Projects Portfolio
Edit `app/data/projects_data.py`:
- Project descriptions and links
- Technologies used
- Screenshots and demos

#### Experience History
Update `app/data/experience_data.py`:
- Work history and achievements
- Education background
- Professional timeline

### Visual Customization

#### Colors and Styling
- **Main Styles**: Edit `app/static/css/style.css`
- **Utility Classes**: Modify `app/static/css/utility.css` 
- **Card Components**: Customize `app/static/css/cards.css`
- **Custom Overrides**: Use `app/static/css/custom.css`

#### Layout Components
- **Navigation**: Templates in `app/templates/components/`
- **Page Layouts**: Base templates in `app/templates/page_layouts/`
- **Content Pages**: Individual pages in `app/templates/pages/`

## Deployment

### Docker Deployment

1. **Build Docker Image**
   ```bash
   ./build-push.sh
   ```

2. **Run Container**
   ```bash
   docker run -p 5000:5000 portfolio-app
   ```

### Production Setup

1. **Configure Environment**
   ```bash
   export FLASK_ENV=production
   export FLASK_DEBUG=False
   ```

2. **Use Production Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 main:app
   ```

## Project Structure

```
app/
├── config.py              # Application configuration
├── routes.py              # URL routing and view functions
├── context_processor.py   # Template context processors
├── error_handlers.py      # Error handling
├── universal_card.py      # Card component logic
├── data/                  # Content and data files
├── static/               # CSS, JS, images
├── templates/            # Jinja2 templates
└── utils/                # Utility functions
```

## Troubleshooting

### Common Issues

**Port Already in Use**
```bash
# Find and kill process using port 5000
lsof -ti:5000 | xargs kill -9
```

**CSS Changes Not Showing**
- Hard refresh your browser (Ctrl+Shift+R or Cmd+Shift+R)
- Clear browser cache
- Check browser developer tools for cached resources

**Import Errors**
```bash
# Reinstall in development mode
pip install -e .
```

**Virtual Environment Issues**
```bash
# Recreate virtual environment
rm -rf me2u-venv-flask
python -m venv me2u-venv-flask
source me2u-venv-flask/bin/activate
pip install -e .
```

### Development Tips

- **Live Reloading**: Set `FLASK_DEBUG=True` for automatic reloading
- **Template Debugging**: Enable debug mode to see detailed error messages
- **CSS Development**: Use browser developer tools to test changes before updating files
- **Content Updates**: Restart the server after modifying data files

## Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the project structure and configuration
3. Ensure all dependencies are properly installed
4. Verify environment variables are set correctly

## License

See LICENSE file for details.
