"""
  Copyright (c) 2023 Yoel Castillo (@astroyoel)
 
  Este código ha sido escrito por mí, Yoel Castillo, para que lo uses de manera libre.
  He dedicado horas y horas a su creación, así que por favor, aprovéchalo.
  No se requiere atribución ni se impone ninguna restricción. Disfrútalo y úsalo bien.
"""

import serial
import pyautogui
import pyperclip
import time

# Configura el puerto serie de Arduino
ser = serial.Serial('COM4', 9600)

while True:
    try:
        # Lee los datos desde Arduino
        data = ser.readline().decode().strip()

        # Obtiene la hora actual
        current_time = time.strftime('%H:%M:%S')

        # Combina la hora actual con los datos
        data_with_time = current_time + " " + data

        # Copia los datos al portapapeles
        pyperclip.copy(data_with_time)

        # Pega los datos
        pyautogui.hotkey('ctrl', 'v')  # Pega los datos desde el portapapeles

        # Presiona la tecla "Down" para moverse al siguiente elemento
        pyautogui.press('down')

    except KeyboardInterrupt:
        break

ser.close()
