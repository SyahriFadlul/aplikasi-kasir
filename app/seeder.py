from database.database import SessionLocal
from models.user import User
from models.role import Role
from models.permission import Permission
from models.pivot import RolePermission, UserRole
import bcrypt

def seed():
    db = SessionLocal()

    # 1. Create admin role
    admin_role = db.query(Role).filter_by(name='admin').first()
    if not admin_role:
        admin_role = Role(name='admin')
        db.add(admin_role)
        db.commit()
        print("✅ Admin role created.")

    # 2. Create admin permissions
    permissions = ['manage_users', 'manage_roles', 'manage_inventory', 'view_reports']
    for perm_name in permissions:
        perm = db.query(Permission).filter_by(name=perm_name).first()
        if not perm:
            perm = Permission(name=perm_name)
            db.add(perm)
            db.commit()
            print(f"✅ Permission '{perm_name}' created.")

        # Link permission to admin role
        if not db.query(RolePermission).filter_by(role_id=admin_role.id, permission_id=perm.id).first():
            rp = RolePermission(role_id=admin_role.id, permission_id=perm.id)
            db.add(rp)
            db.commit()

    # 3. Create admin user
    admin_user = db.query(User).filter_by(username='admin').first()
    if not admin_user:
        # admin_user = User(
        #     username='admin',
        #     password=bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt()),  # hashed password
        #     role='admin'
        # )
        admin_user = User(
            username='admin',
            password=bcrypt.hashpw('admin123'.encode('utf-8'), bcrypt.gensalt())
        )
        db.add(admin_user)
        db.commit()
        print("✅ Admin user created.")

    # 4. Assign role to user
    if not db.query(UserRole).filter_by(user_id=admin_user.id, role_id=admin_role.id).first():
        ur = UserRole(user_id=admin_user.id, role_id=admin_role.id)
        db.add(ur)
        db.commit()
        print("✅ Admin role assigned to user.")

    db.close()
    print("🎉 Seeding complete!")

if __name__ == "__main__":
    seed()
