# ----------------------
# IMPORTS
# ----------------------

from app import create_app
from app.config import config

app = create_app()

# ----------------------
# APP ENTRY POINT
# ----------------------

# Only run the app if this file is run directly (not imported)
# Configuration is now loaded from pyproject.toml
if __name__ == "__main__":
    print(f"🚀 Starting {config.app_name} v{config.version}")
    print(f"🌐 Server running on {config.host}:{config.port}")
    print(f"🔧 Debug mode: {config.debug}")
    
    app.run(
        host=config.host,
        port=config.port,
        debug=config.debug
    )


