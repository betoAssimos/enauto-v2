from catalystwan.session import create_manager_session
import urllib3
urllib3.disable_warnings()
 
# The SDK handles:
#   - Session cookie management
#   - XSRF token fetching
#   - Automatic re-authentication on session expiry
#   - SSL verification config
session = create_manager_session(
    url="10.10.20.90",
    username="admin",
    password="C1sco12345",
    port=443
)
 
print(f"Connected to vManage: {session.server_name}")
print(f"Session active: {session.session_type}")
 
# ── Always close the session when done ────────────────────────
# This invalidates the JSESSIONID on the server
session.close()