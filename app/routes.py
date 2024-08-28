from app import app

@app.route('/')
def index():
    return "Welcome to the Retail Fashion Intelligence Platform"