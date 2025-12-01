from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models.user import User

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/dashboard')
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    # Get counts for dashboard
    total_users = User.query.count()
    pending_users = User.query.filter_by(is_approved=False, is_admin=False).count()
    approved_users = User.query.filter_by(is_approved=True).count()
    
    return render_template('admin/dashboard.html', 
                         total_users=total_users,
                         pending_users=pending_users,
                         approved_users=approved_users)

@admin_bp.route('/pending')
@login_required
def pending_users():
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    # Get pending users
    pending_users = User.query.filter_by(is_approved=False, is_admin=False).all()
    return render_template('admin/pending_users.html', pending_users=pending_users)

@admin_bp.route('/approve_user/<int:user_id>')
@login_required
def approve_user(user_id):
    if not current_user.is_admin:
        flash('Access denied.', 'error')
        return redirect(url_for('main.index'))
    
    user = User.query.get(user_id)
    if user:
        user.is_approved = True
        db.session.commit()
        flash(f'User {user.username} has been approved!', 'success')
    else:
        flash('User not found!', 'error')
    
    return redirect(url_for('admin.all_users'))

@admin_bp.route('/make_faculty/<int:user_id>')  # ADD THIS MISSING ROUTE
@login_required
def make_faculty(user_id):
    if not current_user.is_admin:
        flash('Access denied.', 'error')
        return redirect(url_for('main.index'))
    
    user = User.query.get(user_id)
    if user:
        user.is_faculty = True
        user.is_approved = True  # Auto-approve when making faculty
        db.session.commit()
        flash(f'User {user.username} is now a faculty member!', 'success')
    else:
        flash('User not found!', 'error')
    
    return redirect(url_for('admin.all_users'))

@admin_bp.route('/users')
@login_required
def all_users():
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('main.index'))
    
    # Get ALL users from database
    all_users = User.query.all()
    return render_template('admin/all_users.html', users=all_users)

@admin_bp.route('/calendar')
@login_required
def calendar():
    if not current_user.is_admin:
        flash('Access denied. Admin privileges required.', 'error')
        return redirect(url_for('main.index'))
    return render_template('admin/calendar.html')

# Debug route to see all users in database
@admin_bp.route('/debug_users')
@login_required
def debug_users():
    if not current_user.is_admin:
        return "Access denied"
    
    all_users = User.query.all()
    result = "All Users in Database:<br>"
    for user in all_users:
        result += f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Approved: {user.is_approved}, Admin: {user.is_admin}, Faculty: {user.is_faculty}<br>"
    return result