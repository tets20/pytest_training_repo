from model.kontact import Kontact

def test_delete_first_kontact(app):
    if app.kontact.count() == 0:
        app.kontact.create(Kontact(firstname="test"))
    app.kontact.delete_first_kontact()
