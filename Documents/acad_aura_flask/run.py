from app import create_app
from app.models.user import User

app = create_app()

# Import db from app after creating app
from app import db

with app.app_context():
    # Create all tables
    db.create_all()
    
    # Create admin user if it doesn't exist
    admin = User.query.filter_by(email='admin@acadaura.com').first()
    if not admin:
        admin_user = User(
            username='admin',
            email='admin@acadaura.com',
            is_admin=True,
            is_faculty=True,  # Admin can also access faculty portal
            is_approved=True
        )
        admin_user.set_password('admin123')
        db.session.add(admin_user)
        db.session.commit()
        print("✅ Admin user created!")
        print("📧 Email: admin@acadaura.com")
        print("🔑 Password: admin123")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)