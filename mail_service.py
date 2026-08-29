# from __future__ import print_function
# from googleapiclient.discovery import build
# from apiclient import errors
# from httplib2 import Http
# from email.mime.text import MIMEText
# import base64
# from google.oauth2 import service_account

# # Email variables. Modify this!
# EMAIL_FROM = 'support@ayninfotech.com'
# EMAIL_SUBJECT = 'Query on AYN Infotech Ltd Website'
# EMAIL_TO = 'cto@ayninfotech.com'
# EMAIL_CONTENT = 'Test'


# def create_content(name, email, query, mobile):
#     content = "Hi " + name + ",\n\nGreetings!\n\nThank you for showing interest in AYN Infotech.\n\nWe have received a query from you. We will get in touch with you shortly.\n\nEmail = " + email + "\nName = " + name + "\nMobile = " + mobile + "\nQuery = " + query + "\n\nBest Regards.\n\nAYN Infotech Ltd\nayninfotech.com\n\n"
#     return content


# def create_document_content(name, job_title, phone, work_email, company, no_of_employees, product):
#     content = "Hi " + name + ",\n\nGreetings from AYN Infotech Limited!\n\nThank you for showing interest in " + product + ".\n\nYou will be contacted very soon by one of our executives using the following details.\n\nName = " + name + "\nJob Title = " + job_title + "\nPhone = " + str(phone) + "\nWork Email = " + work_email + "\nCompany = " + company + "\n# Employees = " + no_of_employees + "\n\nBest Regards.\n\nAYN Infotech Ltd\nayninfotech.com\n\n"
#     return content


# def create_message(to, message_text, subject=EMAIL_SUBJECT, sender=EMAIL_FROM):
#     """Create a message for an email.

#     Args:
#     sender: Email address of the sender.
#     to: Email address of the receiver.
#     subject: The subject of the email message.
#     message_text: The text of the email message.

#     Returns:
#     An object containing a base64url encoded email object.
#     """
#     message = MIMEText(message_text)
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject
#     return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


# def send_message(service, message, user_id='me'):
#     """Send an email message.
#     Args:
#     service: Authorized Gmail API service instance.
#     user_id: User's email address. The special value "me"
#     can be used to indicate the authenticated user.
#     message: Message to be sent.
#     Returns:
#     Sent Message.
#     """
#     try:
#         message = (service.users().messages().send(userId=user_id, body=message)
#                    .execute())
#         # print('Message Id: %s' % message['id'])
#         return message
#     except errors.HttpError as error:
#         print('An error occurred: %s' % error)


# def service_account_login():
#     SCOPES = ['https://www.googleapis.com/auth/gmail.send']
#     SERVICE_ACCOUNT_FILE = 'ayn_cred.json'

#     credentials = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#     delegated_credentials = credentials.with_subject(EMAIL_FROM)
#     service = build('gmail', 'v1', credentials=delegated_credentials)
#     return service



from __future__ import print_function
from email.mime.text import MIMEText
import base64

# NOTE:
# Google API imports (googleapiclient, apiclient, google.oauth2) are
# intentionally NOT imported at the top of this file.
#
# Reason: Vercel's Python serverless runtime has a packaging conflict
# with google-api-python-client (it tries to import "six.moves" from
# a shadowed/vendored copy and fails with
# "ModuleNotFoundError: No module named 'six.moves'").
#
# If these imports happen at module load time, the ENTIRE Flask app
# fails to import and the whole website crashes with a 500 error.
#
# By moving the imports inside the functions that actually need them,
# the website itself will always load fine. Only the specific action
# of sending an email will fail (and that failure is already caught
# by try/except in components/__init__.py's get_mail_service()).

# Email variables. Modify this!
EMAIL_FROM = 'support@ayninfotech.com'
EMAIL_SUBJECT = 'Query on AYN Infotech Ltd Website'
EMAIL_TO = 'cto@ayninfotech.com'
EMAIL_CONTENT = 'Test'


def create_content(name, email, query, mobile):
    content = "Hi " + name + ",\n\nGreetings!\n\nThank you for showing interest in AYN Infotech.\n\nWe have received a query from you. We will get in touch with you shortly.\n\nEmail = " + email + "\nName = " + name + "\nMobile = " + mobile + "\nQuery = " + query + "\n\nBest Regards.\n\nAYN Infotech Ltd\nayninfotech.com\n\n"
    return content


def create_document_content(name, job_title, phone, work_email, company, no_of_employees, product):
    content = "Hi " + name + ",\n\nGreetings from AYN Infotech Limited!\n\nThank you for showing interest in " + product + ".\n\nYou will be contacted very soon by one of our executives using the following details.\n\nName = " + name + "\nJob Title = " + job_title + "\nPhone = " + str(phone) + "\nWork Email = " + work_email + "\nCompany = " + company + "\n# Employees = " + no_of_employees + "\n\nBest Regards.\n\nAYN Infotech Ltd\nayninfotech.com\n\n"
    return content


def create_message(to, message_text, subject=EMAIL_SUBJECT, sender=EMAIL_FROM):
    """Create a message for an email.

    Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

    Returns:
    An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, message, user_id='me'):
    """Send an email message.
    Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.
    Returns:
    Sent Message.
    """
    from apiclient import errors

    try:
        message = (service.users().messages().send(userId=user_id, body=message)
                   .execute())
        # print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)


def service_account_login():
    from googleapiclient.discovery import build
    from google.oauth2 import service_account

    SCOPES = ['https://www.googleapis.com/auth/gmail.send']
    SERVICE_ACCOUNT_FILE = 'ayn_cred.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    delegated_credentials = credentials.with_subject(EMAIL_FROM)
    service = build('gmail', 'v1', credentials=delegated_credentials)
    return service
