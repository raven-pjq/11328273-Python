import tkinter as tk
from tkinter import messagebox
import pygame
import librosa
import numpy as np
from PIL import Image, ImageTk
import threading
import time

# Initialize pygame mixer for sound
# 初始化pygame音效混音器
pygame.mixer.init()

# Function to detect siren sound
# 函數用於檢測警報聲
def detect_siren_from_file(file_path, siren_freq_range=(600, 1500)):
    y, sr = librosa.load(file_path, sr=None)
    spectrum = np.abs(np.fft.fft(y))[:len(y)//2]
    freqs = np.fft.fftfreq(len(y), d=1/sr)[:len(y)//2]  
    detected = any((siren_freq_range[0] <= freq <= siren_freq_range[1]) and (amp > 0.1)
                   for freq, amp in zip(freqs, spectrum / max(spectrum)))
    return detected

# Function to animate ambulance and car
# 函數用於動畫化救護車和汽車
def ambulan_lewat():
    # Check if siren sound is detected before proceeding with the animation
    # 檢查是否偵測到警報聲，如果有再開始動畫
    siren_file = "siren.wav"  
    if detect_siren_from_file(siren_file):  
        pygame.mixer.music.load(siren_file)
        pygame.mixer.music.play(-1)  

        # Add detection text below the car
        # 在車子下方加入偵測文字
        text_id = canvas.create_text(400, 350, text="Ambulance is passing! Please give way!\n救護車過去了！請讓道！", font=("Arial", 14), fill="red")

        # Car animation moving down to give way
        # 汽車動畫移動下方讓道
        car_y = 200  # Initial position of the car
        # 汽車的初始位置
        while car_y < 300:  # Car moving down
            # 汽車向下移動
            canvas.coords(car_img, 400, car_y)  # Car stays in the same horizontal position
            # 汽車保持在相同的水平方向
            root.update()
            time.sleep(0.03)
            car_y += 5

        # Ambulance movement
        # 救護車移動
        ambulance_x = 900  
        while ambulance_x > 30:  
            canvas.coords(ambulance_img, ambulance_x, 200)
            root.update()
            time.sleep(0.03)
            ambulance_x -= 5

        # Stop the siren sound after the ambulance has passed
        # 救護車經過後停止警報聲
        pygame.mixer.music.stop()

        # After the ambulance has passed, car returns to its initial position
        # 救護車過後，汽車返回原位置
        while car_y > 200: 
            canvas.coords(car_img, 400, car_y)
            root.update()
            time.sleep(0.03)
            car_y -= 5

        canvas.delete(text_id)

# Create the main window
# 創建主視窗
root = tk.Tk()
root.title("Ambulance Simulation\n救護車模擬")
root.geometry("800x500") 


# Frame for the canvas
# 創建畫布框架
frame_canvas = tk.Frame(root)
frame_canvas.pack()

# Canvas for displaying images
# 創建畫布來顯示圖片
canvas = tk.Canvas(frame_canvas, width=800, height=400, bg="white")
canvas.pack()

# Load car image
# 載入汽車圖片
car_image = Image.open("car.png") 
car_image = car_image.resize((100, 100), Image.Resampling.LANCZOS)
car_photo = ImageTk.PhotoImage(car_image)
car_img = canvas.create_image(400, 200, image=car_photo)

# Load ambulance image
# 載入救護車圖片
ambulance_image = Image.open("ambulance.png")
ambulance_image = ambulance_image.resize((100, 50), Image.Resampling.LANCZOS)
ambulance_photo = ImageTk.PhotoImage(ambulance_image)
ambulance_img = canvas.create_image(900, 200, image=ambulance_photo)

# Frame for the button
# 創建按鈕框架
frame_button = tk.Frame(root)
frame_button.pack(pady=10) 

# Button to start the ambulance animation
# 按鈕，啟動救護車動畫
btn = tk.Button(frame_button, text="Ambulance Passes\n救護車過去", font=("Arial", 14), command=lambda: threading.Thread(target=ambulan_lewat).start())
btn.pack()

# Run the window
# 啟動視窗
root.mainloop()
