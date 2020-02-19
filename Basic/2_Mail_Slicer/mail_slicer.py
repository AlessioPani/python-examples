# The email slicer is a handy program to get the username and domain name
# from an email address.
# It will check if the email provided by the user is valid (with a
# combination of if/elif conditions), with the related exceptions.

import argparse  # Argument parser


def slice(email):
    # This function will print the domain and the username of an email
    username = email[:email.find('@')].lower()
    domain = email[email.find('@') + 1:].lower()
    print('Username: {} | Domain: {}'.format(username, domain))


def wrapper(email):
    # This function will check if the email is a valid one:
    # - If not, raise an exception with a message for the user;
    # - If yes, call the slice function.
    position_at = email.find('@')
    position_dot = email.find('.')

    if email.count('@') == 0 or email.count('@') > 1:
        raise ValueError('Please, insert a valid email!')
    elif email[position_at + 1:].count('.') == 0:
        raise ValueError('Please, insert a valid email!')
    else:
        slice(email)


if __name__ == "__main__":
    # Argument parser configuration and init
    parser = argparse.ArgumentParser(
        description='To get the username and domain name from an email.')
    parser.add_argument(
        '--mail',
        '-m',
        help='The email you want to slice.'
    )
    args = parser.parse_args()

    # Check if the user didn't provide the appropriate argument
    if args.mail is None:
        raise AttributeError('Please provide an email! Use -h for help.')
    else:
        wrapper(args.mail)
