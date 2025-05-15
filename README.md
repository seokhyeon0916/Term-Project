# Term Project
2023학년 1학기 파이썬 과학 기초프로그래밍 기말프로젝트

# 개요
파이썬 Tkinter모듈과 Numpy모듈을 이용하여 사용자의 개인정보를 읽고 저장하며 각 데이터의 자료를 그래프화 하는 프로그램

# 프로젝트 목표 및 내용
#### 이 프로젝트의 목표

1.사용자가 입력하는 정보를 정확하게 읽어서 myinfo.txt파일에 저장해야 하며 다시 정보를 불러올 때 파일에서부터 불러올 수 있어야 한다.
``` bash
def save_info():
    name = name_entry.get()
    id_ = id_entry.get()
    major = major_entry.get()
    year = year_entry.get()

    with open("myInfo.txt", "w") as f:
        f.write(f"{name}\n{id_}\n{major}\n{year}")

def load_info():
    with open("myInfo.txt", "r") as f:
        lines = f.readlines()
        name_entry.delete(0, END)
        name_entry.insert(0, lines[0].strip())
        id_entry.delete(0, END)
        id_entry.insert(0, lines[1].strip())
        major_entry.delete(0, END)
        major_entry.insert(0, lines[2].strip())
        year_entry.delete(0, END)
        year_entry.insert(0, lines[3].strip())
```

2.data1과 data2버튼을 클릭했을 시 data1.txt파일과 data2.txt파일에서 데이터들을 불러와 리스트화 시켜야 한다.
```bash
data1_list = []
data2_list = []

def load_data1():
    with open("data1.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            epoch, loss, mse, psnr = map(float, line.strip().split(","))
            data1_list.append((epoch, loss, mse, psnr))


def load_data2():
    with open("data2.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            epoch, loss, mse, psnr = map(float, line.strip().split(","))
            data2_list.append((epoch, loss, mse, psnr))
```

3.각 데이터 plot버튼을 클릭했을 시 정확한 그래프의 형태가 나와야 한다.
```bash
def plot_data1():
    if not data1_list:
        return
    epochs = [x[0] for x in data1_list]
    loss = [x[1] for x in data1_list]
    mse = [x[2] for x in data1_list]
    psnr = [x[3] for x in data1_list]

    plt.subplot(3, 1, 1)
    plt.plot(epochs, loss, label="Loss")
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(epochs, mse, label="MSE")
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(epochs, psnr, label="PSNR")
    plt.grid()

    plt.show()


def plot_data2():
    if not data2_list:
        return
    epochs = [x[0] for x in data2_list]
    loss = [x[1] for x in data2_list]
    mse = [x[2] for x in data2_list]
    psnr = [x[3] for x in data2_list]

    plt.subplot(3, 1, 1)
    plt.plot(epochs, loss, label="Loss")
    plt.grid()

    plt.subplot(3, 1, 2)
    plt.plot(epochs, mse, label="MSE")
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.plot(epochs, psnr, label="PSNR")
    plt.grid()

    plt.show()
```

4.dataprocessing&save버튼을 클릭했을 시 data1 버튼과 data2버튼을 클릭해서 만들어진 리스트들을 가지고 각 정보의 최대, 최소, 평균값을 구하여
dataprocessing.txt파일에 저장해야 하며 그 정보들을 파일에서부터 불러와 데이터 텍스트 박스에 출력해야 한다.

```bash
def data_processing():
    if not data1_list or not data2_list:
        return

    all_data = data1_list + data2_list
    loss_list = [x[1] for x in all_data]
    mse_list = [x[2] for x in all_data]
    psnr_list = [x[3] for x in all_data]

    max_loss = max(loss_list)
    min_loss = min(loss_list)
    avg_loss = sum(loss_list) / len(loss_list)

    max_mse = max(mse_list)
    min_mse = min(mse_list)
    avg_mse = sum(mse_list) / len(mse_list)

    max_psnr = max(psnr_list)
    min_psnr = min(psnr_list)
    avg_psnr = sum(psnr_list) / len(psnr_list)

    with open("DataProcessing.txt", "w") as f:
        f.write(f"Loss: max={max_loss}, min={min_loss}, avg={avg_loss}\n")
        f.write(f"MSE: max={max_mse}, min={min_mse}, avg={avg_mse}\n")
        f.write(f"PSNR: max={max_psnr}, min={min_psnr}, avg={avg_psnr}\n")

    with open("DataProcessing.txt", "r") as f:
        contents = f.read()
        data_text.delete("1.0", END)
        data_text.insert(END, contents)
```


# 개발 환경
* Python
* Library/Package: numpy, tkinter, matplotlib.pylpot, PIL.Image, PIL.ImageTK
