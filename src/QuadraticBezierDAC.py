import time
from Visulization import Animation, Draw

def QuadraticBezierDAC(Point1,Point2,Point3,cur_iteration,iteration):
    ## Membentuk dua buah subpoint dan sebuah titik estimasi
    SubPoint1 = SubPoint(Point1,Point2)
    SubPoint2 = SubPoint(Point2,Point3)
    ResultPoint = SubPoint(SubPoint1,SubPoint2)

    ## Apabila iterasi masih berlanjut maka kembali panggil fungsi secara rekursi hingga iterasi selesai
    if cur_iteration < iteration:
        ## Mencari solusi dari dua buah pecahan masalah
        left = QuadraticBezierDAC(Point1, SubPoint1, ResultPoint, cur_iteration + 1, iteration)
        right = QuadraticBezierDAC(ResultPoint, SubPoint2, Point3, cur_iteration + 1, iteration)
        result = Merge(left,right) ## Menggabungkan kedua buah pecahan solusi
        return result
    
    result = ([Point1, ResultPoint, Point3])
    return result

## Fungsi untuk menggabung dua buah solusi 
def Merge(list1,list2):
    result = list1[:-1]
    result.extend(list2)
    return result

## Fungsi untuk mencari midpoint dari dua buah point
def SubPoint(Point1,Point2):
    return ((Point1[0] + Point2[0]) / 2, (Point1[1] + Point2[1]) / 2)

def main():
    
    initial_point_list = [] ## List titik handle kurva bezier
    # Input jumlah iterasi
    iteration = int(input("Masukkan jumlah iterasi: ")) ## jumlah iterasi
    ## Input titik
    for i in range(1,4):
        x,y = [int(i) for i in input(f"Masukkan titik ke {i}: ").split(" ")]
        initial_point_list.append((x,y))
    
    ## Input pilihan untuk menampilkan animasi
    draw_stepbystep = input("Apakah animasi pembentukan ditampilkan? (y/n): ")

    Point1,Point2,Point3 = initial_point_list ## memecah initial_point_list menjadi 3 buah point

    ## Mencari waktu running dan jumlah titik yang di generasi
    start = time.time()
    result = QuadraticBezierDAC(Point1,Point2,Point3,1,iteration)
    elapsed_time = time.time() - start
    num_of_point = len(result)

    # Mengecek apakah pengguna ingin digambar stepnya
    if draw_stepbystep in ["y","Y","yes","Yes","YES"]:
        alliterationresult = []
        for i in range(1,iteration+1):
            point_list = QuadraticBezierDAC(Point1,Point2,Point3,1,i)
            alliterationresult.append(point_list)
        Animation(alliterationresult,initial_point_list,iteration,elapsed_time,num_of_point) ## jika iya animasikan pembentukan kurva
    else:
        Draw(result,initial_point_list,iteration,elapsed_time,num_of_point) ## jika tidak cukup gambar hasil akhir