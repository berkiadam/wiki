

```
$sudo dnf install \
    texlive-collection-basic \
    texlive-collection-latex \
    texlive-collection-latexrecommended \
    texlive-collection-latexextra \
    dvipng

$ sudo dnf install \
    python3-devel \
    pango pango-devel \
    cairo cairo-devel \
    pkgconf-pkg-config \
    ffmpeg

$ pip install manim

$ manim -h

$ manim -p -ql gradient_descent.py GradientDescentUpdate
```

Machine Learning example 1
```
$ manim -p -ql ml_flat_example1.py ML_Flat_Example1
```

Az utolsó paraméter a fájlban lévő osztály neve:
```py
class ML_Flat_Example1(Scene):

```