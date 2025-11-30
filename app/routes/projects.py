from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Project
from app.forms import ProjectForm

projects_bp = Blueprint('projects', __name__, url_prefix='/projects')

@projects_bp.route('/new', methods=['GET', 'POST'])
@login_required
def new_project():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            description=form.description.data,
            posted_by=current_user.id
        )
        db.session.add(project)
        db.session.commit()
        flash('Project posted successfully!', 'success')
        return redirect(url_for('projects.list_projects'))
    return render_template('new_project.html', form=form)

@projects_bp.route('/')
def list_projects():
    projects = Project.query.all()
    return render_template('projects.html', projects=projects)