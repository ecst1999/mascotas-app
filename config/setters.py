from models.role import Role

class RoleSetter():

    def __init__(self, db) -> None:
        self.db = db

    def set_roles(self):

        admin = Role(rol_id=1, rol_nombre="admin")
        user = Role(rol_id=2, rol_nombre="user")

        self.db.add(admin)
        self.db.add(user)

        self.db.commit()

