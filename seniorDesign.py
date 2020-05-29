import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import ttk
from playsound import playsound
import spectrogram as sp

language = ""
Tone = ""
Word = ""
sound = ''
spaghetti = 0

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)


        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        self.title("Learning Tonal languages")
        self.geometry("400x300")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, MandPage, VietPage,ListPage,PlayRecordPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")


    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]

        frame.tkraise()


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Start learning Tonal languages", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Mandarin",
                            command=lambda: langPicked(self,"Mandarin"))
        button1.pack()
        button2 = tk.Button(self, text="Vietnamese",
                            command=lambda: langPicked(self,"Vietnamese"))
        button2.pack()

        def langPicked(self,n):
            global language
            language = n
            if language == "Mandarin":

                controller.show_frame("MandPage")
            else:
                controller.show_frame("VietPage")


class MandPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pick which tone you need to practice", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)



        button = tk.Button(self, text="Tone1",
                           command=lambda: TonePicked(self,"1"))
        button.pack()

        button2 = tk.Button(self, text="Tone2",
                           command=lambda: TonePicked(self,"2"))
        button2.pack()

        button3 = tk.Button(self, text="Tone3",
                           command=lambda: TonePicked(self,"3"))
        button3.pack()

        button4 = tk.Button(self, text="Tone4",
                           command=lambda: TonePicked(self,"4"))
        button4.pack()

        button5 = tk.Button(self, text="<- Back",
                           command=lambda: controller.show_frame("HomePage"))
        button5.pack()

        def TonePicked(self,n):
            global Tone
            Tone = n
            controller.show_frame("ListPage")

class VietPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Pick which tone you need to practice", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Level",
                           command=lambda: TonePicked(self,"1"))
        button.pack()

        button2 = tk.Button(self, text="Deep",
                           command=lambda: TonePicked(self,"2"))
        button2.pack()

        button3 = tk.Button(self, text="Sharp",
                          command=lambda: TonePicked(self,"3"))
        button3.pack()

        button4 = tk.Button(self, text="Heavy",
                           command=lambda: TonePicked(self,"4"))
        button4.pack()


        button5 = tk.Button(self, text="Asking",
                           command=lambda: TonePicked(self,"5"))
        button5.pack()

        button6 = tk.Button(self, text="Tumbling",
                           command=lambda: TonePicked(self,"6"))
        button6.pack()

        button7 = tk.Button(self, text="<- Back",
                           command=lambda: controller.show_frame("HomePage"))
        button7.pack()

        def TonePicked(self,n):
            global Tone
            Tone = n
            controller.show_frame("ListPage")
