![image](http://img1.bj.wezhan.cn/content/sitefiles/2026736/images/9955151_ruituotech_376069de-c817-4c30-b8d0-2a433f6b58aa_resize_picture.jpeg)

# vicinspector

给VIC软件的z3d文件添加提取工具

A script to bulk copy inspectors of the VIC software

# Demo 

The gif shows how to use the vicinspector to bulk copy inspectors by command line.

![image](http://image.ruituo.work/vicinspector-demo.gif)

# Steps

The steps are：

- Download the vicinspector.rar in the 'package' folder.

- Unzip the rar file.

- Click the vicinspector.bat and start the command line window.

- Input the your command with the Synopsis：

`vicinspector <the path of z3d file> [-t tool] [-m mode] [-s 100 0] [-n 2] `
  
 - The command line window will display success signal and you can open the z3d file to check the result.

# Usage

- You can learn the detailed usages of the vicinspector by seeing the [Toturial 1](https://www.bilibili.com/video/av43218925) and [Toturial 2](https://www.bilibili.com/video/av43317433)

- In addition you can input `vicinspector -h ` to get the help information in the command line.

The information is:

```

usage: vicinspector .z3d文件路径 -t 矩形 -m 复制 -s 100 0 -n 2

使用方法： vicinspector脚本是用于z3d文件添加提取工具，用法是 vicinspector [C\:z3d文件路径 est.z3d] -t 点
-m 复制

positional arguments:
  filePath              .z3d文件路径

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         显示版本信息
  -t [TOOL], --tool [TOOL]
                        查询工具类型：点、直线、圆、矩形、引伸计、多边形，默认矩形
  -m [MODE], --mode [MODE]
                        模式：增加、复制，阵列复制，默认复制
  -p POSITION [POSITION ...], --position POSITION [POSITION ...]
                        工具位于图像像素位置（x y）：默认1000 1000，即图像上水平位置1000垂直位置1000
  -s STEP [STEP ...], --step STEP [STEP ...]
                        复制工具的像素步长（x y）：默认0 0
  -n [NUMBER], --number [NUMBER]
                        复制工具个数：默认1
  -r [RADIUS], --radius [RADIUS]
                        圆形工具半径（像素），默认50
  -u [HEIGHT], --height [HEIGHT]
                        矩形工具高度（像素），默认50
  -w [WIDTH], --width [WIDTH]
                        矩形工具宽度（像素）,默认50
  --colormap            完美绘图

---结束---

```

# Updates

The Updates of the vicinspector are:

- Design a GUI to make using the script more easily.

- The script can be integrated with VIC software.







