import frappe

@frappe.whitelist()
def greeting(name=None):
    """Example API endpoint.
    Usage:
      /api/method/hello_world.api.greeting
      /api/method/hello_world.api.greeting?name=Kresten
    """
    return f"Hello, {name}!" if name else "Hello, ERPNext!"
