import numpy as np
from tkinter import *
import matplotlib.pyplot as plt
from PIL import Image,ImageTk


def Data_Read():
    #myInfo.txt파일에서 data를 불러와 입력상자와 텍스트 상자에 표시하는 함수
    f2 = open('myInfo.txt', 'r')
    data = f2.readlines()
    f2.close()
    
    Name = data[0].rstrip('\n')
    Number = data[1].rstrip('\n')
    Major = data[2].rstrip('\n')
    Grade = data[3].rstrip('\n')

    # Data Write into Entry box
    e1.delete(0, END)
    e1.insert(END, Name)
    e2.delete(0, END)
    e2.insert(END, Number)
    e3.delete(0, END)
    e3.insert(END, Major)
    e4.delete(0, END)
    e4.insert(END, Grade)

    # Data Write into textbox
    t1.delete(1.0, END)
    t1.insert(END, '성명 : ' + Name + '\n')
    t1.insert(END, '학번 : ' + Number + '\n')
    t1.insert(END, '전공 : ' + Major + '\n')
    t1.insert(END, '학년 : ' + Grade + '\n')

def Data_Save():
    # Read Entry data
    Name = e1.get()
    Number = e2.get()
    Major = e3.get()
    Grade = e4.get()

    # Clear entry box
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    # Save Entry data to a file myInfo.txt
    f1 = open('myInfo.txt', 'w')
    f1.write(Name + '\n' + Number + '\n' + Major + '\n' + Grade + '\n')
    f1.close()

def Generate_Data1():
    file1 = open("data1.txt", 'r')
    gan_loss1 = []
    val_mse1 = []
    psnr1 = []
    mse1 = []
    epoch1 = []

    for line in file1.readlines():
        data = line.split()
        epoch1.append(int(data[0].lstrip('epoch')))
        gan_loss1.append(float(data[4].rstrip(';')))
        val_mse1.append(float(data[8].rstrip(';')))
        psnr1.append(float(data[11].rstrip(';')))
        mse1.append(float(data[14].rstrip(';')))

    file1.close()
    return epoch1, gan_loss1, val_mse1, psnr1, mse1

def Generate_Data2():
    file2 = open("data2.txt", 'r')
    gan_loss2 = []
    val_mse2 = []
    psnr2 = []
    mse2 = []
    epoch2 = []

    for line in file2.readlines():
        data = line.split()
        epoch2.append(int(data[0].lstrip('epoch')))
        gan_loss2.append(float(data[4].rstrip(';')))
        val_mse2.append(float(data[8].rstrip(';')))
        psnr2.append(float(data[11].rstrip(';')))
        mse2.append(float(data[14].rstrip(';')))

    file2.close()
    return epoch2, gan_loss2, val_mse2, psnr2, mse2

def Plot_GAN_Loss():
    epoch1, gan_loss1, _, _, _ = Generate_Data1()
    epoch2, gan_loss2, _, _, _ = Generate_Data2()

    plt.figure(2)

    # data1 GAN Loss 그래프
    plt.subplot(2, 1, 1)
    plt.plot(epoch1, gan_loss1)
    plt.xlabel('epochs')
    plt.ylabel('GAN Loss')
    plt.title("data1")
    plt.grid(True)

    # data2 GAN Loss 그래프
    plt.subplot(2, 1, 2)
    plt.plot(epoch2, gan_loss2)
    plt.xlabel('epochs')
    plt.ylabel('GAN Loss')
    plt.title("data2")
    plt.grid(True)

    plt.show()

def Plot_PSNR():
    epoch1, _, _, psnr1, _ = Generate_Data1()
    epoch2, _, _, psnr2, _ = Generate_Data2()

    plt.figure(3)

    # data1 PSNR 그래프
    plt.subplot(3, 1, 1)
    plt.plot(epoch1, psnr1)
    plt.xlabel('epochs')
    plt.ylabel('PSNR')
    plt.title("data1")
    plt.grid(True)

    # data2 PSNR 그래프
    plt.subplot(3, 1, 2)
    plt.plot(epoch2, psnr2)
    plt.xlabel('epochs')
    plt.ylabel('PSNR')
    plt.title("data2")
    plt.grid(True)

    plt.show()

