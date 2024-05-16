import streamlit as st

st.title("Site top!")
st.write("teste dos sites locos do paranaue")
st.image('dog.jpg', caption='dog fofo')

st.header('botao')
if st.button('Say hello'):
  st.write('Why hello there')
else:
  st.write('Goodbye')

st.file_uploader("Upload a CSV")
st.multiselect("não", ["sei", "como", "isso","funciona"])

import tkinter as tk
import time

class VirtualPet:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Virtual Pet")

        self.hunger = 100
        self.sleepiness = 100
        self.fun = 100

        self.hunger_label = tk.Label(self.root, text="Fome: 100")
        self.hunger_label.pack()

        self.sleepiness_label = tk.Label(self.root, text="Sono: 100")
        self.sleepiness_label.pack()

        self.fun_label = tk.Label(self.root, text="Diversão: 100")
        self.fun_label.pack()

        self.feed_button = tk.Button(self.root, text="Alimentar", command=self.feed)
        self.feed_button.pack()

        self.sleep_button = tk.Button(self.root, text="Dormir", command=self.sleep)
        self.sleep_button.pack()

        self.play_button = tk.Button(self.root, text="Brincar", command=self.play)
        self.play_button.pack()

        self.update_stats()

        self.root.mainloop()

    def update_stats(self):
        self.hunger -= 1
        self.sleepiness -= 1
        self.fun -= 1

        self.hunger_label['text'] = f"Fome: {self.hunger}"
        self.sleepiness_label['text'] = f"Sono: {self.sleepiness}"
        self.fun_label['text'] = f"Diversão: {self.fun}"

        if self.hunger <= 0 or self.sleepiness <= 0 or self.fun <= 0:
            self.game_over()
        else:
            self.root.after(1000, self.update_stats)

    def feed(self):
        self.hunger += 20
        if self.hunger > 100:
            self.hunger = 100
        self.hunger_label.config(text=f"Fome: {self.hunger}")

    def sleep(self):
        self.sleepiness += 20
        if self.sleepiness > 100:
            self.sleepiness = 100
        self.sleepiness_label.config(text=f"Sono: {self.sleepiness}")

    def play(self):
        self.fun += 20
        if self.fun > 100:
            self.fun = 100
        self.fun_label.config(text=f"Diversão: {self.fun}")

    def game_over(self):
        self.root.title("Game Over!")
        self.hunger_label['text'] = "Fome: 0"
        self.sleepiness_label['text'] = "Sono: 0"
        self.fun_label['text'] = "Diversão: 0"
        self.feed_button['state'] = 'disabled'
        self.sleep_button['state'] = 'disabled'
        self.play_button['state'] = 'disabled'

if __name__ == "__main__":
    pet = VirtualPet()
