import os
from app import create_app, socketio

# Top-level Flask app for Gunicorn
app = create_app()

# Optional: keep this block for local dev
if __name__ == '__main__':
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get('PORT', '5000'))
    
    socketio.run(
        app,
        host=host,
        port=port,
        allow_unsafe_werkzeug=True,
        use_reloader=False,
        log_output=True
    )
