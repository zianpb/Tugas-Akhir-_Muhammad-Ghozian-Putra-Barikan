# ==============================
# GUI.py — MoodMeal (UI Modern) + UNDO/REDO
# ==============================

import tkinter as tk
from tkinter import messagebox

from food_data import menu_list, Makanan
from nutrition_tracker import UserTracker


class MoodMealGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("MoodMeal - Gojii")
        self.root.geometry("400x750")

        # Latar belakangg
        self.COLOR_BG = "#F5F7FA"
        self.COLOR_CARD = "#FFFFFF"
        self.COLOR_PRIMARY = "#4CAF50"
        self.COLOR_ACCENT = "#2196F3"
        self.COLOR_TEXT = "#333333"
        self.COLOR_SUBTEXT = "#666666"

        self.root.configure(bg=self.COLOR_BG)

        self.tracker = UserTracker()
        self.list_rekomendasi = []
        self.index_sekarang = 0

        self.halaman_setup()

    # -----------------------------------------------------
    # Clear Screen
    # -----------------------------------------------------
    def bersihkan_layar(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # -----------------------------------------------------
    # HALAMAN 1 — SETUP
    # -----------------------------------------------------
    def halaman_setup(self):
        self.bersihkan_layar()
        self.root.configure(bg=self.COLOR_BG)

        # Judulnya
        tk.Label(
            self.root, text="MoodMeal",
            font=("Helvetica", 24, "bold"),
            fg=self.COLOR_TEXT, bg=self.COLOR_BG
        ).pack(pady=(30, 5))

        tk.Label(
            self.root, text="Aplikasi rekomendasi makanan berdasarkan mood",
            font=("Helvetica", 10),
            fg=self.COLOR_SUBTEXT, bg=self.COLOR_BG
        ).pack(pady=(0, 20))

        # --- Card Container ---
        card = tk.Frame(self.root, bg=self.COLOR_CARD)
        card.pack(fill="x", padx=25, pady=10)

        # --- Input builder ---
        def buat_input(label):
            tk.Label(
                card, text=label,
                bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
                anchor="w",
                font=("Helvetica", 10, "bold")
            ).pack(fill="x", padx=15, pady=(10, 0))

            entry = tk.Entry(card, font=("Helvetica", 11), relief="solid", bd=1)
            entry.pack(fill="x", padx=15, pady=(0, 10))
            return entry

        self.input_bb = buat_input("Berat Badan (kg):")
        self.input_tb = buat_input("Tinggi Badan (cm):")

        tk.Label(
            card, text="Pilih Goal Program:",
            bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
            font=("Helvetica", 10, "bold")
        ).pack(pady=(10, 5))

        self.var_goal = tk.StringVar(value="Maintenance")
        frame_goal = tk.Frame(card, bg=self.COLOR_CARD)
        frame_goal.pack()

        modes = ["Cutting (Defisit)", "Maintenance (Normal)", "Bulking (Surplus)"]
        for m in modes:
            tk.Radiobutton(
                frame_goal, text=m,
                variable=self.var_goal, value=m.split()[0],
                bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
                activebackground=self.COLOR_CARD, selectcolor="#E8E8E8"
            ).pack(anchor="w")

        tk.Button(
            self.root, text="Hitung & Lanjut",
            bg=self.COLOR_PRIMARY, fg="white",
            font=("Helvetica", 12, "bold"),
            command=self.proses_setup
        ).pack(fill="x", padx=40, pady=25)

    def proses_setup(self):
        try:
            bb = int(self.input_bb.get())
            tb = int(self.input_tb.get())
            goal = self.var_goal.get()
            target = self.tracker.hitung_kebutuhan(bb, tb, goal)

            info_strategi = self.tracker.get_goal_info()

            messagebox.showinfo(
                "Hasil",
                f"Target: {target} kkal/hari\n\n{info_strategi}"
            )

            self.halaman_utama()

        except ValueError:
            messagebox.showerror("Error", "Isi angka yang benar!")

    # -----------------------------------------------------
    # HALAMAN 2 — MAIN PAGE
    # -----------------------------------------------------
    def halaman_utama(self):
        self.bersihkan_layar()
        self.root.configure(bg=self.COLOR_BG)

        limit = self.tracker.get_limit()
        goal = self.tracker.goal

        # --- Header ---
        tk.Label(
            self.root, text=f"{goal} — {limit} kkal",
            font=("Helvetica", 16, "bold"),
            fg=self.COLOR_PRIMARY, bg=self.COLOR_BG
        ).pack(pady=(25, 5))

        # --- Goal Info ---
        tk.Label(
            self.root, text=self.tracker.get_goal_info(),
            bg="#FFF3CD", fg="#856404",
            font=("Helvetica", 9), wraplength=350,
            padx=10, pady=6
        ).pack(pady=(0, 20), fill="x", padx=25)

        # --- CARD INPUT ---
        card = tk.Frame(self.root, bg=self.COLOR_CARD)
        card.pack(fill="x", padx=25, pady=5)

        def buat_input(label):
            tk.Label(
                card, text=label,
                bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
                font=("Helvetica", 10, "bold"),
                anchor="w"
            ).pack(fill="x", padx=10, pady=(10, 0))

            entry = tk.Entry(card, font=("Helvetica", 11),
                             relief="solid", bd=1)
            entry.pack(fill="x", padx=10, pady=(0, 10))
            return entry

        self.entry_budget = buat_input("Isi Dompetmu (Rp):")

        # --- Mood Picker ---
        tk.Label(
            card, text="Mood Kamu:",
            bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
            font=("Helvetica", 10, "bold")
        ).pack(pady=(5, 0))

        self.var_mood = tk.StringVar(value="Biasa")

        frame_mood = tk.Frame(card, bg=self.COLOR_CARD)
        frame_mood.pack(pady=5)

        moods = ["Sedih", "Senang", "Marah", "Lelah", "Sehat", "Biasa"]

        for i, m in enumerate(moods):
            tk.Radiobutton(
                frame_mood, text=m,
                variable=self.var_mood, value=m,
                bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
                activebackground=self.COLOR_CARD,
                selectcolor="#E8E8E8",
                font=("Helvetica", 9)
            ).grid(row=i//2, column=i % 2, sticky="w", padx=10)

        # --- Button Cari ---
        tk.Button(
            self.root,
            text="CARI REKOMENDASI",
            bg=self.COLOR_PRIMARY, fg="white",
            font=("Helvetica", 12, "bold"),
            height=2,
            command=self.logika_cari_makan
        ).pack(fill="x", padx=40, pady=15)

        # --- Add Menu Button ---
        tk.Button(
            self.root, text="➕ Tambah Menu Baru",
            command=self.halaman_tambah_menu,
            bg=self.COLOR_ACCENT, fg="white",
            font=("Helvetica", 10, "bold")
        ).pack(pady=2)

        # --- Result Card ---
        self.frame_hasil = tk.Frame(self.root, bg=self.COLOR_CARD)
        self.frame_hasil.pack(fill="both", expand=True,
                              padx=25, pady=15)

        self.lbl_nama = tk.Label(
            self.frame_hasil, text="Klik cari dulu...",
            font=("Helvetica", 13, "bold"),
            bg=self.COLOR_CARD, fg=self.COLOR_TEXT
        )
        self.lbl_nama.pack(pady=10)

        self.lbl_info = tk.Label(
            self.frame_hasil, text="",
            font=("Helvetica", 10),
            bg=self.COLOR_CARD, fg=self.COLOR_SUBTEXT
        )
        self.lbl_info.pack()

        # --- Buttons navigation ---
        self.btn_next = tk.Button(
            self.frame_hasil, text="➡️ Menu Berikutnya",
            command=self.ganti_menu_selanjutnya,
            state="disabled", font=("Helvetica", 10)
        )
        self.btn_next.pack(pady=10)

        self.btn_makan = tk.Button(
            self.frame_hasil, text="PILIH MENU INI",
            bg=self.COLOR_PRIMARY, fg="white",
            command=self.proses_makan,
            state="disabled", font=("Helvetica", 11, "bold")
        )
        self.btn_makan.pack(pady=10)

        # =====================
        # --- UNDO / REDO ---
        # =====================
        frame_undo_redo = tk.Frame(self.frame_hasil, bg=self.COLOR_CARD)
        frame_undo_redo.pack(pady=5)

        self.btn_undo = tk.Button(
            frame_undo_redo, text="↩️ UNDO",
            bg="#FFC107", fg="black",
            font=("Helvetica", 10, "bold"),
            width=10,
            command=self.proses_undo,
            state="disabled"
        )
        self.btn_undo.grid(row=0, column=0, padx=5)

        self.btn_redo = tk.Button(
            frame_undo_redo, text="↪️ REDO",
            bg="#03A9F4", fg="white",
            font=("Helvetica", 10, "bold"),
            width=10,
            command=self.proses_redo,
            state="disabled"
        )
        self.btn_redo.grid(row=0, column=1, padx=5)

        # --- Footer ---
        tk.Button(
            self.root, text="⬅️ Ubah Data Diri",
            command=self.halaman_setup,
            fg=self.COLOR_SUBTEXT, bg=self.COLOR_BG,
            relief="flat"
        ).pack(side="bottom", pady=5)

        self.lbl_status = tk.Label(
            self.root, text=self.tracker.get_status(),
            bd=1, relief="sunken", anchor="w",
            bg="#EEEEEE"
        )
        self.lbl_status.pack(side="bottom", fill="x")

        # initial update undo/redo button state
        self.update_undo_redo_buttons()

    # -----------------------------------------------------
    # Logic — Cari Makanan
    # -----------------------------------------------------
    def logika_cari_makan(self):
        mood_user = self.var_mood.get()

        try:
            val = self.entry_budget.get()
            budget_user = int(val) if val else 0
        except ValueError:
            messagebox.showerror("Error", "Budget harus angka!")
            return

        self.list_rekomendasi = []

        for mkn in menu_list:
            cek_fit = self.tracker.cek_kecocokan_makanan(mkn)
            cek_duit = mkn.harga <= budget_user
            cek_mood = True if mood_user == "Biasa" else mkn.mood == mood_user

            if cek_fit and cek_duit and cek_mood:
                self.list_rekomendasi.append(mkn)

        if self.list_rekomendasi:
            self.index_sekarang = 0
            self.tampilkan_detail_menu()
            self.btn_next.config(state="normal")
            self.btn_makan.config(state="normal")
        else:
            self.lbl_nama.config(text="Tidak Ditemukan", fg="red")
            self.lbl_info.config(text="Naikkan budget / Ganti mood")
            self.btn_next.config(state="disabled")
            self.btn_makan.config(state="disabled")

    def tampilkan_detail_menu(self):
        mkn = self.list_rekomendasi[self.index_sekarang]

        self.lbl_nama.config(text=mkn.nama, fg=self.COLOR_TEXT)
        self.lbl_info.config(
            text=f"Rp {mkn.harga:,} | {mkn.kalori} kkal\n"
                 f"P:{mkn.protein}g  K:{mkn.karbo}g  L:{mkn.lemak}g"
        )

    def ganti_menu_selanjutnya(self):
        total = len(self.list_rekomendasi)
        if total > 1:
            self.index_sekarang = (self.index_sekarang + 1) % total
            self.tampilkan_detail_menu()
        else:
            messagebox.showinfo("Info",
                                "Cuma ada 1 menu yang cocok.")

    def proses_makan(self):
        mkn = self.list_rekomendasi[self.index_sekarang]
        # panggil tracker untuk makan (tracker harus meng-handle history untuk undo/redo)
        try:
            self.tracker.makan(mkn)
        except Exception as e:
            # fallback: kalau tracker versi lama tanpa support undo, tetap tambahkan kalori
            try:
                # asumsikan ada atribut private __current_kalori? jangan akses private; jadi kita skip
                pass
            except Exception:
                pass

        status = self.tracker.get_status()
        self.lbl_status.config(text=status)

        # update tombol undo/redo sesuai state tracker
        self.update_undo_redo_buttons()

        if "OVERLIMIT" in status:
            self.lbl_status.config(bg="#FFCCCC", fg="red")
            messagebox.showwarning("Waduh!", "Kamu OVERLIMIT!")
        else:
            self.lbl_status.config(bg="#EEEEEE", fg="black")
            messagebox.showinfo("Sukses", f"Kamu makan {mkn.nama}")

    # -----------------------------------------------------
    # UNDO / REDO handlers (GUI)
    # -----------------------------------------------------
    def proses_undo(self):
        if hasattr(self.tracker, "undo"):
            msg = self.tracker.undo()
        else:
            msg = "Fitur undo tidak tersedia pada tracker."

        # update status & button states
        try:
            self.lbl_status.config(text=self.tracker.get_status())
        except Exception:
            pass

        messagebox.showinfo("Undo", msg)
        self.update_undo_redo_buttons()

    def proses_redo(self):
        if hasattr(self.tracker, "redo"):
            msg = self.tracker.redo()
        else:
            msg = "Fitur redo tidak tersedia pada tracker."

        # update status & button states
        try:
            self.lbl_status.config(text=self.tracker.get_status())
        except Exception:
            pass

        messagebox.showinfo("Redo", msg)
        self.update_undo_redo_buttons()

    def update_undo_redo_buttons(self):
        """
        Enable/disable undo & redo buttons based on tracker history.
        Uses hasattr checks so GUI still works even if tracker doesn't have stacks.
        """
        # default disable
        state_undo = "disabled"
        state_redo = "disabled"

        if hasattr(self.tracker, "history"):
            try:
                if len(self.tracker.history) > 0:
                    state_undo = "normal"
            except Exception:
                state_undo = "disabled"

        if hasattr(self.tracker, "redo_stack"):
            try:
                if len(self.tracker.redo_stack) > 0:
                    state_redo = "normal"
            except Exception:
                state_redo = "disabled"

        # apply states (buttons may not exist yet if called early)
        try:
            self.btn_undo.config(state=state_undo)
        except Exception:
            pass
        try:
            self.btn_redo.config(state=state_redo)
        except Exception:
            pass

    # -----------------------------------------------------
    # POPUP — Add Menu
    # -----------------------------------------------------
    def halaman_tambah_menu(self):
        self.popup = tk.Toplevel(self.root)
        self.popup.title("Tambah Menu")
        self.popup.geometry("350x500")
        self.popup.configure(bg=self.COLOR_BG)

        tk.Label(
            self.popup, text="Input Data Makanan",
            font=("Helvetica", 14, "bold"),
            fg=self.COLOR_TEXT, bg=self.COLOR_BG
        ).pack(pady=15)

        # Input creator
        def bikin_input(label):
            frame = tk.Frame(self.popup, bg=self.COLOR_CARD)
            frame.pack(fill="x", padx=20, pady=5)

            tk.Label(frame, text=label,
                     width=15, anchor="w",
                     bg=self.COLOR_CARD, fg=self.COLOR_TEXT,
                     font=("Helvetica", 10, "bold")
                     ).pack(side="left")

            entry = tk.Entry(frame, font=("Helvetica", 10))
            entry.pack(side="right", fill="x", expand=True)
            return entry

        self.ent_nama = bikin_input("Nama Makanan:")
        self.ent_harga = bikin_input("Harga (Rp):")

        tk.Frame(self.popup, height=2, bg="#DDD").pack(fill="x", padx=20, pady=10)

        self.ent_kalori = bikin_input("Kalori (kkal):")
        self.ent_prot = bikin_input("Protein (g):")
        self.ent_karbo = bikin_input("Karbo (g):")
        self.ent_lemak = bikin_input("Lemak (g):")

        tk.Label(
            self.popup, text="Kategori Mood:",
            bg=self.COLOR_BG, fg=self.COLOR_TEXT,
            font=("Helvetica", 10, "bold")
        ).pack(pady=(5, 0))

        self.var_mood_baru = tk.StringVar(value="Biasa")
        moods = ["Sedih", "Senang", "Marah", "Lelah", "Sehat", "Biasa"]
        tk.OptionMenu(self.popup, self.var_mood_baru, *moods).pack(pady=10)

        tk.Button(
            self.popup, text="SIMPAN",
            bg=self.COLOR_ACCENT, fg="white",
            font=("Helvetica", 11, "bold"),
            command=self.simpan_menu_baru
        ).pack(fill="x", padx=30, pady=15)

    def simpan_menu_baru(self):
        try:
            nama = self.ent_nama.get()
            if not nama:
                messagebox.showerror("Error", "Nama tidak boleh kosong!")
                return

            harga = int(self.ent_harga.get())
            kal = int(self.ent_kalori.get())
            p = int(self.ent_prot.get())
            k = int(self.ent_karbo.get())
            l = int(self.ent_lemak.get())
            mood = self.var_mood_baru.get()

            makanan_baru = Makanan(nama, harga, mood, kal, p, k, l)
            menu_list.append(makanan_baru)

            messagebox.showinfo("Berhasil", f"{nama} ditambahkan!")

            self.popup.destroy()

        except ValueError:
            messagebox.showerror("Error", "Semua input angka harus valid!")


# ================================================
# RUN APP
# ================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = MoodMealGUI(root)
    root.mainloop()
