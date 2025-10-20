import tkinter as tk
from tkinter import messagebox
import random

class TebakAngkaGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Game Tebak Angka")
        self.root.geometry("400x400")
        self.root.config(bg="#1e1e2f")

        self.batas = 0
        self.angka_rahasia = 0
        self.skor = 100
        self.kesempatan = 0

        self.create_widgets_awal()

    def create_widgets_awal(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(
            self.root, text="🎯 GAME TEBAK ANGKA 🎯",
            bg="#1e1e2f", fg="white", font=("Arial", 18, "bold")
        ).pack(pady=30)

        tk.Label(
            self.root, text="Pilih Tingkat Kesulitan", bg="#1e1e2f", fg="#f0db4f",
            font=("Arial", 12)
        ).pack(pady=10)

        tk.Button(self.root, text="Mudah (1–10)", command=lambda: self.mulai_game(10, 5),
                  width=20, bg="#4CAF50", fg="white", font=("Arial", 11)).pack(pady=5)
        tk.Button(self.root, text="Sedang (1–50)", command=lambda: self.mulai_game(50, 7),
                  width=20, bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=5)
        tk.Button(self.root, text="Sulit (1–100)", command=lambda: self.mulai_game(100, 10),
                  width=20, bg="#f44336", fg="white", font=("Arial", 11)).pack(pady=5)

    def mulai_game(self, batas, kesempatan):
        self.batas = batas
        self.kesempatan = kesempatan
        self.angka_rahasia = random.randint(1, batas)
        self.skor = 100
        self.create_widgets_game()

    def create_widgets_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(
            self.root, text=f"Tebak angka antara 1 dan {self.batas}",
            bg="#1e1e2f", fg="white", font=("Arial", 13)
        ).pack(pady=20)

        self.label_info = tk.Label(
            self.root, text=f"Kesempatan tersisa: {self.kesempatan}",
            bg="#1e1e2f", fg="#f0db4f", font=("Arial", 12)
        )
        self.label_info.pack(pady=5)

        self.entry_tebakan = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.entry_tebakan.pack(pady=10)
        self.entry_tebakan.focus()

        tk.Button(self.root, text="Tebak!", command=self.periksa_tebakan,
                  width=12, bg="#00adb5", fg="white", font=("Arial", 12, "bold")).pack(pady=10)

        self.label_hasil = tk.Label(self.root, text="", bg="#1e1e2f", fg="white", font=("Arial", 12))
        self.label_hasil.pack(pady=5)

        self.label_skor = tk.Label(self.root, text=f"Skor: {self.skor}", bg="#1e1e2f", fg="#00ff99", font=("Arial", 12))
        self.label_skor.pack(pady=10)

    def periksa_tebakan(self):
        try:
            tebakan = int(self.entry_tebakan.get())
        except ValueError:
            messagebox.showwarning("Input Salah", "Masukkan angka yang valid!")
            return

        if tebakan < 1 or tebakan > self.batas:
            messagebox.showinfo("Peringatan", f"Angka harus antara 1–{self.batas}")
            return

        self.kesempatan -= 1

        if tebakan < self.angka_rahasia:
            self.label_hasil.config(text="Terlalu kecil!", fg="#ffb703")
            self.skor -= 10
        elif tebakan > self.angka_rahasia:
            self.label_hasil.config(text="Terlalu besar!", fg="#ffb703")
            self.skor -= 10
        else:
            messagebox.showinfo("🎉 Selamat!", f"Kamu menebak dengan benar!\nAngkanya: {self.angka_rahasia}\nSkor akhir: {self.skor}")
            self.main_lagi()
            return

        self.label_skor.config(text=f"Skor: {self.skor}")
        self.label_info.config(text=f"Kesempatan tersisa: {self.kesempatan}")
        self.entry_tebakan.delete(0, tk.END)

        if self.kesempatan == 0:
            messagebox.showinfo("😢 Kalah!", f"Kamu kehabisan kesempatan!\nAngka yang benar: {self.angka_rahasia}\nSkor akhir: {self.skor}")
            self.main_lagi()

    def main_lagi(self):
        pilih = messagebox.askyesno("Main Lagi?", "Apakah kamu ingin bermain lagi?")
        if pilih:
            self.create_widgets_awal()
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = TebakAngkaGame(root)
    root.mainloop()
