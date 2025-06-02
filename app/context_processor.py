from datetime import datetime

def inject_globals():
    return {
        'current_year': datetime.now().year
    }