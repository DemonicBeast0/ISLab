# Role-Based Access Control (RBAC) Implementation

class RoleBasedAccessControl:
    def __init__(self):
        self.roles = {
            "admin": ["create", "edit", "delete", "view"],
            "editor": ["edit", "view"],
            "viewer": ["view"]
        }
        self.users = {}

    def add_user(self, username, role):
        if role in self.roles:
            self.users[username] = role
        else:
            print("Invalid role!")

    def check_access(self, username, permission):
        role = self.users.get(username)
        if role and permission in self.roles[role]:
            return f"Access granted for {username} to {permission}."
        else:
            return f"Access denied for {username} to {permission}."

# Example Usage
rbac = RoleBasedAccessControl()
rbac.add_user("Alice", "admin")
rbac.add_user("Bob", "editor")
rbac.add_user("Charlie", "viewer")

print(rbac.check_access("Alice", "delete"))  # Access granted
print(rbac.check_access("Bob", "delete"))    # Access denied
print(rbac.check_access("Charlie", "view"))  # Access granted
