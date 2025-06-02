# ----------------------
# IMPORTS
# ----------------------

from app import create_app

app = create_app()

# ----------------------
# APP ENTRY POINT
# ----------------------

# Only run the app if this file is run directly (not imported)
# host="0.0.0.0" allows access from any network interface
# debug=True enables auto-reloading and detailed error pages
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)


