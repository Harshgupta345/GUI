import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, PhotoImage

class FithubApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fithub")
        self.geometry("1200x800")
        self.configure(bg="#ffffff")  # White background for the main window

        # Load images
        self.logo_image = PhotoImage(file="logo.png")  # Ensure logo.png is in the working directory
        self.banner_image = PhotoImage(file="banner.png")  # Ensure banner.png is in the working directory

        # Create the main layout
        self.create_navigation()
        self.create_main_frame()
        self.show_home()

    def create_navigation(self):
        # Navigation bar with vibrant colors and modern styling
        self.nav_bar = tk.Frame(self, bg="#ff5722", pady=10)
        self.nav_bar.pack(side=tk.TOP, fill=tk.X)

        sections = ["Home", "Nearby Gyms", "Live Stream", "Online Trainer", "Posts", "Tasks", "Fitness AI Monitor", "Fitness Shopping"]
        for section in sections:
            btn = ttk.Button(self.nav_bar, text=section, command=lambda s=section: self.show_section(s), style='Nav.TButton')
            btn.pack(side=tk.LEFT, padx=10)

        # Define the style for navigation buttons
        style = ttk.Style()
        style.configure('Nav.TButton', background="#ff5722", foreground="#ffffff", font=("Arial", 12, "bold"), padding=10)
        style.map('Nav.TButton', background=[('active', '#e64a19')])

    def create_main_frame(self):
        # Create main content frame with a banner
        self.main_frame = tk.Frame(self, bg="#ffffff")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        banner = tk.Label(self.main_frame, image=self.banner_image, bg="#ffffff")
        banner.pack(pady=10, fill=tk.X)

    def show_section(self, section):
        # Clear the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        
        # Re-add the banner
        banner = tk.Label(self.main_frame, image=self.banner_image, bg="#ffffff")
        banner.pack(pady=10, fill=tk.X)

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
        header = tk.Label(self.main_frame, text="Welcome to Fithub!", font=("Arial", 36, "bold"), bg="#ffffff", fg="#ff5722")
        header.pack(pady=20)

        logo = tk.Label(self.main_frame, image=self.logo_image, bg="#ffffff")
        logo.pack(pady=10)

        desc = tk.Label(self.main_frame, text="Your ultimate fitness companion for finding gyms, live workouts, and more!", font=("Arial", 16), bg="#ffffff", fg="#333333")
        desc.pack(pady=20)

    def show_nearby_gyms(self):
        self.create_section_header("Nearby Gyms")
        search_frame = tk.Frame(self.main_frame, bg="#ffffff")
        search_frame.pack(pady=20, fill=tk.X)

        search_entry = ttk.Entry(search_frame, font=("Arial", 14))
        search_entry.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

        search_button = ttk.Button(search_frame, text="Search", style='Search.TButton')
        search_button.pack(side=tk.LEFT, padx=10)

        # Define the style for search button
        style = ttk.Style()
        style.configure('Search.TButton', background="#ff5722", foreground="#ffffff", font=("Arial", 14, "bold"))
        style.map('Search.TButton', background=[('active', '#e64a19')])

        listbox_frame = tk.Frame(self.main_frame, bg="#ffffff")
        listbox_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        listbox = tk.Listbox(listbox_frame, height=15, width=80, bg="#f5f5f5", font=("Arial", 12))
        listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

    def show_live_stream(self):
        self.create_section_header("Live Stream")
        tk.Label(self.main_frame, text="Live video feed here", font=("Arial", 16), bg="#ffffff", fg="#ff5722").pack(pady=20)
        tk.Label(self.main_frame, text="Upcoming sessions list", font=("Arial", 14), bg="#ffffff", fg="#333333").pack(pady=10)
        tk.Listbox(self.main_frame, height=15, width=80, bg="#f5f5f5", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

    def show_online_trainer(self):
        self.create_section_header("Online Trainer")
        tk.Label(self.main_frame, text="Available Trainers", font=("Arial", 24, "bold"), bg="#ffffff", fg="#ff5722").pack(pady=20)
        tk.Listbox(self.main_frame, height=15, width=80, bg="#f5f5f5", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)
        tk.Label(self.main_frame, text="Chat with Trainer", font=("Arial", 16), bg="#ffffff", fg="#333333").pack(pady=20)
        tk.Text(self.main_frame, height=10, width=80, bg="#f5f5f5", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

    def show_posts(self):
        self.create_section_header("Posts")
        tk.Label(self.main_frame, text="Post Feed", font=("Arial", 24, "bold"), bg="#ffffff", fg="#ff5722").pack(pady=20)
        tk.Text(self.main_frame, height=15, width=80, bg="#f5f5f5", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

        post_frame = tk.Frame(self.main_frame, bg="#ffffff")
        post_frame.pack(pady=10, fill=tk.X)
        tk.Entry(post_frame, width=60, font=("Arial", 14)).pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        tk.Button(post_frame, text="Post", style='Post.TButton').pack(side=tk.LEFT, padx=10)

        style = ttk.Style()
        style.configure('Post.TButton', background="#ff5722", foreground="#ffffff", font=("Arial", 14, "bold"))
        style.map('Post.TButton', background=[('active', '#e64a19')])

    def show_tasks(self):
        self.create_section_header("Tasks")
        tk.Label(self.main_frame, text="Task Management", font=("Arial", 24, "bold"), bg="#ffffff", fg="#ff5722").pack(pady=20)
        tk.Text(self.main_frame, height=15, width=80, bg="#f5f5f5", font=("Arial", 12)).pack(pady=10, fill=tk.BOTH, expand=True)

        task_frame = tk.Frame(self.main_frame, bg="#ffffff")
        task_frame.pack(pady=10, fill=tk.X)
        tk.Entry(task_frame, width=60, font=("Arial", 14)).pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        tk.Button(task_frame, text="Add Task", style='Task.TButton').pack(side=tk.LEFT, padx=10)

        style = ttk.Style()
        style.configure('Task.TButton', background="#ff5722", foreground="#ffffff", font=("Arial", 14, "bold"))
        style.map('Task.TButton', background=[('active', '#e64a19')])

    def show_fitness_ai_monitor(self):
        self.create_section_header("Fitness AI Monitor")
        tk.Label(self.main_frame, text="AI Fitness Dashboard", font=("Arial", 24, "bold"), bg="#ffffff", fg="#ff5722").pack(pady=20)
        tk.Label(self.main_frame, text="Metrics and recommendations", font=("Arial", 16), bg="#ffffff", fg="#333333").pack(pady=10)
        tk.Label(self.main_frame, text="Placeholder for detailed metrics", font=("Arial", 14), bg="#ffffff", fg="#333333").pack(pady=10)

    def show_fitness_shopping(self):
        self.create_section_header("Fitness Shopping")
        tk.Label(self.main_frame, text="Shop Fitness Equipment", font=("Arial", 24, "bold"), bg="#ffffff", fg="#ff5722").pack(pady=20)
        tk.Label(self.main_frame, text="Product catalog here", font=("Arial", 16), bg="#ffffff", fg="#333333").pack(pady=10)
        tk.Button(self.main_frame, text="Add to Cart", style='Cart.TButton').pack(pady=10)

        style = ttk.Style()
        style.configure('Cart.TButton', background="#ff5722", foreground="#ffffff", font=("Arial", 14, "bold"))
        style.map('Cart.TButton', background=[('active', '#e64a19')])

    def create_section_header(self, title):
        header = tk.Label(self.main_frame, text=title, font=("Arial", 28, "bold"), bg="#ffffff", fg="#ff5722")
        header.pack(pady=20)

if __name__ == "__main__":
    app = FithubApp()
    app.mainloop()
