#
# <p align="center">Flood fill</p>

An image is represented by an m x n char grid image where image[i][j] represents the first letter of collor name on the image.

You are also given two integers (coordinates of the starting point, f.e. sr, sc), and char - color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.

Here is an example of repainting image from gray ('G') into black ('B') color starting from point image[1][7]:

<p align="center">
<img width="308" src="https://user-images.githubusercontent.com/92269527/207987517-79a9457e-875a-42c0-b5a1-3794a7451b5f.png"> 
<img width="300" src="https://user-images.githubusercontent.com/92269527/207987628-207150dd-cfd1-48dc-ac2e-d9ad605e60f2.png">
</p>

#
# <p align="center">Career</p>

You want to make a career in big corporation, which has got a complicated hierarchical structure and many positions. However, after checking testimonials on GlassDoor you found out, that different positions in this corporation provide different amount of useful experience, so you should carefully pick the positions you want to work in.

Structure of positions in this company looks like a pyramide, where heigher level has one more position than the lower one. Experience you can gain on each position and abibilty to move between positions is displayed below:
<p align="center">
<img src="https://user-images.githubusercontent.com/92269527/207985462-d3c7be3c-8003-4d74-b8da-e184116c9a18.png">
</p>