def Plot_Val_MSE():
    epoch1, _, val_mse1, _, _ = Generate_Data1()
    epoch2, _, val_mse2, _, _ = Generate_Data2()

    plt.figure(4)

    # data1 Validation MSE 그래프
    plt.subplot(2, 1, 1)
    plt.plot(epoch1, val_mse1)
    plt.xlabel('epochs')
    plt.ylabel('Validation MSE')
    plt.title("data1")
    plt.grid(True)

    # data2 Validation MSE 그래프
    plt.subplot(2, 1, 2)
    plt.plot(epoch2, val_mse2)
    plt.xlabel('epochs')
    plt.ylabel('Validation MSE')
    plt.title("data2")
    plt.grid(True)

    plt.show()

def Plot_MSE():
    epoch1, _, _, _, mse1 = Generate_Data1()
    epoch2, _, _, _, mse2 = Generate_Data2()

    plt.figure(5)

    # data1 MSE 그래프
    plt.subplot(2, 1, 1)
    plt.plot(epoch1, mse1)
    plt.xlabel('epochs')
    plt.ylabel('MSE')
    plt.title("data1")
    plt.grid(True)

    # data2 MSE 그래프
    plt.subplot(2, 1, 2)
    plt.plot(epoch2, mse2)
    plt.xlabel('epochs')
    plt.ylabel('MSE')
    plt.title("data2")
    plt.grid(True)

    plt.show()

# 통계를 계산하는 함수 수정
def Calculate_Statistics():
    #data1 최대,최솟,평균 구하기
    file1 = open("data1.txt", 'r')
    gan_loss1 = []
    val_mse1 = []
    psnr1 = []
    mse1 = []
    epoch1 = []

    for line in file1.readlines():
        data = line.split()
        epoch1.append(int(data[0].lstrip('epoch')))
        gan_loss1.append(float(data[4].rstrip(';')))
        val_mse1.append(float(data[8].rstrip(';')))
        psnr1.append(float(data[11].rstrip(';')))
        mse1.append(float(data[14].rstrip(';')))

    file1.close()
    #data2 최대,최솟,평균구하기
    file2 = open("data2.txt", 'r')
    gan_loss2 = []
    val_mse2 = []
    psnr2 = []
    mse2 = []
    epoch2 = []

    for line in file2.readlines():
        data = line.split()
        epoch2.append(int(data[0].lstrip('epoch')))
        gan_loss2.append(float(data[4].rstrip(';')))
        val_mse2.append(float(data[8].rstrip(';')))
        psnr2.append(float(data[11].rstrip(';')))
        mse2.append(float(data[14].rstrip(';')))

    file2.close()

    # data2 통계 계산
    gan_loss2_min = min(gan_loss2)
    gan_loss2_max = max(gan_loss2)
    gan_loss2_avg = sum(gan_loss2) / len(gan_loss2)

    val_mse2_min = min(val_mse2)
    val_mse2_max = max(val_mse2)
    val_mse2_avg = sum(val_mse2) / len(val_mse2)

    psnr2_min = min(psnr2)
    psnr2_max = max(psnr2)
    psnr2_avg = sum(psnr2) / len(psnr2)

    mse2_min = min(mse2)
    mse2_max = max(mse2)
    mse2_avg = sum(mse2) / len(mse2)
    
    # data1 통계 계산
    gan_loss1_min = min(gan_loss1)
    gan_loss1_max = max(gan_loss1)
    gan_loss1_avg = sum(gan_loss1) / len(gan_loss1)

    val_mse1_min = min(val_mse1)
    val_mse1_max = max(val_mse1)
    val_mse1_avg = sum(val_mse1) / len(val_mse1)

    psnr1_min = min(psnr1)
    psnr1_max = max(psnr1)
    psnr1_avg = sum(psnr1) / len(psnr1)

    mse1_min = min(mse1)
    mse1_max = max(mse1)
    mse1_avg = sum(mse1) / len(mse1)

    # 텍스트 박스 업데이트
    with open("DataProcessing.txt", "w") as file:
        # Write the content to the file
        file.write("-data1의 데이터의 최대,최소,평균값-\n")
        file.write("GAN Loss:\n")
        file.write("최소값: {:.2f}\n".format(gan_loss1_min))
        file.write("최대값: {:.2f}\n".format(gan_loss1_max))
        file.write("평균값: {:.2f}\n\n".format(gan_loss1_avg))

        file.write("Validation MSE:\n")
        file.write("최소값: {:.2f}\n".format(val_mse1_min))
        file.write("최대값: {:.2f}\n".format(val_mse1_max))
        file.write("평균값: {:.2f}\n\n".format(val_mse1_avg))

        file.write("PSNR:\n")
        file.write("최소값: {:.2f}\n".format(psnr1_min))
        file.write("최대값: {:.2f}\n".format(psnr1_max))
        file.write("평균값: {:.2f}\n\n".format(psnr1_avg))

        file.write("MSE:\n")
        file.write("최소값: {:.2f}\n".format(mse1_min))
        file.write("최대값: {:.2f}\n".format(mse1_max))
        file.write("평균값: {:.2f}\n\n".format(mse1_avg))

        file.write("-data2의 데이터의 최대,최소,평균값-\n")
        file.write("GAN Loss:\n")
        file.write("최소값: {:.2f}\n".format(gan_loss2_min))
        file.write("최대값: {:.2f}\n".format(gan_loss2_max))
        file.write("평균값: {:.2f}\n\n".format(gan_loss2_avg))

        file.write("Validation MSE:\n")
        file.write("최소값: {:.2f}\n".format(val_mse2_min))
        file.write("최대값: {:.2f}\n".format(val_mse2_max))
        file.write("평균값: {:.2f}\n\n".format(val_mse2_avg))

        file.write("PSNR:\n")
        file.write("최소값: {:.2f}\n".format(psnr2_min))
        file.write("최대값: {:.2f}\n".format(psnr2_max))
        file.write("평균값: {:.2f}\n\n".format(psnr2_avg))

        file.write("MSE:\n")
        file.write("최소값: {:.2f}\n".format(mse2_min))
        file.write("최대값: {:.2f}\n".format(mse2_max))
        file.write("평균값: {:.2f}\n".format(mse2_avg))
        
    with open("DataProcessing.txt", "r") as file:
        content = file.read()
        
    # Update the text box
    t2.delete(1.0, END)
    t2.insert(END, content)

