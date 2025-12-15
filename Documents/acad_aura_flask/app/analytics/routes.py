from flask import Blueprint, render_template

analytics_bp = Blueprint('analytics', __name__, template_folder='templates')


@analytics_bp.route('/')
def index():
    # Minimal analytics overview placeholder
    sample_charts = {
        'attendance': {'labels': ['Mon', 'Tue', 'Wed'], 'data': [80, 85, 82]},
        'grades': {'labels': ['A', 'B', 'C'], 'data': [40, 35, 25]},
    }
    return render_template('admin/dashboard.html', charts=sample_charts)
