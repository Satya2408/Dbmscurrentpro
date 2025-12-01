from flask import Blueprint, render_template
from flask_login import login_required, current_user

faculty_bp = Blueprint('faculty', __name__)

@faculty_bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_faculty and not current_user.is_admin:
        return "Access denied. Faculty privileges required."
    return render_template('faculty/dashboard.html')

@faculty_bp.route('/my_courses')
@login_required
def my_courses():
    if not current_user.is_faculty and not current_user.is_admin:
        return "Access denied. Faculty privileges required."
    return render_template('faculty/my_courses.html')

@faculty_bp.route('/students')
@login_required
def students():
    if not current_user.is_faculty and not current_user.is_admin:
        return "Access denied. Faculty privileges required."
    return render_template('faculty/students.html')

@faculty_bp.route('/attendance')
@login_required
def attendance():
    if not current_user.is_faculty and not current_user.is_admin:
        return "Access denied. Faculty privileges required."
    return render_template('faculty/attendance.html')

@faculty_bp.route('/grades')
@login_required
def grades():
    if not current_user.is_faculty and not current_user.is_admin:
        return "Access denied. Faculty privileges required."
    return render_template('faculty/grades.html')