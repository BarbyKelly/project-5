# Signal file added to fix messages - all of it learned from ChatGPT
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib import messages


# ---- Sign In - message toasts ----
# Sign In - message
def sign_in_toast(sender, request, user, **kwargs):
    """
    Feedback to User 'Signed in as (username)
    """
    messages.success(
        request,
        f"Signed in as {user.username}"
    )

# Connect the signal to Username
user_logged_in.connect(sign_in_toast)


# Sign Out - message
def sign_out_toast(sender, request, user, **kwargs):
    """
    Feedback to User 'Signed out'
    """
    messages.success(
        request,
        "You have signed out."
    )

# Connect the signal to Username 
user_logged_out.connect(sign_out_toast)
