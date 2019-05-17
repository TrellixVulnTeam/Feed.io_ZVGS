# Import the Firebase service
import firebase_admin
from firebase_admin import auth


# Initialize the default app
default_app = firebase_admin.initialize_app(cred)
print(default_app.name)  # "[DEFAULT]"

# Retrieve services via the auth package...
# auth.create_custom_token(...)