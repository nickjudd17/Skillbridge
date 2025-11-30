from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

dashboard_bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@dashboard_bp.route('/')
@login_required
def dashboard():
    if current_user.role == 'student':
        return render_template('student_dashboard.html')
    elif current_user.role == 'business':
        return render_template('business_dashboard.html')
    else:
        return redirect(url_for('index'))