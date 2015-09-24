Find the total area covered by two rectilinear rectangles in a 2D plane.

### 题意
求两个矩形覆盖的面积

### 题解
如果两个矩形不相交，那么是他们的面积和
不相交的判断条件为 (A > G) or (B >H) or (C < E) or (D < F)

在保证相交的情况下，相交面积是 两个较小x,y坐标的大者和，大x,y坐标的小者