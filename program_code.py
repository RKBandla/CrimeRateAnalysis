#CRIME RATE ANALYSIS......
import tkinter as tk
from tkinter import ttk, filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class CrimeRatePredictionApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Crime Rate Prediction App")

        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate x and y coordinates to center the window
        x_coordinate = (screen_width - 600) // 2
        y_coordinate = (screen_height - 400) // 2

        # Set window size and position
        self.root.geometry(f"600x400+{x_coordinate}+{y_coordinate}")

        self.root.configure(bg='#ADD8E6')

        # Create a frame to hold the content
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(expand=True, fill='both')

        # Label and Entry for location
        ttk.Label(self.main_frame, text="Location:").grid(row=0, column=0, padx=10, pady=10)
        self.location_entry = ttk.Entry(self.main_frame)
        self.location_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and Entry for type of crime
        ttk.Label(self.main_frame, text="Type of Crime:").grid(row=1, column=0, padx=10, pady=10)
        self.crime_type_entry = ttk.Entry(self.main_frame)
        self.crime_type_entry.grid(row=1, column=1, padx=10, pady=10)

        # Button to load dataset
        ttk.Button(self.main_frame, text="Load Dataset", command=self.load_dataset).grid(row=2, column=0, columnspan=2, pady=10)

        # Button to predict crime rate
        ttk.Button(self.main_frame, text="Predict Crime Rate", command=self.predict_crime_rate).grid(row=3, column=0, columnspan=2, pady=10)

        # Matplotlib figure for plotting
        self.figure, self.ax = plt.subplots(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.main_frame)
        self.canvas.get_tk_widget().grid(row=4, column=0, columnspan=2, pady=10)

        # Initialize empty DataFrame for the dataset
        self.df = pd.DataFrame()

    def load_dataset(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])

        if file_path:
            self.df = pd.read_csv(file_path)
            ttk.Label(self.main_frame, text=f"Dataset loaded successfully. Rows: {len(self.df)}, Columns: {len(self.df.columns)}").grid(row=2, column=0, columnspan=2, pady=10)

    def predict_crime_rate(self):
        if not self.df.empty:
            # Get location and type of crime from entries
            location = self.location_entry.get()
            crime_type = self.crime_type_entry.get()

            # Assuming your dataset has 'Location', 'CrimeType', and 'CrimeRate' columns
            try:
                crime_rate = self.df.loc[(self.df['Location'] == location) & (self.df['CrimeType'] == crime_type), 'CrimeRate'].values[0]
                ttk.Label(self.main_frame, text=f"Crime Rate for {location} ({crime_type}): {crime_rate}").grid(row=3, column=0, columnspan=2, pady=10)
            except IndexError:
                ttk.Label(self.main_frame, text=f"No data found for location: {location}, crime type: {crime_type}", foreground='red').grid(row=3, column=0, columnspan=2, pady=10)
        else:
            ttk.Label(self.main_frame, text="Please load a dataset first.", foreground='red').grid(row=2, column=0, columnspan=2, pady=10)

if _name_ == "_main_":
    root = tk.Tk()
    app = CrimeRatePredictionApp(root)
    root.mainloop()
