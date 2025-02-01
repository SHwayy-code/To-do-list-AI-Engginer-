class AIEngineerRoadmap:
    def __init__(self):
        self.tasks = {
            "1": {"description": "Pelajari dasar-dasar Python", "completed": False},
            "2": {"description": "Pelajari matematika untuk AI (Aljabar Linear, Kalkulus, Probabilitas)", "completed": False},
            "3": {"description": "Pelajari konsep Machine Learning dasar", "completed": False},
            "4": {"description": "Pelajari library Python untuk AI (NumPy, Pandas, Matplotlib)", "completed": False},
            "5": {"description": "Pelajari framework Machine Learning (Scikit-Learn)", "completed": False},
            "6": {"description": "Pelajari Deep Learning (TensorFlow, PyTorch)", "completed": False},
            "7": {"description": "Bangun proyek kecil menggunakan Machine Learning", "completed": False},
            "8": {"description": "Pelajari Natural Language Processing (NLP)", "completed": False},
            "9": {"description": "Pelajari Computer Vision", "completed": False},
            "10": {"description": "Ikuti kompetisi AI (Kaggle)", "completed": False},
            "11": {"description": "Pelajari deployment model AI (Flask, FastAPI, Docker)", "completed": False},
            "12": {"description": "Buat portofolio proyek AI di GitHub", "completed": False},
            "13": {"description": "Terus update dengan riset terbaru di bidang AI", "completed": False},
        }

    def show_tasks(self):
        print("=== To-Do List Menjadi AI Engineer ===")
        for task_id, task_info in self.tasks.items():
            status = "✓" if task_info["completed"] else " "
            print(f"{task_id}. [{status}] {task_info['description']}")

    def complete_task(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id]["completed"] = True
            print(f"Task {task_id} selesai! Selamat! 🎉")
        else:
            print("Task tidak ditemukan. Cek kembali ID task.")

    def check_progress(self):
        total_tasks = len(self.tasks)
        completed_tasks = sum(1 for task in self.tasks.values() if task["completed"])
        progress = (completed_tasks / total_tasks) * 100
        print(f"\nProgres Anda: {completed_tasks}/{total_tasks} task selesai ({progress:.2f}%)")
        if progress == 100:
            print("Selamat! Anda sudah menyelesaikan roadmap menjadi AI Engineer! 🚀")

# Contoh penggunaan
roadmap = AIEngineerRoadmap()

while True:
    print("\nMenu:")
    print("1. Lihat To-Do List")
    print("2. Tandai Task sebagai Selesai")
    print("3. Cek Progres")
    print("4. Keluar")
    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        roadmap.show_tasks()
    elif choice == "2":
        task_id = input("Masukkan ID task yang sudah selesai: ")
        roadmap.complete_task(task_id)
    elif choice == "3":
        roadmap.check_progress()
    elif choice == "4":
        print("Terima kasih! Semangat belajar! 💪")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
