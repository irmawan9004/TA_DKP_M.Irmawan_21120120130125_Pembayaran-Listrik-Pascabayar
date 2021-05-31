from tkinter import * 
from tkinter import ttk
import tkinter.messagebox as m


class Tagihanlis():
    def __init__(self, email, password,daya,golongan,harga,kmawal,kmakhir,totalm,tagihan,uang,pajak):
        self.email = email
        self.password = password
        self.daya = daya
        self.golongan = golongan
        self.harga = harga
        self.kmawal = kmawal
        self.kmakhir = kmakhir
        self.totalm = totalm
        self.tagihan = tagihan
        self.uang = uang
        self.pajak = pajak
        
    
    def getDaya(self):
        return self.daya
    def getGolongan(self):
        return self.golongan
    def getHarga(self):
        return self.harga
    def getKmawal(self):
        return self.kmawal
    def getKmakhir(self):
        return self.kmakhir
    def getTotalm(self):
        return self.totalm
    def getTagihan(self):
        return self.tagihan
    def getUang(self):
        return self.uang
    def getPajak(self):
        return self.pajak
    def getKembali(self):
        return self.Kembali
    def setBersihin(self, clear):
        self.golongan = ""
        self.daya = ""
        self.harga = 0
        self.km_awal = 0
        self.km_akhir = 0
        self.totalm = 0
        self.tagihan = 0
        self.uang = 0
        self.pajak = 0
        

Listrik1 = Tagihanlis("","",0,0,0,0,0,0,0,0,0,)
def masuk():

    nomorid = inomor.get()
    namapelanggan = inama.get()
    if(nomorid == 'admin' and namapelanggan == 'admin'):
        m.showinfo('Sukses', 'Nomor Id dan Password yang anda masukkan benar!')
        return
    else:
        m.showwarning('Failed','Nomor Id dan Password yang anda masukkan salah!')
        return

def daya():
    print("sialan")
    km_awal = Listrik1.getKmawal()
    km_akhir = Listrik1.getKmakhir()
    harga = Listrik1.getHarga()
    golongan = Listrik1.getGolongan()
    km_awal = iawal.get()
    km_akhir = iakhir.get()
    dikali = 0
    totalmeter = 0
    totaltagihan = 0
    if strhobi.get() == '450V':
        harga = "\t\tRp.196"
        golongan = "\t\tR1/TR"
        dikali = 196
    elif strhobi.get() == '900V':
        harga = "\t\tRp.274"
        golongan = "\t\tR1M/TR"
        dikali = 274
    elif strhobi.get() == '1300V':
        harga = "\t\tRp.1352"
        golongan = "\t\tR1/M"
        dikali = 1352
    elif strhobi.get() == '3500':
        harga = "\t\tRp.1444"
        golongan = "\t\tR2/TR"
        dikali = 1444
    if(km_awal == "" and km_akhir == ""):
        m.showinfo('Info', 'KM AWAL dan KM AKHIR harap Diisi!')
    elif(km_awal >= km_akhir):
        m.showinfo('Info,KM Akhir harus lebih besar')
    elif(km_akhir > km_awal):
        totalmeter = (int(km_akhir) - int(km_awal))
        totaltagihan = totalmeter * dikali
    print("sialan")
    print(totalmeter)
    print(totaltagihan)
    print(harga)
    print(golongan)
    lbkk = Label(text = "Harga per Kwh\t:"+harga)
    lbkk.place(x=30,y=310)
    lbgl = Label(text = "Golongan\t:"+str(golongan))
    lbgl.place(x=30,y=350)
    lbtt = Label(text = "Total Meter\t:\t\t"+str(totalmeter))
    lbtt.place(x=30,y=390)
    ltag = Label(text = "Total Tagihan\t:\t\tRp."+str(totaltagihan))
    ltag.place(x=30,y=430)
        
    
 
def membayar():
    
    global totaltagihan
    totaltagihan = totalmeter * dikali
    nominal = inom.get()
    if(nominal == "" and totaltagihan == ""):
        m.showinfo('Info','Anda Belum mengisi Uang atau Penggunaan Listrik')
    elif(nominal < totaltagihan):
        m.showinfo('Info','Uang Anda Kurang')
    elif(nominal >= totaltagihan):
        kembali = (nominal - totaltagihan)

        m.showinfo("Kembalian = " + "Rp" + kembali) 


top = Tk()  
top.geometry("800x600")
top.title("Masukkan Data")


#creating label  
lbnama = Label(top, text = "Nomor ID\t:")
lbnama.place(x = 30,y = 20)    
lbjk = Label(text = "Nama Pelanggan\t:")
lbjk.place(x = 30, y=60)
lbbb = Label(text = "Pilih Daya Listrik\t:")
lbbb.place(x=30,y=130)
lbgl = Label(text = "Golongan\t:")
lbgl.place(x=30,y=350)
lbkk = Label(text = "Harga per Kwh\t:",)
lbkk.place(x=30,y=310)
lbjm = Label(text = "Kwh Awal\t:")
lbjm.place(x=30,y=170)
lbmb = Label(text = "Kwh Akhir\t:")
lbmb.place(x=30,y=210)
lbtt = Label(text = "Total Meter\t:")
lbtt.place(x=30,y=390)
ltag = Label(text = "Total Tagihan\t:")
ltag.place(x=30,y=430)
lnom = Label(text = "Uang Anda\t:")
lnom.place(x = 30, y=500)

#create input  
inama = StringVar()
inama = Entry(top,width = 40,)
inama.place(x = 200, y = 20, ) 
inomor = IntVar()
inomor = Entry(top,width = 40,)
inomor.place(x = 200, y = 60)  
km_awal=IntVar()
iawal = Entry(top,width = 40, )
iawal.place(x = 200, y = 170)
Km_akhir =IntVar()
iakhir = Entry(top,width = 40, )
iakhir.place(x = 200, y = 210)
nominal = DoubleVar()
inom = Entry(top,width = 40, )
inom.place(x = 200,y = 500)


#create combobox
strhobi = StringVar(value='450V') 
Cb1 = ttk.Combobox(top, width = 17, textvariable = strhobi, state="readonly")
Cb1.place(x=200, y=130)

# Adding combobox drop down list 
Cb1['values'] = ('450V' ,
                 '900V',
                 '1300V',
                 '3500V' ) 

#create button
btn = Button(text = 'Check',command = masuk)
btn.place(x = 400 , y = 85)
btn1 = Button(top, command = daya, text="Hitung")
btn1.place(x=400,y=235)
btn2 = Button(top, command = membayar, text = "Bayar")
btn2.place(x = 400, y = 525)

top.mainloop()    

