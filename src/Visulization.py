import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

## Fungsi untuk menampilkan animasi pembentukan kurva bezier per iterasi
def Animation(alliterationresult,initial_point_list,iteration,elapsed_time,num_of_point):
    fig, ax = plt.subplots()
    x, y = [], []
    line, = ax.plot([], [], 'bo')

    ## Fungsi animasi untuk menghasilkan frame
    def animate(frame):
        result = alliterationresult[frame]
        x_handle = [p[0] for p in initial_point_list]
        y_handle = [p[1] for p in initial_point_list]
        x = [p[0] for p in result]
        y = [p[1] for p in result]
        fig.clear()
        plt.title(f'Iterasi {frame+1}', loc='right')
        plt.title(f'Waktu eksekusi : {elapsed_time}ms', loc='left')
        plt.xlabel(f"Jumlah titik : {num_of_point}")
        plt.plot(x_handle,y_handle,marker=".")
        plt.plot(x,y,marker=".")
        return line
    
    anim = FuncAnimation(fig,animate,frames=iteration,interval = 500) ## Meskipun tidak dipakai variabel anim wajib digunakan untuk menyimpan animasi
    plt.show()

## Fungsi menampilkan kurva bezier tanpa animasi pembentukan per iterasi
def Draw(result,initial_point_list,iteration,elapsed_time,num_of_point):
    x = [p[0] for p in result]
    y = [p[1] for p in result]
    x_handle = [p[0] for p in initial_point_list]
    y_handle = [p[1] for p in initial_point_list]
    plt.title(f'Iterasi {iteration}', loc='right')
    plt.title(f'Waktu eksekusi : {elapsed_time}ms', loc='left')
    plt.xlabel(f"Jumlah titik di generasi : {num_of_point}")
    plt.plot(x,y,marker=".")
    plt.plot(x_handle,y_handle,marker=".")
    plt.show()