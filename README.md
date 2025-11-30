# SkillBridge

SkillBridge is a Flask web application that connects students with businesses through real-world projects.  
Students can explore opportunities and apply, while businesses can post projects, review applicants, and manage applications.

## Features
- User registration and login (students and businesses)
- Role-based dashboards:
  - Students: explore projects, track applications
  - Businesses: post projects, manage applicants (accept/reject)
- Project posting and listing
- Application submission and status tracking
- Reviews system for projects
- Bootstrap-styled landing page and dashboards

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/nickjudd17/SkillBridge.git
   cd SkillBridge

2. Create a virtual environment:
   python -m venv .venv

   Activate it:
   - Windows (PowerShell): .\.venv\Scripts\activate
   - Mac/Linux: source .venv/bin/activate

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app:
   python run.py

   Visit the app at http://127.0.0.1:5000/

## Project Structure
skillbridge/
│
├── app/
│   ├── __init__.py        # App factory and routes
│   ├── models.py          # Database models
│   ├── forms.py           # WTForms for login/register/apply
│   ├── routes/
│   │   ├── auth.py        # Authentication routes
│   │   ├── projects.py    # Project routes
│   │   ├── applications.py# Application routes
│   │   └── dashboard.py   # Role-based dashboards
│   └── templates/         # HTML templates
│
├── run.py                 # Entry point
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

## Collaboration
- Fork or clone the repo
- Create a new branch for features:
  git checkout -b feature-name
- Commit and push changes
- Open a Pull Request on GitHub

## Notes
- Keep .venv/ out of GitHub (already in .gitignore)
- Use main branch for stable code
- Add teammates under Settings → Collaborators

## License
This project is currently unlicensed. Add a license if needed for open-source use.
