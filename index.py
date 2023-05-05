class Property:
    def __init__(self, address, owner):
        self.address = address
        self.owner = owner
        self.units = []

    def add_unit(self, unit):
        self.units.append(unit)

    def view_units(self):
        for unit in self.units:
            print(f"{unit.size} sq. ft. unit, rent: {unit.rent}, deposit: {unit.deposit}")

class Unit:
    def __init__(self, size, rent, deposit):
        self.size = size
        self.rent = rent
        self.deposit = deposit
        self.tenant = None

    def assign_tenant(self, tenant):
        self.tenant = tenant

class Tenant:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def view_profile(self):
        print(f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}")

class Invoice:
    def __init__(self, tenant, amount):
        self.tenant = tenant
        self.amount = amount

    def generate_receipt(self):
        print(f"Receipt for {self.tenant.name}: KES {self.amount} paid.")

class PropertyManagementSystem:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def view_properties(self):
        for property in self.properties:
            print(f"Property address: {property.address}\nOwner: {property.owner}")
            property.view_units()

    def add_tenant(self, tenant, unit):
        unit.assign_tenant(tenant)

    def invoice_tenant(self, tenant):
        invoice = Invoice(tenant, 200)
        invoice.generate_receipt()

    def send_invoice(self, tenant):
        # Simulating sending an email using Gmail
        import smtplib, ssl
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "your_email_address@gmail.com"  # Enter your address
        receiver_email = tenant.email  # Enter tenant email address
        password = input("Type your password and press enter: ")
        message = f"""\
        Subject: Property Management Invoice
        
        Dear {tenant.name},
        
        This is a reminder that your monthly rent and garbage service fee is KES 200.
        
        Thank you,
        Property Management System"""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)

    def generate_report(self):
        # Generate a report with list of properties, units, tenants, invoices and receipts
        for property in self.properties:
            print(f"Property address: {property.address}\nOwner: {property.owner}")
            for unit in property.units:
                print(f"{unit.size} sq. ft. unit, rent: {unit.rent}, deposit: {unit.deposit}")
                if unit.tenant:
                    unit.tenant.view_profile()
                    self.invoice_tenant(unit.tenant)
                    receipt = Invoice(unit.tenant, 200)
                    receipt.generate_receipt()
#this is the end 
<incl
