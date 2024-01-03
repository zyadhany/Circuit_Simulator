# &%#?! Python (المشطشطين)

This project is seprated into 3 parts.

-   Curcit simmulation
    -   response for simmulate curcuit and get it's results.

-   Cuicit Detector
    -   Ai module that detect circuit from image or video and give you it's netlist.

-   Gui Applcation
    - The use interface that user deal with.


##  What we need in this project?
-   C (memory managment)
-   Python (Opp & moduoles)
-   Sheard Libraries (DLL files)
-   multiable process
-   Algorithms like: DFS - Prefix
-   Circuit mathmatic soluation
-   Command line interface
-   Gui with python
-   Machine learning
-   train dataset for opject detection
-   image procecing
---
## Curcit simmulation

that the programe response to simulate circuit and gives you it's results.

at beging we got 2 options to work with.
-   use pyspise
-   start from scratch

but duo to time we have and we also need to learn how to use python and work with modules we decided to go on with pyspise but we had problems working with it and it didn't work good with us.

it's very good library but anviroment didn't fit with us giving us errors, it worked with anaconda enviroment but we didn't like this way.

so we decided to look at other opthins we have and found library called ahkab, it isn't the best but we liked the it is as it's very simple and we can understand it's src code while editing it.

the problem that it's not full or not complated yet, miss alot of opthins and some if it's function don't work that well also it's made like at 2005 and last upadete was 2016 so most of it's dependanse needs to be updated, but we liked it and decided to go on with it.

we started to work with it's function and files one by one(those we wants to work with), fix them and edit what we don't like.

you can check other documntion to find the last functions we stand for and how to use it.

---
## Circit Detector

It's a Ai module that take a image or video analaysing it into netlist.

### How it work?

it we have hand darwn image in paper we can think it as black/white pixels.

black stand for circuit, white is paper and we don't need it.

in that was we can swich our image or frame from video into gray image that have only 2 values 0/255 Black&white.

-   255 = True (drawn circuit)
-   0   = False (just the Background)

``` image with Break ```

now we got our image in good shape, now we want to detect it's components and node.

now we run opject detection module and get components one by one, like that:

```image of component detection```

after that to get our nodes, we remove components from image and using dfs we can now which pixele are in same point and which is different.

```image of skel```

then we connect our nodes to components and for each component we need to find out which node it belong to

---
## Gui Applaction

we have couble of opthions (pygame/pyslide/tkinter) and we decided to make it with tkinter.

it's not best opthion but the felt more comfortable to work with it.

our Gui has 2 main functinalty
1.  Work as gui simmulation by draging and build components then run it.
2.  Acess to Circuit detector and pass image or open video with it.

---
