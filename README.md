# 跑tangent convolution代码笔记
## 前期准备工作
首先clone一下代码

```bash
git clone https://github.com/tatarchm/tangent_conv.git
```

根据Pre-prequisites：

```
python == 3.6
tensorflow >= 1.3
joblib
```

用docker pull下tensorflow的镜像

```bash
docker pull tensorflow/tensorflow:1.3.0-gpu-py3
```

用nvidia-docker创建容器，将tangent convolution的代码挂载进去，可以同时挂载自己需要的数据集

```bash
nvidia-docker run -it \
-e DISPLAY -e="QT_X11_NO_MITSHM=1" -e GDK_SCALE -e GDK_DPI_SCALE \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v '/home/youkenhou/tangent_conv':/tangent_conv \
tensorflow/tensorflow:1.3.0-gpu-py3 bash
```

打开容器之后安装joblib

```
pip3 install joblib
```

根据说明进行下一步，clone作者提供的Open3D

```bash
git clone https://github.com/tatarchm/Open3D.git
```

```bash
cd Open3D
util/scripts/install-deps-ubuntu.sh
```

经过以上步骤会装好Open3D编译所需的环境。但是在这里```install-deps-ubuntu.sh```会安装python2，导致之后的cmake会默认使用python2，而无法正确编译，之后会报```No module named 'py3d'```错误，所以要进行以下的步骤。

首先安装cmake

```bash
apt-get install -y cmake automake
```

再稍微修改作者提供的步骤，指定python3的位置

```bash
mkdir build
cd build
cmake -DPYTHON_EXECUTABLE:FILEPATH=/usr/bin/python3.5 ../src
make
```

以上修改参照[这里](https://github.com/IntelVCL/Open3D/issues/129)。

编译好之后进入```build/lib```，确认是否成功编译了py3d

```bash
python3
>>> from py3d import *
>>>
```

能够import py3d说明成功了，接下来按照说明添加Open3D以及tangent convolution的路径。

打开```tangent_conv/util/path_config.py```，修改两行代码

```python
open3d_path = '/tangent_conv/Open3D/build/lib/'
tc_path = '/tangent_conv/'
```

接下来就可以利用作者提供的脚本下载数据集并处理，这里下载了semantic3d的数据，一点小修改，需要把python改成python3，否则就会提示```No module named 'py3d'```

```bash
python3 get_data.py <directory_for_downloaded_files> <desired_output_directory> semantic3d
```

运行过程中可能会提示```No module named 'wget'```，只要安装wget就可以了

```bash
pip3 install wget
```

脚本运行过程中还会出现```sh: 1: 7z: not found```的错误，是因为没有安装解压软件

```bash
apt-get install p7zip-full
```

再次运行脚本，就可以开始下载semantic3d数据集了。注意这个数据集很大，要留好硬盘空间。

precompute.py中有旋转数据集以扩大的代码rotation，会把一个数据旋转八次，占巨大空间。

作者的semantic3d数据读取部分有些bug，所以没有跑通。

上述容器配置好之后，可以使用commit将容器保存为新的镜像
```bash
commit $container id$ tangent_conv:v1
```
之后再进行实验就可以利用新的命令
```bash
nvidia-docker run -it --rm --cpus=6 -m 24576M -p 6006:6006 \
-e DISPLAY -e="QT_X11_NO_MITSHM=1" -e GDK_SCALE -e GDK_DPI_SCALE \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-v '/home/youkenhou/tangent_conv':/tangent_conv \
tangent_conv:v1 bash
```
```--cpus```可以限制容器使用的cpu数，```-m```可以限制容器使用的内存量，```-p```可以映射端口，进行tensorboard查看。

## 将阿里点云分割比赛的数据集转换为网络输入的数据格式
阿里点云分割比赛的训练集数据格式：```pts```文件夹包含了点云xyz坐标信息，```intensity```文件夹包含了点云强度信息，```label```文件夹包含了点云的分类，这三个文件夹中的文件名、文件个数都是对应的。

假设一个文件为```12345.csv```，```pts/12345.csv```是一个```n行3列```的数组，```intensity/12345.csv```是一个```n行1列```的数组，```label/12345.csv```是一个```n行1列```的数组。

tangent convolution的输入格式是n个文件夹，根据文件夹的名字来定义每一个输入文件，每个文件夹中包含了一个```scan.pcd```文件和一个```scan.labels```文件，根据作者的数据处理代码可以将阿里的数据```pts```转换为```scan.pcd```，```label```文件可以直接复制为```scan.labels```，改个名字就可以。

