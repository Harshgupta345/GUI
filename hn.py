import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage

class FithubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fithub")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")  # Light grey background

        # Load images
        self.logo_image = PhotoImage(file="logo.png")  # Ensure logo.png is in the working directory

        # Create main frame and navigation menu
        self.create_navigation()
        self.create_main_frame()
        self.show_home()

    def create_navigation(self):
        # Navigation bar with improved styling
        self.nav_bar = tk.Frame(self, bg="#007bff", pady=10)
        self.nav_bar.pack(side=tk.TOP, fill=tk.X)

        sections = ["Home", "Nearby Gyms", "Live Stream", "Online Trainer", "Posts", "Tasks", "Fitness AI Monitor", "Fitness Shopping"]
        for section in sections:
            btn = ttk.Button(self.nav_bar, text=section, command=lambda s=section: self.show_section(s), style='Nav.TButton')
            btn.pack(side=tk.LEFT, padx=5)

        style = ttk.Style()
        style.configure('Nav.TButton', background="#0056b3", foreground="#ffffff", font=("Arial", 12))
        style.map('Nav.TButton', background=[('active', '#003d7a')])

    def create_main_frame(self):
        self.main_frame = tk.Frame(self, bg="#ffffff", padx=20, pady=20)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def show_section(self, section):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        if section == "Home":
            self.show_home()
        elif section == "Nearby Gyms":
            self.show_nearby_gyms()
        elif section == "Live Stream":
            self.show_live_stream()
        elif section == "Online Trainer":
            self.show_online_trainer()
        elif section == "Posts":
            self.show_posts()
        elif section == "Tasks":
            self.show_tasks()
        elif section == "Fitness AI Monitor":
            self.show_fitness_ai_monitor()
        elif section == "Fitness Shopping":
            self.show_fitness_shopping()

    def show_home(self):
        header = tk.Label(self.main_frame, text="Welcome to Fithub!", font=("Arial", 30, "bold"), bg="#ffffff", fg="#007bff")
        header.pack(pady=20)

        logo = tk.Label(self.main_frame, image=self.logo_image, bg="#ffffff")
        logo.pack(pady=10)

        desc = tk.Label(self.main_frame, text="Your ultimate fitness companion for finding gyms, live workouts, and more!", font=("Arial", 14), bg="#ffffff")
        desc.pack(pady=10)

    def show_nearby_gyms(self):
        self.create_section_header("Nearby Gyms")
        search_frame = tk.Frame(self.main_frame, bg="#ffffff")
        search_frame.pack(pady=10, fill=tk.X)

        search_entry = ttk.Entry(search_frame, font=("Arial", 12))
        search_entry.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)

        search_button = ttk.Button(search_frame, text="Search", style='Search.TButton')
        search_button.pack(side=tk.LEFT, padx=5)

        style = ttk.Style()
        style.configure('Search.TButton', background="#007bff", foreground="#ffffff", font=("Arial", 12))
        style.map('Search.TButton', background=[('active', '#003d7a')])

        # Placeholder for list of gyms
        listbox = tk.Listbox(self.main_frame, height=10, width=60, bg="#f9f9f9", font=("Arial", 12))
        listbox.pack(pady=10, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(self.main_frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

    def show_live_stream(self):
        self.create_section_header("Live Stream")
        tk.Label(self.main_frame, text="Live video feed here", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Label(self.main_frame, text="Upcoming sessions list", font=("Arial", 12), bg="#ffffff").pack(pady=10)
        tk.Listbox(self.main_frame, height=10, width=60, bg="#f9f9f9", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

    def show_online_trainer(self):
        self.create_section_header("Online Trainer")
        tk.Label(self.main_frame, text="Available Trainers", font=("Arial", 18), bg="#ffffff").pack(pady=10)
        tk.Listbox(self.main_frame, height=10, width=60, bg="#f9f9f9", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)
        tk.Label(self.main_frame, text="Chat with Trainer", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Text(self.main_frame, height=10, width=60, bg="#f9f9f9", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

    def show_posts(self):
        self.create_section_header("Posts")
        tk.Label(self.main_frame, text="Post Feed", font=("Arial", 18), bg="#ffffff").pack(pady=10)
        tk.Text(self.main_frame, height=15, width=80, bg="#f9f9f9", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

        post_frame = tk.Frame(self.main_frame, bg="#ffffff")
        post_frame.pack(pady=10, fill=tk.X)
        tk.Entry(post_frame, width=60, font=("Arial", 12)).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        tk.Button(post_frame, text="Post", style='Post.TButton').pack(side=tk.LEFT, padx=5)

        style = ttk.Style()
        style.configure('Post.TButton', background="#007bff", foreground="#ffffff", font=("Arial", 12))
        style.map('Post.TButton', background=[('active', '#003d7a')])

    def show_tasks(self):
        self.create_section_header("Tasks")
        tk.Label(self.main_frame, text="Task Management", font=("Arial", 18), bg="#ffffff").pack(pady=10)
        tk.Text(self.main_frame, height=15, width=80, bg="#f9f9f9", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

        task_frame = tk.Frame(self.main_frame, bg="#ffffff")
        task_frame.pack(pady=10, fill=tk.X)
        tk.Entry(task_frame, width=60, font=("Arial", 12)).pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        tk.Button(task_frame, text="Add Task", style='Task.TButton').pack(side=tk.LEFT, padx=5)

        style = ttk.Style()
        style.configure('Task.TButton', background="#007bff", foreground="#ffffff", font=("Arial", 12))
        style.map('Task.TButton', background=[('active', '#003d7a')])

    def show_fitness_ai_monitor(self):
        self.create_section_header("Fitness AI Monitor")
        tk.Label(self.main_frame, text="AI Fitness Dashboard", font=("Arial", 18), bg="#ffffff").pack(pady=10)
        tk.Label(self.main_frame, text="Metrics and recommendations", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Label(self.main_frame, text="Placeholder for detailed metrics", font=("Arial", 12), bg="#ffffff").pack(pady=10)

    def show_fitness_shopping(self):
        self.create_section_header("Fitness Shopping")
        tk.Label(self.main_frame, text="Shop Fitness Equipment", font=("Arial", 18), bg="#ffffff").pack(pady=10)
        tk.Label(self.main_frame, text="Product catalog here", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Button(self.main_frame, text="Add to Cart", style='Cart.TButton').pack(pady=10)

        style = ttk.Style()
        style.configure('Cart.TButton', background="#007bff", foreground="#ffffff", font=("Arial", 12))
        style.map('Cart.TButton', background=[('active', '#003d7a')])

    def create_section_header(self, title):
        header = tk.Label(self.main_frame, text=title, font=("Arial", 22, "bold"), bg="#ffffff", fg="#007bff")
        header.pack(pady=20)

if __name__ == "__main__":
    app = FithubApp()
    app.mainloop()
