from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import login_required, current_user
from app import db
from app.models import Project
from app.forms import ProjectForm

projects_bp = Blueprint('projects', __name__)

# List all projects
@projects_bp.route('/projects')
@login_required
def list_projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)

# Create a new project (business only)
@projects_bp.route('/projects/new', methods=['GET', 'POST'])
@login_required
def new_project():
    if current_user.role != 'business':
        abort(403)
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            business_id=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully!', 'success')
        return redirect(url_for('projects.list_projects'))
    return render_template('new_project.html', form=form)

# Delete a project (business only)
@projects_bp.route('/projects/delete/<int:project_id>', methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    if project.business_id != current_user.id:
        abort(403)
    db.session.delete(project)
    db.session.commit()
    flash('Project removed successfully.', 'success')
    return redirect(url_for('projects.list_projects'))