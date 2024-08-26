print('''      
                 ____________________________________________________________________________________
                |                            "Perbandingan Pengendalian Persedian                    |
                |                            dengan Metode LUC,LTC dan Silver Meal"                  |
                |                                                                                    |
                |                                     DISUSUN OLEH:                                  |
                |                                 Rahmad Haret Rayhanda                              |      
                |____________________________________________________________________________________|
                ''')

class Registrasi:
    print(50*"-")
    print("Silahkan Melakukan Registrai terlebih dahulu! ".center(50))
    print(50*"-")
    def __init__(self):
        self.registered_username = None
        self.registered_password = None

    def register(self):
        username = str(input("Masukkan username: "))
        password = str(input("Masukkan password: "))
        if len(password) < 8:
            print(50*"-")
            print("Password 8 Characters or longer!")
            print(50*"-")
            self.register()
        else:
            self.registered_username = username
            self.registered_password = password
            print()
            print(50*"-")
            print("Selamat Anda berhasil registrasi".center(50))
            print("silahkan Login".center(50))
            print(50*"-")
            print()
            self.login()

    def login(self):
        username = str(input("Masukkan username: "))
        password = str(input("Masukkan password: "))

        if username != self.registered_username or password != self.registered_password:
            print(50*"-")
            print("Username atau Password salah. Silakan coba lagi!".center(50))
            print(50*"-")
            self.login()
        else:
            print()
            print(50*"-")
            print()
            print("Login Success".center(50))
            print("Silahkan memulai input data".center(50))
            print()
            print(50*"-")

registrasi = Registrasi()
registrasi.register()

