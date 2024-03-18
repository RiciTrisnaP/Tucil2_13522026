import time
from Visulization import Animation, Draw

def QuadraticBezierBF(initial_point_list,iteration):
    step = 2**(iteration) ##  Membuat jumlah step dari nilai t
    increment = 1 / step ## Increment dari nilai t

    ## Membuat daftar nilai t yang akan digunakan untuk mengenerasi titik dengan BF
    listOfTValue = [i * increment for i in range(1,step+1)]

    ## Membuat list penampung titik yang tergenerasi
    result = [initial_point_list[0]] ## Menambahkan titik awal ke dalam list result
    for i in listOfTValue:
        temp = lerpAllTheWay(initial_point_list,i) ## Melakukan linear interpolasi pada tiap nilai t
        result.append(temp)

    return result
 
def lerpAllTheWay(initial_point_list,t): ## De Casteljau's Algorithm

    if len(initial_point_list) == 1: ## Apabila telah didapat satu titik estimasi
        return initial_point_list[0]

    subPointList = [] ## List penampung subpoint sesuai hasil linear interpolation pada nilai t saat ini
    for i in range(0,len(initial_point_list)-1): ## Mengenerasi subpoint sesuai nilai t dan list subpoint saat ini
        Point1, Point2 = initial_point_list[i:i+2]
        subPoint = lerp(Point1,Point2,t)
        subPointList.append(subPoint)
    
    result = lerpAllTheWay(subPointList,t) ## Melakukan linear interpolation pada subpoint list hingga didapat satu titik
    return result

def lerp(Point1,Point2,t): ## Linear interpolation
    return ((1 - t) * Point1[0] + t * Point2[0], (1 - t) * Point1[1] + t * Point2[1])

def main():
    initial_point_list = [] ## List titik handle kurva bezier
    ## Input jumlah iterasi
    iteration = int(input("Masukkan jumlah iterasi: "))

    ## input titik
    for i in range(1,4):
        x,y = [int(i) for i in input(f"Masukkan titik ke {i}: ").split(" ")]
        initial_point_list.append((x,y))

    ## Input pilihan untuk menampilkan animasi
    draw_stepbystep = input("Apakah animasi pembentukan ditampilkan? (y/n): ")

    ## Mencari waktu running dan jumlah titik yang di generasi
    start = time.time()
    result = QuadraticBezierBF(initial_point_list,iteration)
    elapsed_time = time.time() - start
    num_of_point = len(result)

    # Mengecek apakah pengguna ingin digambar stepnya
    if draw_stepbystep in ["y","Y","yes","Yes","YES"]:
        alliterationresult = []
        for i in range(1,iteration+1):
            point_list = QuadraticBezierBF(initial_point_list,i)
            alliterationresult.append(point_list)
        Animation(alliterationresult,initial_point_list,iteration,elapsed_time,num_of_point) ## jika iya animasikan pembentukan kurva
    else:
        Draw(result,initial_point_list,iteration,elapsed_time,num_of_point) ## jika tidak cukup gambar hasil akhir