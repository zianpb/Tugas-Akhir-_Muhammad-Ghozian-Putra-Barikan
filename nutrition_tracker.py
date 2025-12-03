# nutrition_tracker.py

class UserTracker:
    def __init__(self):
        self.__current_kalori = 0
        self.limit = 2000 
        self.goal = "Maintenance"

        # UNTUK UNDO & REDO
        self.history = []       # Stack kalori yang sudah dimakan
        self.redo_stack = []    # Stack redo

    # --------------------------
    # HITUNG KEBUTUHAN
    # --------------------------
    def hitung_kebutuhan(self, bb, tb, goal_user):
        self.goal = goal_user
        bmr = (10 * bb) + (6.25 * tb) - (5 * 20) + 5
        tdee = bmr * 1.3
        
        if self.goal == "Cutting":
            self.limit = int(tdee - 500)
        elif self.goal == "Bulking":
            self.limit = int(tdee + 500)
        else:
            self.limit = int(tdee)
            
        return self.limit

    # --------------------------
    # CEK KEC0C0KAN MAKANAN
    # --------------------------
    def cek_kecocokan_makanan(self, makanan):
        p = makanan.protein
        k = makanan.karbo
        cal = makanan.kalori

        if self.goal == "Cutting":
            if p >= 20 and k < 30 and cal < 400:
                return True
        elif self.goal == "Bulking":
            if cal > 500 or (p > 20 and k > 50):
                return True
        elif self.goal == "Maintenance":
            if 300 <= cal <= 600:
                return True
                
        return False

    # --------------------------
    #SCAN MAKANAN
    # --------------------------
    def makan(self, makanan_obj):
        self.__current_kalori += makanan_obj.kalori
        
        # Push ke history
        self.history.append(makanan_obj.kalori)

        # REDO dihapus karena aksi baru
        self.redo_stack.clear()

    # --------------------------
    # UNDO
    # --------------------------
    def undo(self):
        if not self.history:
            return "Tidak ada yang bisa di-undo."

        last = self.history.pop()
        self.__current_kalori -= last

        # Masukkan ke redo stack
        self.redo_stack.append(last)

        return f"Undo berhasil: -{last} kkal"

    # --------------------------
    # REDO
    # --------------------------
    def redo(self):
        if not self.redo_stack:
            return "Tidak ada yang bisa di-redo."

        last = self.redo_stack.pop()
        self.__current_kalori += last

        # Kembali masuk history
        self.history.append(last)

        return f"Redo berhasil: +{last} kkal"

    # --------------------------
    # STATUS KALORI
    # --------------------------
    def get_status(self):
        sisa = self.limit - self.__current_kalori
        if sisa < 0:
            kelebihan = abs(sisa)
            return f"OVERLIMIT KALORI HARIAN!!!! (+{kelebihan} kkal)"
        else:
            return f"{self.__current_kalori} / {self.limit} kkal (Sisa: {sisa})"

    def get_limit(self):
        return self.limit

    # --------------------------
    # INFO GOAL
    # --------------------------
    def get_goal_info(self):
        if self.goal == "Cutting":
            return "Strategi: Protein Tinggi, Kurangi Karbo & Lemak"
        elif self.goal == "Bulking":
            return "Strategi: Surplus Kalori, Karbo & Protein Tinggi"
        return "Strategi: Gizi Seimbang & Kalori Normal"