while True:            
    print("1. Melanjutkan Pengisian Data")
    print("2. keluar program")
    lanjut = input("\nMasukkan pilihan: ")
    if lanjut == "2":
        print("program selesai")
        break
    elif lanjut == "1":
        print("Lanjutkan")

        class LUC:
            print("\nMetode LUC(Least Unit Coast)")
            def __init__(self, ongkos_pesan, ongkos_simpan_per_unit):
               self.ongkos_pesan = ongkos_pesan
               self.ongkos_simpan_per_unit = ongkos_simpan_per_unit
               self.frekuensi_pemesanan = 0

            def calculate_ongkos_simpan(self, demand, periode, start_periode):
                if periode == start_periode:
                    return 0
                else:
                    return demand[periode - 1] * (periode - start_periode) * self.ongkos_simpan_per_unit

            def calculate_ongkos_total(self, demand, months):
                results = []
                ongkos_simpan_kumulatif = 0
                start_periode = 1
                self.frekuensi_pemesanan = 0
                ongkos_simpan_1_10 = 0
                ongkos_simpan_11_12 = 0

                for i in range(len(demand)):
                    periode = i + 1
                    if periode == 11:  
                
                        ukuran_lot = sum(demand[:periode])  
                        ongkos_simpan = sum(self.calculate_ongkos_simpan(demand, j + 1, start_periode) for j in range(11))
                        ongkos_simpan_kumulatif = ongkos_simpan
                        ongkos_total = self.ongkos_pesan + ongkos_simpan_kumulatif
                        ongkos_total_per_unit = ongkos_total / ukuran_lot
                        results.append({
                            "Period": months[i],
                            "Demand": sum(demand[:periode]),
                            "Period Coverage": f"{start_periode} s.d {periode}",
                            "Lot Size": ukuran_lot,
                            "Ordering Cost": self.ongkos_pesan,
                            "Holding Cost": ongkos_simpan_kumulatif,
                            "Total Cost": ongkos_total,
                            "Total Cost Per Unit": ongkos_total_per_unit
                        }) 
 
                        ongkos_simpan_1_10 = sum(self.calculate_ongkos_simpan(demand, j + 1, start_periode) for j in range(10))

                        start_periode = 11
                        ongkos_simpan_kumulatif = 0
                        self.frekuensi_pemesanan += 1

                    ukuran_lot = sum(demand[start_periode - 1:periode])
                    ongkos_simpan = self.calculate_ongkos_simpan(demand, periode, start_periode)
                    ongkos_simpan_kumulatif += ongkos_simpan
                    if start_periode == 11:
                        ongkos_simpan_11_12 = ongkos_simpan_kumulatif
                    ongkos_total = self.ongkos_pesan + ongkos_simpan_kumulatif
                    ongkos_total_per_unit = ongkos_total / ukuran_lot
                    if periode == 12:
                        self.frekuensi_pemesanan += 1
                    results.append({
                    "Period": months[i],
                    "Demand": demand[i],
                    "Period Coverage": f"{start_periode} s.d {periode}" if periode > start_periode else str(start_periode),
                    "Lot Size": ukuran_lot,
                    "Ordering Cost": self.ongkos_pesan,
                    "Holding Cost": ongkos_simpan_kumulatif,
                    "Total Cost": ongkos_total,
                    "Total Cost Per Unit": ongkos_total_per_unit
                })

                total_ongkos_simpan = ongkos_simpan_1_10 + ongkos_simpan_11_12
                ongkos_pesan_total = self.frekuensi_pemesanan * self.ongkos_pesan
                total_ongkos = total_ongkos_simpan + ongkos_pesan_total

                return results, ongkos_simpan_1_10, ongkos_simpan_11_12, total_ongkos_simpan, ongkos_pesan_total, total_ongkos

            def input_data(self):
                print()
                print("Silahkan input data bulan, permmintaan per bulan, ongkos pesan dan ongkos simpan per unit!")
                print(100*"_")
                print()
                months_input = str(input("Masukkan nama bulan untuk setiap periode, dipisahkan dengan koma(misalnya: jan,feb,mar): "))
                demand_input = str(input("Masukkan permintaan untuk setiap bulan, dipisahkan dengan koma(misalnya:23,24,27): "))
                ongkos_pesan = float(input("Masukkan ongkos pesan(Rp): "))
                ongkos_simpan_per_unit = float(input("Masukkan ongkos simpan per unit(Rp): "))

                demand = list(map(int, demand_input.split(',')))
                months = months_input.split(',')
                return demand, months, ongkos_pesan, ongkos_simpan_per_unit

            def display_results(self, costs, ongkos_simpan_1_10, ongkos_simpan_11_12, total_ongkos_simpan, ongkos_pesan_total, total_ongkos):
                print()
                print("\nTabel Metode LUC")
                header = ["Periode", "Demand", "Cakupan Periode", "Ukuran Lot", "Ongkos Pesan", "Ongkos Simpan", "Ongkos Total", "Ongkos Total Per Unit"]
                header_format = "| {:<10} | {:<10} | {:<20} | {:<12} | {:<15} | {:<15} | {:<15} | {:<20} |"
                row_format = "| {:<10} | {:<10} | {:<20} | {:<12} | {:<15} | {:<15} | {:<15} | {:<21} |"
         
                print("-" * 142)
                print(header_format.format(*header))
                print("-" * 142)  
        
                for cost in costs:
                    row = [cost['Period'], cost['Demand'], cost['Period Coverage'], cost['Lot Size'], cost['Ordering Cost'], 
                    "{:.2f}".format(cost['Holding Cost']), "{:.2f}".format(cost['Total Cost']), "{:.2f}".format(cost['Total Cost Per Unit'])]
                    print(row_format.format(*row))
                    print("-" * 142)

                print("\nDari tabel hasil perolehan perhitungan data-data permintaan selama 1 tahun, diperoleh beberapa variabel penting \nyang akan dibandingkan dengan metode lain, diantaranya:")
                print()
                print(20*"-")
                print("Frekuensi Pemesanan:", self.frekuensi_pemesanan)
                print("rekuensi pemesanan 1:")
                print("Ongkos Simpan (1 s.d 10):", ongkos_simpan_1_10)
                print("Frekuensi pemesanan 2:")
                print("Ongkos Simpan (11 s.d 12):", ongkos_simpan_11_12)
                print()
                print("Total Ongkos Simpan:", total_ongkos_simpan)
                print("Ongkos Pesan Total:", ongkos_pesan_total)
                print("Ongkos Total:", total_ongkos)
                print(20*"-")

        luc = LUC(0, 0)

        demand, months, ongkos_pesan, ongkos_simpan_per_unit = luc.input_data()

        luc.ongkos_pesan = ongkos_pesan
        luc.ongkos_simpan_per_unit = ongkos_simpan_per_unit

        costs, ongkos_simpan_1_10, ongkos_simpan_11_12, total_ongkos_simpan, ongkos_pesan_total, total_ongkos = luc.calculate_ongkos_total(demand, months)

        luc.display_results(costs, ongkos_simpan_1_10, ongkos_simpan_11_12, total_ongkos_simpan, ongkos_pesan_total, total_ongkos)        
  
        class LTC:
            print("\n Metode LTC (Least Total Cost)")
            def __init__(self, demand, months, holding_cost):
                self.demand = demand
                self.months = months
                self.holding_cost = holding_cost
                self.result = {
                    'Periode': [], 'Dt': [], 'Ukuran Lot': [], 'Periode Simpan': [], 'Ongkos Simpan': [], 'Ongkos Simpan Kumulatif': []
                }

            def ltc_method(self):
                periods = len(self.demand)
                lot_size = 0
                cumulative_holding_cost = 0
                period_counter = 0

                for i in range(periods):
                    if i == 9:  
                        total_holding_cost = self.holding_cost * self.demand[i] * period_counter
                        cumulative_holding_cost += total_holding_cost

                        self.result['Periode'].append(self.months[i]) 
                        self.result['Dt'].append(self.demand[i])
                        self.result['Ukuran Lot'].append(lot_size)
                        self.result['Periode Simpan'].append(period_counter)
                        self.result['Ongkos Simpan'].append(total_holding_cost)
                        self.result['Ongkos Simpan Kumulatif'].append(cumulative_holding_cost)

                      
                        period_counter = 0
                        lot_size = self.demand[i]
                        total_holding_cost = self.holding_cost * self.demand[i] * period_counter
                        cumulative_holding_cost = total_holding_cost

                        self.result['Periode'].append(self.months[i])
                        self.result['Dt'].append(self.demand[i])
                        self.result['Ukuran Lot'].append(lot_size)
                        self.result['Periode Simpan'].append(period_counter)
                        self.result['Ongkos Simpan'].append(total_holding_cost)
                        self.result['Ongkos Simpan Kumulatif'].append(cumulative_holding_cost)

                        period_counter += 1 
    
                    else:
                        lot_size += self.demand[i]
                        total_holding_cost = self.holding_cost * self.demand[i] * period_counter if period_counter > 0 else 0
                        cumulative_holding_cost += total_holding_cost

                        self.result['Periode'].append(self.months[i]) 
                        self.result['Dt'].append(self.demand[i])
                        self.result['Ukuran Lot'].append(lot_size)
                        self.result['Periode Simpan'].append(period_counter)
                        self.result['Ongkos Simpan'].append(total_holding_cost)
                        self.result['Ongkos Simpan Kumulatif'].append(cumulative_holding_cost) 

                        period_counter += 1

                return self.result

            def display_results(self):
                print()
                print("\nTabel Metode LTC")
                header = ["Periode", "Dt", "Ukuran Lot", "Periode Simpan", "Ongkos Simpan(Rp)", "Ongkos Simpan Kumulatif(Rp)"]
                header_format = "| {:<12} | {:<10} | {:<12} | {:<15} | {:<18} | {:<28} |"
                row_format = "| {:<12} | {:<10} | {:<12} | {:<15} | {:<18} | {:<28} |"

             
                total_width = sum(len(h) + 4 for h in header) + (len(header) + 1)
                print("-" * 114)
                print(header_format.format(*header))
                print("-" * 114)  

                for i in range(len(self.result['Periode'])):
                    row = [
                        self.result['Periode'][i], self.result['Dt'][i], self.result['Ukuran Lot'][i], self.result['Periode Simpan'][i],
                        self.result['Ongkos Simpan'][i], "{:.2f}".format(self.result['Ongkos Simpan Kumulatif'][i])
                    ]
                    print(row_format.format(*row))
                    print("-" * 114)

            def calculate_costs(self):
              
                frekuensi_pemesanan = 2
                ongkos_pemesanan = 50000

              
                ongkos_simpan_kumulatif_8_270 = None
                ongkos_simpan_kumulatif_2_122 = None

                for i in range(len(self.result['Periode'])):
                    if self.result['Periode Simpan'][i] == 8 and self.result['Ukuran Lot'][i] == 270:
                        ongkos_simpan_kumulatif_8_270 = self.result['Ongkos Simpan Kumulatif'][i]
                    if self.result['Periode Simpan'][i] == 2 and self.result['Ukuran Lot'][i] == 122:
                        ongkos_simpan_kumulatif_2_122 = self.result['Ongkos Simpan Kumulatif'][i]

               
                jumlah_frekuensi_pemesanan = frekuensi_pemesanan
 
              
                total_ongkos_pesan = jumlah_frekuensi_pemesanan * ongkos_pemesanan

              
                total_ongkos_simpan = (ongkos_simpan_kumulatif_8_270 or 0) + (ongkos_simpan_kumulatif_2_122 or 0)
                ongkos_total = total_ongkos_simpan + total_ongkos_pesan
           
                print("\nDari tabel hasil perolehan perhitungan data-data permintaan selama 1 tahun, diperoleh beberapa variabel penting \nyang akan dibandingkan dengan metode lain, diantaranya:")
                print()
                print(20*"-")
                print("Frekuensi Pemesanan:", jumlah_frekuensi_pemesanan)
                print("Total Ongkos Pesan (2 kali pesan):", total_ongkos_pesan)
                print("Ongkos Simpan Kumulatif:", total_ongkos_simpan)
                print("Ongkos Total:", ongkos_total)
                print(20*"-")

        def get_user_input():
            print()
            print("Silahkan input data bulan, permmintaan per bulan dan ongkos simpan per unit!")
            print(100*"_")
            print()
            months = input("Masukkan bulan (dipisahkan dengan koma, contoh: Jan,Feb,Mar): ").split(',')  
            demand = list(map(int, input("Masukkan jumlah saham setiap bulan (dipisahkan dengan koma, contoh: 23,24,27): ").split(',')))
            holding_cost_per_unit = float(input("Masukkan ongkos simpan per unit per periode (Rp): "))
            holding_cost = holding_cost_per_unit  
            return months, demand, holding_cost

       
        months, demand, holding_cost = get_user_input()

        ltc = LTC(demand, months, holding_cost)
        table = ltc.ltc_method()
        ltc.display_results()
        ltc.calculate_costs()


        class Silvermeal:
            print("\nMetode Silver Meal")
            
            def __init__(self, months):
                self.months = months
                self.result = {
                    'Periode': [], 'Dt': [], 'Cakupan Periode': [], 'Ukuran Lot': [], 
                    'Ongkos Pesan (Rp)': [], 'Ongkos Simpan (Rp)': [], 'Ongkos Total (Rp)': [], 
                    'Ongkos Total per Periode (Rp)': []
                }

            def calculate(self, demand, ordering_cost, holding_cost):
                periods = len(demand)
                i = 0
                while i < periods:
                    period_demand = 0
                    total_holding_cost = 0
                    cakupan_periode = 0
                    for j in range(i, min(i + 9, periods)):
                        period_demand += demand[j]
                        total_holding_cost += (j - i) * demand[j] * holding_cost
                        total_cost = ordering_cost + total_holding_cost
                        average_cost = total_cost / period_demand

                        if j == i or j == i + 8 or (len(self.result['Ongkos Total per Periode (Rp)']) > 0 and average_cost <= self.result['Ongkos Total per Periode (Rp)'][-1]):
                            cakupan_periode += 1
                            self.result['Periode'].append(self.months[j])  
                            self.result['Dt'].append(demand[j])
                            self.result['Cakupan Periode'].append(cakupan_periode)
                            self.result['Ukuran Lot'].append(period_demand)
                            self.result['Ongkos Pesan (Rp)'].append(ordering_cost)
                            self.result['Ongkos Simpan (Rp)'].append(total_holding_cost)
                            self.result['Ongkos Total (Rp)'].append(total_cost)
                            self.result['Ongkos Total per Periode (Rp)'].append(total_cost / cakupan_periode)
                        else:
                            break
                    i += cakupan_periode

            def display_results(self):
                print("\nTabel Perhitungan Silver Meal")
                header = ["Periode", "Dt", "Cakupan Periode", "Ukuran Lot", "Ongkos Pesan (Rp)", "Ongkos Simpan (Rp)", "Ongkos Total (Rp)", "Ongkos Total per Periode (Rp)"]
                header_format = "| {:<10} | {:<10} | {:<15} | {:<12} | {:<17} | {:<17} | {:<17} | {:<28} |"
                row_format = "| {:<10} | {:<10} | {:<15} | {:<12} | {:<17} | {:<17} | {:<17} | {:<30} |"
                
                print("-" * 153)
                print(header_format.format(*header))
                print("-" * 153)        
                
                for i in range(len(self.result['Periode'])):
                    row = [self.result['Periode'][i], self.result['Dt'][i], self.result['Cakupan Periode'][i], self.result['Ukuran Lot'][i], 
                        self.result['Ongkos Pesan (Rp)'][i], "{:.2f}".format(self.result['Ongkos Simpan (Rp)'][i]), 
                        "{:.2f}".format(self.result['Ongkos Total (Rp)'][i]), "{:.2f}".format(self.result['Ongkos Total per Periode (Rp)'][i])]
                    print(row_format.format(*row))
                    print("-" * 153)

            def calculate_frequencies_and_costs(self, cakupan_periode_1, ukuran_lot_1, cakupan_periode_2, ukuran_lot_2, ordering_cost):
                frekuensi_pemesanan = 0
                ongkos_simpan_1 = None
                ongkos_simpan_2 = None

                for i in range(len(self.result['Periode'])):
                    if self.result['Cakupan Periode'][i] == cakupan_periode_1 and self.result['Ukuran Lot'][i] == ukuran_lot_1:
                        ongkos_simpan_1 = self.result['Ongkos Simpan (Rp)'][i]
                        frekuensi_pemesanan += 1
                    if self.result['Cakupan Periode'][i] == cakupan_periode_2 and self.result['Ukuran Lot'][i] == ukuran_lot_2:
                        ongkos_simpan_2 = self.result['Ongkos Simpan (Rp)'][i]
                        frekuensi_pemesanan += 1

                jumlah_frekuensi_pemesanan = frekuensi_pemesanan
                total_ongkos_pesan = jumlah_frekuensi_pemesanan * ordering_cost
                total_ongkos_simpan = (ongkos_simpan_1 or 0) + (ongkos_simpan_2 or 0)
                ongkos_total = total_ongkos_simpan + total_ongkos_pesan
                return jumlah_frekuensi_pemesanan, total_ongkos_pesan, total_ongkos_simpan, ongkos_total

        def get_user_input():
            print()
            print("Silahkan input data bulan, permintaan per bulan, ongkos pesan dan ongkos simpan per unit!")
            print(100*"_")
            print()
            months = str(input("Masukkan bulan (dipisahkan dengan koma, contoh: Jan,Feb,Mar): ").split(','))
            demand = list(map(int, input("Masukkan jumlah saham setiap bulan (dipisahkan dengan koma, contoh: 23,24,27): ").split(',')))
            ordering_cost = float(input("Masukkan ongkos pesan (Rp): "))
            holding_cost = float(input("Masukkan ongkos simpan per unit per periode (Rp): "))
            return months, demand, ordering_cost, holding_cost 

        months, demand, ordering_cost, holding_cost = get_user_input()

        silvermeal = Silvermeal(months)
        silvermeal.calculate(demand, ordering_cost, holding_cost)
        silvermeal.display_results()

        cakupan_periode_1, ukuran_lot_1 = 8, 233
        cakupan_periode_2, ukuran_lot_2 = 4, 159
        jumlah_frekuensi_pemesanan, total_ongkos_pesan, total_ongkos_simpan, ongkos_total = silvermeal.calculate_frequencies_and_costs(
            cakupan_periode_1, ukuran_lot_1, cakupan_periode_2, ukuran_lot_2, ordering_cost)

        print("\nDari tabel hasil perolehan perhitungan data-data permintaan selama 1 tahun, diperoleh beberapa variabel penting \nyang akan dibandingkan dengan metode lain, diantaranya:")
        print(20*"-")
        print("\nFrekuensi Pemesanan:", jumlah_frekuensi_pemesanan)
        print("Total Ongkos Pesan ({} kali pesan):".format(jumlah_frekuensi_pemesanan), total_ongkos_pesan) 
        print("Ongkos Simpan Kumulatif:", total_ongkos_simpan)
        print("Ongkos Total:", ongkos_total)
        print(20*"-")

        class Tabel_Perbandingan:
            def __init__(self):
                print("\nTabel Perbandingan Pengendalian Persediaan dengan Metode LUC, LTC, dan Silver Meal")
                self.result = {
                'Metode': [], 'Jumlah Frekuensi Pemesanan': [], 'Ongkos Pesan': [], 'Ongkos Simpan': [], 'Total Ongkos': []
                }

            def input_data(self, metode, frekuensi_pemesanan, ongkos_simpan):
                ongkos_pesan = 50000 * frekuensi_pemesanan
                total_ongkos = ongkos_simpan + ongkos_pesan
        
                self.result['Metode'].append(metode)
                self.result['Jumlah Frekuensi Pemesanan'].append(frekuensi_pemesanan)
                self.result['Ongkos Pesan'].append(ongkos_pesan)
                self.result['Ongkos Simpan'].append(ongkos_simpan)
                self.result['Total Ongkos'].append(total_ongkos)

            def print_result(self):
                header = f"| {'Metode':<15} | {'Jumlah Frekuensi Pemesanan':<24} | {'Ongkos Pesan (Rp)':<16} | {'Ongkos Simpan (Rp)':<17} | {'Total Ongkos (Rp)':<16} |"
                line = "-" * len(header)
                print(line)
                print(header)
                print(line)
                for i in range(len(self.result['Metode'])):
                    metode = self.result['Metode'][i]
                    frekuensi = self.result['Jumlah Frekuensi Pemesanan'][i]
                    ongkos_pesan = f"{self.result['Ongkos Pesan'][i]:,}"
                    ongkos_simpan = f"{self.result['Ongkos Simpan'][i]:,}"
                    total_ongkos = f"{self.result['Total Ongkos'][i]:,}"
                    print(f"| {metode:<15} | {frekuensi:<26} | {ongkos_pesan:<17} | {ongkos_simpan:<18} | {total_ongkos:<17} |")
                    print(line)
    
            def find_optimum_method(self):
                min_total_ongkos = min(self.result['Total Ongkos'])
                index_of_minimum = self.result['Total Ongkos'].index(min_total_ongkos)
                optimum_method = self.result['Metode'][index_of_minimum]
                return optimum_method


        def get_user_input():
            metode_list = ["LUC", "LTC", "Silvermeal"]
            data = []
      
            for metode in metode_list:
                print(f"Masukkan data untuk metode {metode}")
                frekuensi_pemesanan = int(input(f"Jumlah Frekuensi Pemesanan untuk {metode}: "))
                ongkos_simpan = float(input(f"Ongkos Simpan untuk {metode} (Rp): "))
                data.append((metode, frekuensi_pemesanan, ongkos_simpan))
            return data

        tabel_perbandingan = Tabel_Perbandingan()
        data = get_user_input()
        for metode, frekuensi_pemesanan, ongkos_simpan in data:
            tabel_perbandingan.input_data(metode, frekuensi_pemesanan, ongkos_simpan)

        tabel_perbandingan.print_result()
        optimum_method = tabel_perbandingan.find_optimum_method()
        print()
        print(f"\nDapat disimpulkan dari ketiga Metode. Metode yang paling optimum adalah: {optimum_method}")
        print("Karena metode ini yang paling minimum ongkos simpan dan ongkos totalnya")  
        print(100*"_")
   
    print("1. ulang mengisi data")
    print("2. keluar program")
    lanjut = input("\nMasukkan pilihan: ")
    if lanjut == "2":
        print("Program selesai")
        break
    else:
        print("Lanjutkan")