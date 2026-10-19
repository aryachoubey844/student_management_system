REST API + MySQL Console App using Python Flask.
#default_login
Id:admin/password:admin123
### Files
- `database.sql` - Run first. Creates `student_db` and users table with admin login.
- `main.py` - Console version. Connects MySQL (root/root123), login check, Add/View Students.
- `app.py` - Flask API version. Endpoints:
    - GET `/` - Check running
    - GET `/students` - All students
    - POST `/students` - Add new
    - DELETE `/students/<id>` - Delete
    - POST `/login` - Login with admin/admin123

### Run Locally
```bash
pip install -r requirements.txt
python app.py