root = Tk()
blank_space = " "
root.title(20 * blank_space + "Term Project")

L1 = Label(root, text="개인정보 입력", fg="blue")
L1.grid(row=0, columnspan=2)
L2 = Label(root, text="성명")
L2.grid(row=1)
L3 = Label(root, text="학번")
L3.grid(row=2)
L4 = Label(root, text="전공")
L4.grid(row=3)
L5 = Label(root, text="학년")
L5.grid(row=4)

e1 = Entry(root)
e2 = Entry(root)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

e3 = Entry(root)
e4 = Entry(root)
e3.grid(row=3, column=1)
e4.grid(row=4, column=1)

B1 = Button(root, text='개인정보 불러오기', command=Data_Read)
B1.place(x=30,y=250)
B2 = Button(root, text='개인정보 저장', command=Data_Save)
B2.place(x=30,y=200)
B3 = Button(root, text='GAN Loss Plot', command=Plot_GAN_Loss)
B3.place(x=190,y=200)
B4 = Button(root, text='PSNR Plot', command=Plot_PSNR)
B4.place(x=190,y=250)
B5 = Button(root, text='Validation MSE Plot', command=Plot_Val_MSE)
B5.place(x=190,y=300)
B6 = Button(root, text='MSE Plot', command=Plot_MSE)
B6.place(x=190,y=350)
B7 = Button(root, text='Data Processing & Save', command=Calculate_Statistics)
B7.place(x=450,y=350)
B8 = Button(root, text='Data1', command=Generate_Data1)
B8.place(x=30,y=300)
B9 = Button(root, text='Data2', command=Generate_Data2)
B9.place(x=30,y=350)

t1 = Text(root, height=10, width=20)
t1.place(x=190, y=25)

L7 = Label(root, text="개인정보", fg="blue")
L7.place(x=245, y=0)

t2 = Text(root, height=15, width=35)
t2.place(x=390, y=25)

L8 = Label(root, text="데이터", fg="blue")
L8.place(x=500, y=0)

image=Image.open("hallym_logo.jpg")
image_tk=ImageTk.PhotoImage(image)
L9=Label(root,image=image_tk)
L9.place(x=650,y=350)

root.mainloop()
