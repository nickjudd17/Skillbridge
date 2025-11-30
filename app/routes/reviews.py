from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import db, Review, Project
from app.forms import ReviewForm

reviews_bp = Blueprint('reviews', __name__, url_prefix='/reviews')

@reviews_bp.route('/new/<int:project_id>', methods=['GET', 'POST'])
@login_required
def new_review(project_id):
    form = ReviewForm()
    project = Project.query.get_or_404(project_id)

    if form.validate_on_submit():
        review = Review(
            project_id=project.id,
            reviewer_id=current_user.id,
            rating=int(form.rating.data),
            comment=form.comment.data
        )
        db.session.add(review)
        db.session.commit()
        flash('Review submitted!', 'success')
        return redirect(url_for('projects.list_projects'))

    return render_template('new_review.html', form=form, project=project)

@reviews_bp.route('/project/<int:project_id>')
def view_reviews(project_id):
    reviews = Review.query.filter_by(project_id=project_id).all()
    return render_template('reviews.html', reviews=reviews)