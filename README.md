# Augmented Reality with OpenCV 
Augmented reality card based application with Python, numpy, OpenCV and Gooey 

## **Usage** 

<!-- * Place the image of the surface to be tracked inside the `reference` folder.
* On line 36 of `src/ar_main.py` replace `'model.jpg'` with the name of the image you just copied inside the `reference` folder.
* On line 40 of `src/ar_main.py` replace `'fox.obj'` with the name of the model you want to render. To change the size of the rendered model change the scale parameter (number `3`) in line 103 of `src/ar_main.py` by a suitable number. This might require some trial and error.
* Open a terminal session inside the project folder and run `python src/ar_main.py` -->
### **Install dependencies** 
``` 
    pip3 install -r requirements.txt
``` 

### **How to run the program** 
``` 
    python src/ar_main.py
```
Due to the usage of Gooey Parser we can't pass arguments directly to the CLI but if you want to do that then must replace ``custom_args()`` in ``ar_main.py``  with ``default_args()``. 


### **Build executable** 
Performance issue and large file when generate executable files with PyInstaller (~300MB) we would rather you compile the program for better experience. 

### **Command line arguments** 
* `--rectangle`, `-r`: Draws the projection of the reference surface on the video frame as a green rectangle.
* `--matches`, `-m`: Draws matches between reference surface and video frame.
* `--number_matches`, `-nm`: Set number of minimum matches to consider recognition valid. 
* `--object`, `-obj`: Choose model to draw on surface.
* `--surface`, `-s`: Choose surface which model will be drawn on.

## Troubleshooting

**If you get the message**:

```
Unable to capture video
```
Check if your camera working correctly and simply restart the program.  

<!-- printed to your terminal, the most likely cause is that your OpenCV installation has been compiled without FFMPEG support. Pre-built OpenCV packages such as the ones downloaded via pip are not compiled with FFMPEG support, which means that you have to build it manually.

**If you get the error**:

```
Traceback (most recent call last):
File "src/ar_main.py", line 174, in
main()
File "src/ar_main.py", line 40, in main
obj = OBJ(os.path.join(dir_name, 'models/fox.obj'), swapyz=True)
File "[...]/augmented-reality/src/objloader_simple.py", line 16, in init
v = v[0], v[2], v[1]
TypeError: 'map' object is not subscriptable
```
The most likely cause is that you are trying to execute the code with Python 3 and the code is written in Python 2. The `map` function in Python 3 returns an iterable object of type map, and not a subscriptible list. To fix it, change the calls to `map()` by `list(map())` on lines 14, 19 and 24 of `src/objloader_simple.py`. 

## Explanation

See this blog entries for an in-depth explanation of the logic behind the code:

* [Part 1](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/)
* [Part 2](https://bitesofcode.wordpress.com/2018/09/16/augmented-reality-with-python-and-opencv-part-2/)

## Results

* [Mix](https://www.youtube.com/watch?v=YVJSFcUbIoU)
* [Fox](https://www.youtube.com/watch?v=V13VE6UJ-1g)
* [Ship](https://www.youtube.com/watch?v=VDwfW75f3Xo)
* [Rat](https://www.youtube.com/watch?v=Bb7pYthMM64)
* [Cow](https://www.youtube.com/watch?v=f0fNzXP3ku8)
* [Fox II](https://www.youtube.com/watch?v=_fozNTdql6U)
* [Fox III](https://www.youtube.com/watch?v=FGKkIr_IIy4) 
