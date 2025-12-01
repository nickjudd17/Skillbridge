from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Application, Project
from app.forms import ApplicationForm

applications_bp = Blueprint('applications', __name__, url_prefix='/applications')

# Student applies to a project
@applications_bp.route('/apply/<int:project_id>', methods=['GET', 'POST'])
@login_required
def apply(project_id):
    form = ApplicationForm()
    project = Project.query.get_or_404(project_id)

    if form.validate_on_submit():
        application = Application(
            project_id=project.id,
            applicant_id=current_user.id,
            cover_note=form.cover_note.data,
            status="pending"
        )
        db.session.add(application)
        db.session.commit()
        flash('Application submitted successfully!', 'success')
        return redirect(url_for('projects.list_projects'))

    return render_template('apply.html', form=form, project=project)

# Student views their own applications
@applications_bp.route('/')
@login_required
def list_applications():
    applications = Application.query.filter_by(applicant_id=current_user.id).all()
    return render_template('applications.html', applications=applications)

# Business views applications for their own project
@applications_bp.route('/manage/<int:project_id>')
@login_required
def manage_applications(project_id):
    project = Project.query.get_or_404(project_id)

    if current_user.role != 'business' or project.business_id != current_user.id:
        flash("You are not authorized to manage this project's applications.", "danger")
        return redirect(url_for('projects.list_projects'))

    applications = Application.query.filter_by(project_id=project.id).all()
    return render_template('manage_applications.html', project=project, applications=applications)

# Business updates application status
@applications_bp.route('/update/<int:application_id>/<string:status>')
@login_required
def update_application(application_id, status):
    application = Application.query.get_or_404(application_id)
    project = Project.query.get(application.project_id)

    if current_user.role != 'business' or project.business_id != current_user.id:
        flash("You are not authorized to update this application.", "danger")
        return redirect(url_for('projects.list_projects'))

    if status in ["accepted", "rejected"]:
        application.status = status
        db.session.commit()
        flash(f"Application {status}.", "success")
    else:
        flash("Invalid status.", "danger")

    return redirect(url_for('applications.manage_applications', project_id=project.id))