class ListPage(tk.Frame):
    global Tone
    global spaghetti
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Select the word you need to practice"+Tone, font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        

    


        def updateList():
            global spaghetti
            def backList():
                global spaghetti
                spaghetti = 0
                drop.destroy()
                button5.destroy()
                if language == "Mandarin":
                    controller.show_frame("MandPage")
                else:
                    controller.show_frame("VietPage")
        
            def selected(event):
                global spaghetti
                spaghetti = 0
                global Word
                Word = drop.get()
                drop.destroy()
                button5.destroy()
                controller.show_frame("PlayRecordPage")

            if spaghetti == 0:
                mandWords =["a","ai","an","ang","ao",
                            "ba","bai","bai","ban","bang","bao","bei","ben","beng","bi","bian","biao","bie","bin","bing","bo","bu ",
                            "ca","cai","can","cang","cao","ce","cen","cha","chai","chan","chang","chao","che","chen","cheng","chi","chong","chou","chu","chua","chuai","chuan","chuang","chui","chun","chuo","ci","cong","cou","cu","cun","cuo",
                            "da","dai","dan","dang","dao","de dei","den","deng","di","dia","dian","diao","die","ding","diu","dong","dou","du","duan","dui","dun","duo",
                            "e","ei","en","eng","er",
                            "fa","fan","fang","fei","fen","feng","fo","fou","fu",
                            "ga","gai","gang","gao","ge","gei","gen","geng","gong","gou","gu","gua","guai","guan","guang","gui","gun","guo"
                            "ha","hai","han","hang","hao","he","hei","hen","heng","hong","hou","hu","hua","huai","huan","huang","hui","hun"]


                vietWords1 = ["an","anh","ba","ban","bai","bo","ca","cao","cay","chau","con","cuy","dao","dem","do","gan","giy","hai"]
                vietWords2 = ["ba","cau","chong","daau","daay","dai","dau","day","den","doi","duang","duong","gan","gai","goi","ho"]
                vietWords3 = ["bo","bon","ca","chen","chet","chin","cung","dang","dung","duoi","goc"]
                vietWords4 = ["binh","bung","cham","chi","coc","cong","dan","dat","dau","do","doc","duoc","gao","hep"]
                vietWords5 = ["am","bay","bein","bo","buoi","cai","cang","cho","chuyen","co","cu","cua","de","dho","do","gai","heim","hieu","hoi"]
                vietWords6 = ["bai","bao","cu","dade","dia","duong","giu","giua"]

                if language == "Mandarin":
                    drop = ttk.Combobox(self,value = mandWords)
                    drop.current(0)
                    drop.bind("<<ComboboxSelected>>",selected)
                    drop.pack()
                elif language == "Vietnamese":
                    
                    if Tone == "1":
                        drop = ttk.Combobox(self,value = vietWords1)
                        drop.current(0)
                        drop.bind("<<ComboboxSelected>>",selected)
                        drop.pack()

                    elif Tone == "2":
                        drop = ttk.Combobox(self,value = vietWords2)
                        drop.current(0)
                        drop.bind("<<ComboboxSelected>>",selected)
                        drop.pack()
            
                    elif Tone == "3":
                        drop = ttk.Combobox(self,value = vietWords3)
                        drop.current(0)
                        drop.bind("<<ComboboxSelected>>",selected)
                        drop.pack()
                    elif Tone == "4":
                        drop = ttk.Combobox(self,value = vietWords4)
                        drop.current(0)
                        drop.bind("<<ComboboxSelected>>",selected)
                        drop.pack()
                    elif Tone == "5":
                        drop = ttk.Combobox(self,value = vietWords5)
                        drop.current(0)
                        drop.bind("<<ComboboxSelected>>",selected)
                        drop.pack()
                    elif Tone == "6":
                        drop = ttk.Combobox(self,value = vietWords6)
                        drop.current(0)
                        drop.bind("<<ComboboxSelected>>",selected)
                        drop.pack()
                button5 = tk.Button(self, text="<- Back",
                               command=backList)
                button5.pack()
                spaghetti = 1

        button = tk.Button(self, text="Select",
                           command= updateList)
        button.pack()
        
        
class PlayRecordPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        def play(label):
            global sound

            label["text"]= Word
            if language == "Mandarin":
                sound="Mand_MV1/"+Word+Tone+"_MV1_MP3.mp3"
                playsound(sound)

            elif language == "Vietnamese":
                sound="Viet_MV1/"+Word+Tone+"_MV1_MP3.mp3"
                playsound(sound)

        #cowntdown calls record_user from spectrogram.py after 3 seconds
        def countdown(count, countdown_label, sound):
            # change text in label      
            if count > 0:
                countdown_label['text'] = count
                # call countdown again after 1000ms (1s)
                app.after(1000, countdown, count-1, countdown_label, sound)
            else:
                countdown_label['text'] = "RECORDING"
                app.after(100, sp.record_user, countdown_label, sound, language)
                return

        #record function calls countdown
        def Record(countdown_label, sound):
            countdown(3, countdown_label, sound)

        def goBack(countdown_label):
            countdown_label['text'] = ''
            controller.show_frame("ListPage")
            
            

        countdown_label = tk.Label(self, text = "", font = controller.title_font)
        countdown_label.place(x=150,y=150)

        playlabel = tk.Label(self, text="Play or Record", font=controller.title_font)
        playlabel.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Play",
                           command=lambda: play(playlabel))
        button.pack()

        button2 = tk.Button(self, text="Record",
                           command=lambda: Record(countdown_label, sound)) #change to record to accept args
        button2.pack()

        button5 = tk.Button(self, text="<- Back",
                           command=lambda: goBack(countdown_label))
        button5.pack()

        
app = SampleApp()
app.mainloop()
