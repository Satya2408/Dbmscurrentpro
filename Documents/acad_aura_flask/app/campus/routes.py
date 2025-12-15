from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

campus_bp = Blueprint('campus', __name__, template_folder='templates')


@campus_bp.route('/wallet')
@login_required
def wallet():
    # Minimal wallet context for the demo/dev server
    wallet = type('W', (), {'balance': 0.0})()
    transactions = []
    return render_template('campus/wallet.html', wallet=wallet, transactions=transactions)


@campus_bp.route('/canteen')
@login_required
def canteen():
    # Simple placeholder
    items = [
        {'name': 'Sandwich', 'price': 2.5},
        {'name': 'Coffee', 'price': 1.2},
    ]
    return render_template('campus/wallet.html', wallet=type('W', (), {'balance': 0})(), transactions=[], items=items)


@campus_bp.route('/add_money', methods=['POST'])
@login_required
def add_money():
    try:
        amount = float(request.form.get('amount', '0'))
    except Exception:
        amount = 0
    if amount <= 0:
        flash('Invalid amount', 'error')
    else:
        flash(f'Added ${amount:.2f} to wallet (demo).', 'success')
    return redirect(url_for('campus.wallet'))
