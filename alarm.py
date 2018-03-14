import sys
import datetime
import time
import os


__author__ = "salmansamie"


def alarm():
    if (sys.argv[2]).isdigit() and sys.argv[1] in ['hr', 'hrs']:
        given_value = int(sys.argv[2])*60*60
        while given_value > 0:
            print("\nTimer set for (hours)  : " + sys.argv[2])
            print("Time Remaining to exp: " + str(datetime.timedelta(seconds=given_value)))
            time.sleep(1)
            os.system('tput reset')
            given_value -= 1
        os.system('say -v Samantha "Salman, Your countdown timer has expired."')

    elif (sys.argv[2]).isdigit() and sys.argv[1] in ['m', 'min']:
        given_value = int(sys.argv[2])*60
        while given_value > 0:
            print("\nTimer set for (minutes)  : " + sys.argv[2])
            print("Time Remaining to exp    : " + str(datetime.timedelta(seconds=given_value)))
            time.sleep(1)
            os.system('tput reset')
            given_value -= 1
        os.system('say -v Samantha "Salman, Your countdown timer has expired."')

    elif (sys.argv[2]).isdigit() and sys.argv[1] in ['s', 'sec']:
        given_value = int(sys.argv[2])
        while given_value > 0:
            print("\nTimer set for (seconds)  : " + sys.argv[2])
            print("Time Remaining to exp    : " + str(datetime.timedelta(seconds=given_value)))
            time.sleep(1)
            os.system('tput reset')
            given_value -= 1
        os.system('say -v Samantha "Salman, Your countdown timer has expired."')        # explore: say -v \?

    else:
        print("\nAttention: Incorrect Timer Value!!")
        helper()


def helper():
        print("\nEnter an alarm time in any of the below formats:\n"
              "\n +---------+-----------+----------+"
              "\n | Hour    |  Second   | Min      |"
              "\n |---------+-----------+----------|"
              "\n | hr 6    |  s 10     | m 15     |"
              "\n | hrs 6   |  sec 10   | min 15   |"
              "\n +---------+-----------+----------+\n"
              )


if __name__ == '__main__':
    try:
        if len(sys.argv) == 1:
            helper()
            exit(1)

        str_input = (sys.argv[1]).lower()
        arg_valid = ['hr', 'hrs', 's', 'sec', 'm', 'min']

        if str_input == '-h' or str_input == '--help' or str_input == '--h':
            helper()

        elif str_input not in arg_valid:
            print("\nAttention: Incorrect Option!!")
            helper()

        elif str_input in arg_valid:
            alarm()

    except KeyboardInterrupt:
        print("\nExited.")
        exit(1)