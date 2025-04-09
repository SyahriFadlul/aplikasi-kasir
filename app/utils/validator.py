def validate_user_input(username: str, password: str):
    errors = []

    if not username or len(username) < 3:
        errors.append("Username minimal 3 karakter")

    if ' ' in username:
        errors.append("Username tidak boleh mengandung spasi")

    if not password or len(password) < 6:
        errors.append("Password minimal 6 karakter")

    return errors
