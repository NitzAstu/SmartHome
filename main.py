# allow using voice commend
import speech_recognition as sr
# allow to the assistant to return an answer
# text to speech library
import pyttsx3
import pyaudio
import GUI
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, \
    QGridLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from datetime import time, datetime, timedelta
import time

# בנינו משתנה בשם listener שיאזין לנו ויבין מה אומרים
listener = sr.Recognizer()
engine = pyttsx3.init()


def ListenToTheUser(source):  # פונקציה שמשתמשת בapi של גוגל בעזרת הסיפרייה voice recognition ומחזירה את מה שאמרנו
    voice = listener.listen(source)
    # voice to text
    command = listener.recognize_google(voice)
    return command


def talk(text):  # פונקציה ששולחים לה טקסט והיא מתרגמת את הטקסט ל-voice בעזרת הסיפריה pyttsx3
    engine.say(text)  # המחשב עונה text to speech
    engine.runAndWait()


def SmartHome(on_click=None):
    p1.__init__(1, "nothing")
    with sr.Microphone() as source:
        print('listening..')
        # voice = listener.listen(source)
        # voice to text
        c = ListenToTheUser(source)
        print(c)
        # command = listener.recognize_google(voice)  # בתוך המשתנה שמור מה שאמרנו אבל בכתב(גוגל הופך את זה לכתב)
        if 'cold' in c:
            talk('Would you like me to turn on the air conditioner on heat?')
            c1 = ListenToTheUser(source)
            if 'yes' in c1:
                talk('ok, turned on')
                p1.__init__(1, "heat")
            else:
                print('no')
        elif 'called' in c:
            talk('Did you mean that you are cold?')
            c1 = ListenToTheUser(source)
            if 'yes' in c1:
                talk('Would you like me to turn on the air conditioner on heat?')
                c2 = ListenToTheUser(source)
                if 'yes' in c2:
                    talk('ok, turned on')
                    p1.__init__(1, "heat")
                else:
                    print('no')
            else:
                talk('ok. have a nice day')
        elif 'help' in c:
            # countForHelp = 1
            print('help')
            talk('Would you like me to call for help?')
            try:
                c1 = ListenToTheUser(source)
                if 'yes' in c1 or 'help' in c1:
                    print('yes')
                    # countForHelp = 0
                    # countForHelp == 0
                    talk('ok, i am calling for help')
                    p1.__init__(1, "help")
                elif 'no' in c1:
                    # countForHelp == 0
                    # p1.__init__(1, "help")
                    print("no")
            except:
                talk('i am calling for help')
                p1.__init__(1, "help")

            # elif countForHelp == 1:
            # print("countfor help")
            # countdown(10)
            # p1.__init__(1, "help")
        elif 'hot' in c:
            talk('Would you like me to turn on the air conditioner on cold?')
            c1 = ListenToTheUser(source)
            if 'yes' in c1:
                print('yes')
                p1.__init__(1, "cold")
                talk('ok, turned on')
            else:
                print('no')

        elif 'boring' in c or 'bored' in c or 'TV' in c:
            print('boring')
            talk('Would you like me to turn on the TV?')
            c1 = ListenToTheUser(source)
            print(c1)
            if 'yes' in c1:
                p1.__init__(1, "tv")
                talk('which channel do you like to watch?')
                c1 = ListenToTheUser(source)
                print(c1)
                if 'one' in c1 or '1' in c1:
                    print("chanel 1")
                    talk('ok, you chose channel one')
                    p1.__init__(1, "channel one")

                elif 'two' in c1 or '2' in c1:
                    talk('ok, you chose channel two')
                    p1.__init__(1, "channel two")

                elif 'three' in c1 or '3' in c1 or 'tree':
                    talk('ok, you chose channel three')
                    p1.__init__(1, "channel three")
        elif 'turn on the light' in c:
            talk('turning on the light')
            p1.__init__(1, "light on")

        elif 'turn off the light' in c:
            talk('turning off the light')

            p1.__init__(1, "light off")

        elif 'dark' in c or 'darkness' in c:
            print('light')
            talk('Would you like me to turn on the light?')
            c1 = ListenToTheUser(source)
            if 'yes' in c1:
                talk('ok, i am turning on the light')
                print('turn on the light')
                p1.__init__(1, "light on")
            else:
                print('no')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GUI.App()
    ex.__init__(0)
    ex.show()
    p1 = ex
    SmartHome()
    sys.exit(app.exec_())
