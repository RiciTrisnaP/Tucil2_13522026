import time
from Visulization import Animation, Draw

def GeneralBezierDAC(initial_point_list, cur_iteration, iteration):
    # Mengenerasi subpoint dan titik estimasi kemudian membagi masalah menjadi dua
    left_initial_point, right_initial_point = Subdivide(initial_point_list)

    left_initial_point.insert(0,initial_point_list[0]) ## Menambahkan titik handle kurva paling ujung kiri
    right_initial_point.extend([initial_point_list[-1]]) ## Menambahkan titik handle kurva ujung kanan

    if cur_iteration < iteration: ## Apabila iterasi masih belum selesai maka lanjutkan DAC
        ## Mencari solusi dari dua bagian masalah
        left_result = GeneralBezierDAC(left_initial_point,cur_iteration+1,iteration)
        right_result = GeneralBezierDAC(right_initial_point, cur_iteration+1,iteration)
        ## Tahap menggabungkan kedua solusi dari dua bagian yang berbeda
        result = Merge(left_result,right_result)
        return result
    
    result = [left_initial_point[0], left_initial_point[-1],right_initial_point[-1]]
    return result

def Subdivide(initial_point_list):

    subPointList = [] ## List yang menampung semua subpoint yang digenerasi
    for i in range(0,len(initial_point_list)-1): ## Mengenerasi subpoint
        Point1, Point2 = initial_point_list[i:i+2]
        subPoint = SubPoint(Point1,Point2)
        subPointList.append(subPoint)
    
    if(len(subPointList) == 1): ## Apabila sudah menghasilkan titik estimasi
        return subPointList, subPointList.copy()

    subPointListCopy = subPointList ## Membuat salinan Subpointlist untuk selanjutnya di cari subpoint untuk titik-titik pada list tersebut
    left, right = Subdivide(subPointListCopy)
    left.insert(0,subPointList[0])
    right.append(subPointList[-1])

    return left, right

def Merge(list1,list2):
    result = list1 + list2[1:] 
    return result
    
## Fungsi untuk mencari midpoint dari dua buah point
def SubPoint(Point1,Point2):
    return ((Point1[0] + Point2[0]) / 2, (Point1[1] + Point2[1]) / 2)

## fungsi main
def main():
    initial_point_list = [] ## List titik handle kurva bezier
    ## Input derajat
    n = int(input("Masukkan derajat: "))
    ## Input jumlah iterasi
    iteration = int(input("Masukkan jumlah iterasi: "))

    ## Input titik
    for i in range(1,n+2):
        x,y = [int(i) for i in input(f"Masukkan titik ke {i}: ").split(" ")]
        initial_point_list.append((x,y))
    
     ## Input pilihan untuk menampilkan animasi
    draw_stepbystep = input("Apakah animasi pembentukan ditampilkan? (y/n): ")

    ## Mencari waktu running dan jumlah titik yang di generasi
    start = time.time()
    result = GeneralBezierDAC(initial_point_list,1,iteration)
    elapsed_time = time.time() - start
    num_of_point = len(result)

     # Mengecek apakah pengguna ingin digambar stepnya
    if draw_stepbystep in ["y","Y","yes","Yes","YES"]:
        alliterationresult = []
        for i in range(1,iteration+1):
            point_list = GeneralBezierDAC(initial_point_list,1,i)
            alliterationresult.append(point_list)
        Animation(alliterationresult,initial_point_list,iteration,elapsed_time,num_of_point) ## jika iya animasikan pembentukan kurva
    else:
        Draw(result,initial_point_list,iteration,elapsed_time,num_of_point) ## jika tidak cukup gambar hasil akhir