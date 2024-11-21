"""
Modules
"""
import tkinter as tk

""""
Obtenir les paramètres
"""

def get_user_input():
    root = tk.Tk()
    root.withdraw()

    def get_input():
        resolution = resolution_entry.get()
        cmap = cmap_var.get()
        speed = int(speed_entry.get())
        B1 = float(B1_entry.get())
        B2 = float(B2_entry.get())
        D1 = float(D1_entry.get())
        D2 = float(D2_entry.get())
        alpha_n = float(alpha_n_entry.get())
        alpha_m = float(alpha_m_entry.get())
        count = count_entry.get()
        count = int(count) if count.isdigit() else None
        intensity = float(intensity_entry.get())
        inner_radius = float(inner_radius_entry.get())
        outer_radius = float(outer_radius_entry.get())
        sigmode = int(sigmode_var.get())
        sigtype = int(sigtype_var.get())
        mixtype = int(mixtype_var.get())
        timestep_mode = int(timestep_mode_var.get())
        dt = float(dt_entry.get())
        glider = glider_var.get()
        save = save_var.get()
        root.quit()
        return (resolution, cmap, speed, B1, B2, D1, D2, alpha_n, alpha_m, count, intensity, inner_radius, outer_radius, sigmode, sigtype, mixtype, timestep_mode, dt, glider, save)

    dialog = tk.Toplevel(root)
    dialog.title("Paramètres d'entrée")

    tk.Label(dialog, text="Résolution (largeur,hauteur):").grid(row=0, column=0)
    resolution_entry = tk.Entry(dialog)
    resolution_entry.insert(0, "256,256")
    resolution_entry.grid(row=0, column=1)

    tk.Label(dialog, text="Colormap:").grid(row=1, column=0)
    cmap_var = tk.StringVar(dialog)
    cmap_var.set("viridis")
    cmap_menu = tk.OptionMenu(dialog, cmap_var, "viridis", "plasma", "gray", "binary", "seismic", "gnuplot")
    cmap_menu.grid(row=1, column=1)

    tk.Label(dialog, text="Intervalle (ms):").grid(row=2, column=0)
    speed_entry = tk.Entry(dialog)
    speed_entry.insert(0, "60")
    speed_entry.grid(row=2, column=1)

    tk.Label(dialog, text="B1:").grid(row=3, column=0)
    B1_entry = tk.Entry(dialog)
    B1_entry.insert(0, "0.278")
    B1_entry.grid(row=3, column=1)

    tk.Label(dialog, text="B2:").grid(row=4, column=0)
    B2_entry = tk.Entry(dialog)
    B2_entry.insert(0, "0.365")
    B2_entry.grid(row=4, column=1)

    tk.Label(dialog, text="D1:").grid(row=5, column=0)
    D1_entry = tk.Entry(dialog)
    D1_entry.insert(0, "0.267")
    D1_entry.grid(row=5, column=1)

    tk.Label(dialog, text="D2:").grid(row=6, column=0)
    D2_entry = tk.Entry(dialog)
    D2_entry.insert(0, "0.445")
    D2_entry.grid(row=6, column=1)

    tk.Label(dialog, text="alpha_n:").grid(row=7, column=0)
    alpha_n_entry = tk.Entry(dialog)
    alpha_n_entry.insert(0, "0.028")
    alpha_n_entry.grid(row=7, column=1)

    tk.Label(dialog, text="alpha_m:").grid(row=8, column=0)
    alpha_m_entry = tk.Entry(dialog)
    alpha_m_entry.insert(0, "0.147")
    alpha_m_entry.grid(row=8, column=1)

    tk.Label(dialog, text="Nombre (ou laisser vide pour défaut):").grid(row=9, column=0)
    count_entry = tk.Entry(dialog)
    count_entry.grid(row=9, column=1)

    tk.Label(dialog, text="Intensité:").grid(row=10, column=0)
    intensity_entry = tk.Entry(dialog)
    intensity_entry.insert(0, "1")
    intensity_entry.grid(row=10, column=1)

    tk.Label(dialog, text="Rayon intérieur:").grid(row=11, column=0)
    inner_radius_entry = tk.Entry(dialog)
    inner_radius_entry.insert(0, "7")
    inner_radius_entry.grid(row=11, column=1)

    tk.Label(dialog, text="Rayon extérieur:").grid(row=12, column=0)
    outer_radius_entry = tk.Entry(dialog)
    outer_radius_entry.insert(0, "21")
    outer_radius_entry.grid(row=12, column=1)

    tk.Label(dialog, text="Sigmode:").grid(row=13, column=0)
    sigmode_var = tk.StringVar(dialog)
    sigmode_var.set("2")
    sigmode_menu = tk.OptionMenu(dialog, sigmode_var, "0", "1", "2", "3")
    sigmode_menu.grid(row=13, column=1)

    tk.Label(dialog, text="Sigtype:").grid(row=14, column=0)
    sigtype_var = tk.StringVar(dialog)
    sigtype_var.set("2")
    sigtype_menu = tk.OptionMenu(dialog, sigtype_var, "0", "1", "2")
    sigtype_menu.grid(row=14, column=1)

    tk.Label(dialog, text="Mixtype:").grid(row=15, column=0)
    mixtype_var = tk.StringVar(dialog)
    mixtype_var.set("2")
    mixtype_menu = tk.OptionMenu(dialog, mixtype_var, "0", "1", "2")
    mixtype_menu.grid(row=15, column=1)

    tk.Label(dialog, text="Timestep Mode:").grid(row=16, column=0)
    timestep_mode_var = tk.StringVar(dialog)
    timestep_mode_var.set("0")
    timestep_mode_menu = tk.OptionMenu(dialog, timestep_mode_var, "0", "1", "2", "3", "4", "5")
    timestep_mode_menu.grid(row=16, column=1)

    tk.Label(dialog, text="dt:").grid(row=17, column=0)
    dt_entry = tk.Entry(dialog)
    dt_entry.insert(0, "0.1")
    dt_entry.grid(row=17, column=1)

    glider_var = tk.BooleanVar()
    tk.Checkbutton(dialog, text="Ajouter des planeurs?", variable=glider_var).grid(row=18, columnspan=2)

    save_var = tk.BooleanVar()
    tk.Checkbutton(dialog, text="Sauvegarder le champ?", variable=save_var).grid(row=19, columnspan=2)

    tk.Button(dialog, text="Soumettre", command=lambda: get_input()).grid(row=20, columnspan=2)

    root.mainloop()
    return get_input()
