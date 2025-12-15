from app import create_app


def test_wallet_page_returns_200(tmp_path):
    app = create_app({'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:', 'SECRET_KEY': 'test'})
    with app.app_context():
        from app.extensions import db
        db.create_all()
        client = app.test_client()
        # Login not needed in test context if routes are decorated; use GET to check registration
        r = client.get('/campus/wallet')
        # Should return a redirect to login (302) or 200 if test client bypasses auth
        assert r.status_code in (200, 302)
