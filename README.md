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

 # References
My project is based on https://github.com/juangallostra/augmented-reality 

:) really appreciate & special thanks to the original author
