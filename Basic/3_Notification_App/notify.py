# A desktop notifier app runs on your system and it will be used
# to send you notifications after every specific interval of time.

from pynotifier import Notification
from time import sleep


def activate_notification(description):
    # Activate the notification with a description provided
    # by the user.
    Notification(
        title='Alarm',
        description=description,
        icon_path='alarm.ico',
        duration=10,  # Duration in seconds
        urgency=Notification.URGENCY_CRITICAL
    ).send()


if __name__ == "__main__":
    description = input('Insert a description for your alarm: \n=> ')
    wait = float(input('Insert when you want to activate '
                       'this alarm [seconds or submultiples]: \n=> '))
    print("\nWaiting...")
    sleep(wait)  # Before activate the alarm waits some time
    activate_notification(description)
