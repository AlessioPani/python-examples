# A desktop notifier app runs on your system and it will be used
# to send you notifications after every specific interval of time.

from pynotifier import Notification
from time import sleep


def activate_notification(description, type):
    # Activate the notification with a description provided
    # by the user.
    if type == 'L':
        urgency = Notification.URGENCY_LOW
    elif type == 'N':
        urgency = Notification.URGENCY_NORMAL
    else:
        urgency = Notification.URGENCY_CRITICAL
    
    Notification(
        title='Alarm',
        description=description,
        icon_path='alarm.ico',
        duration=5,  # Duration in seconds
        urgency=urgency
    ).send()


if __name__ == "__main__":
    description = input('\nInsert a description for your alarm: \n=> ')
    try:
        type = input('\nInsert the urgency of your alarm '
                     '[L: low - N: normal - C: critical] \n=> ')
        if type.upper() not in ['L', 'N', 'C']:  # Low, Normal and Critical
            raise ValueError

        wait = float(input('\nInsert when you want to activate '
                           'this alarm [seconds or submultiples]: \n=> '))

        print("\nWaiting...")
        sleep(wait)  # Before activate the alarm waits some time
        activate_notification(description, type)

    except ValueError:
        print('\nPlease insert an allowed value!')
