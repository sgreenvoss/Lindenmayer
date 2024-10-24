import tkinter
import tkinter.ttk as ttk
import os

class Gui(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.listeners = []
        self.d_or_s = 'Deterministic' # Initialization
        label = ttk.Label(self, text='I like my L systems...')
        label.grid(row=0, column=0, sticky='w')

        self.d_or_s = tkinter.StringVar(self)
        self.d_or_s.set('deterministic')
        r1 = ttk.Radiobutton(self, text="Deterministic", variable=self.d_or_s, value='deterministic', command=self.change_combo)
        r2 = ttk.Radiobutton(self, text='Stochastic', variable=self.d_or_s, value='stochastic', command=self.change_combo)
        r1.grid(row=0, column=1)
        r2.grid(row=0, column=2)

        label = ttk.Label(self, text='Iterations: ')
        self.iterations = tkinter.StringVar(self)
        iterations = ttk.Entry(self, textvariable=self.iterations)
        self.iterations.set(3)
        label.grid(row=1, column=0, sticky='w')
        iterations.grid(row=1, column=1, sticky='w')

        # submit_iterations = ttk.Button(self, text='submit', command= lambda: self.button_func())
        # submit_iterations.grid(row=1, column = 2, sticky='w')

        self.current_file = ''

        # Get list of files in the directory, removing the '.py' extension
        self.determ_directory = [f[:-3] for f in os.listdir('systems/deterministic') if f.endswith('.py')]
        self.determ_directory.remove('__pycach') if '__pycach' in self.determ_directory else None

        # files in stochastic directory
        self.stoch_directory = [f[:-3] for f in os.listdir('systems/stochastic') if f.endswith('.py')]
        self.stoch_directory.remove('__pycach') if '__pycach' in self.stoch_directory else None

        label1 = ttk.Label(self, text='System')
        label1.grid(row=2, column=0, sticky='w')

        self.system_name = tkinter.StringVar(self)
        self.system_name.set(self.determ_directory[3])  # Set default value

        self.w = ttk.Combobox(self, textvariable=self.system_name, postcommand=self.change_combo)
        self.w.bind("<<ComboboxSelected>>", self.selection_changed)
        self.w.grid(row=2, column=1, sticky='w')

        ttk.Label(self, text='Length: ').grid(row=3, column=0, sticky='w')
        self.current_length = tkinter.StringVar(self)
        self.length_entry = ttk.Entry(self, textvariable=self.current_length)
        self.length_entry.grid(row=3, column=1, sticky='w')

        ttk.Label(self, text='Angle: ').grid(row=3, column=2, sticky='w')
        self.angle = tkinter.StringVar(self)
        self.angle_entry = ttk.Entry(self, textvariable=self.angle)
        self.angle_entry.grid(row=3, column=3, sticky='w')

        ttk.Button(self, text='Reset to defaults', command=self.reset).grid(row=3, column=4, sticky='e')

        clear = ttk.Label(self, text='Clear all')
        clear.grid(row=4, column=0, sticky='w')
        clear_button = ttk.Button(self, text='clear', command=self.clear_all)
        clear_button.grid(row=4, column=1, sticky='w')

        ttk.Label(self, text='Run L System').grid(row=4, column=2, sticky='e')
        ttk.Button(self, text='RUN', command=self.get_and_run).grid(row=4, column=3, sticky='e')

    def reset(self):
        print('resetting')
        self.angle_entry.delete(0, tkinter.END)
        self.length_entry.delete(0, tkinter.END)
        self.get_set_angle_distance()
        self.send_to_listeners('RESET', None)

    def get_and_run(self):
        iterations = int(self.iterations.get())
        distance = float(self.current_length.get())
        angle = float(self.angle.get())
        self.send_to_listeners('RUN', [iterations, distance, angle])

    def change_combo(self):
        print('thinking')
        print(self.d_or_s)
        match self.d_or_s.get():
            case 'deterministic':
                self.w['values'] = self.determ_directory
            case 'stochastic':
                self.w['values'] = self.stoch_directory
                self.system_name.set(self.stoch_directory[0])
        
    def clear_all(self):
        self.send_to_listeners('CLEAR', None)

    def button_func(self):
        self.send_to_listeners('ITER', int(self.iterations.get()))

    def send_to_listeners(self, event, data=None):
        for l in self.listeners:
            l.tell((event, data))

    # THIS SUCKS
    def get_set_angle_distance(self):
        angle, dist =  self.listeners[0].give_angle_distance()
        self.angle.set(angle)
        self.current_length.set(dist)
    # suckage over

    def selection_changed(self, event):
        selection = self.system_name.get()
        self.reset()
        self.open_text(selection)

    def open_text(self, name):
        self.current_file = f'systems.{self.d_or_s.get()}.{name}'
        self.file_path = f'systems/{self.d_or_s.get()}/{name}.py'
        print(self.current_file)
        self.send_to_listeners('SYST', self.current_file)