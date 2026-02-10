from flask import Blueprint, render_template, jsonify

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    """Main landing page."""
    return render_template('index.html')

@bp.route('/health')
def health():
    """Health check endpoint for monitoring."""
    return jsonify({'status': 'healthy'}), 200
