

def test_delete_first_kontact(app):
    app.session.login(username="admin", password="secret")
    app.kontact.delete_first_kontact()
    app.session.logout()
