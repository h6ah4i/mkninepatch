mkninepatch
===

Simple command line tool which generates Android's 9-patch resource.

### Installation

1. Install [Wand](http://docs.wand-py.org/en/0.4.0/) Python module

    ```bash
    pip install Wand
    ```

2. Clone this repository
    ```bash
    git@github.com:h6ah4i/mkninepatch.git
    ```

3. Add the mkninepatch directory in your `$PATH`
    ```
    export PATH=$PATH:[path of the cloned mkninepatch directory]
    ```

### Usage

```
# input : W: 90px, H: 70 px
# output: W: 92px, H: 72 px

# LEFT  : 10 px (from: 10, to: 19)
# TOP   : 20 px (from: 20, to: 39)
# RIGHT : 30 px (from: 30, to: 59)
# BOTTOM: 40 px (from: 40, to: 79)

$ mkninepatch input.png output.9.png -l1 10 19 -t1 20 39 -r 30 59 -b 40 79
```

| Input PNG file (input.png) | Result PNG file (output.9.png) |
|----------------------------------------------|----------------------------------------------|
| <a href="./pic/input.png?raw=true"><img src="./pic/input.png?raw=true" alt="Input PNG file (input.png)" width="90" height="72" /></a> | <a href="./pic/output.9.png?raw=true"><img src="./pic/output.9.png?raw=true" alt="Result PNG file (output.9.png)" width="92" height="72" /></a> |




### Command line options

| Option          | Description                          |
|-----------------|--------------------------------------|
| `-h`            | Show help                            |
| `-l1 start end` | Specify range of the LEFT marker (1) |
| `-l2 start end` | Specify range of the LEFT marker (2) |
| `-l3 start end` | Specify range of the LEFT marker (3) |
| `-l4 start end` | Specify range of the LEFT marker (4) |
| `-t1 start end` | Specify range of the TOP marker (1)  |
| `-t2 start end` | Specify range of the TOP marker (2)  |
| `-t3 start end` | Specify range of the TOP marker (3)  |
| `-t4 start end` | Specify range of the TOP marker (4)  |
| `-r  start end` | Specify range of the RIGHT marker    |
| `-b  start end` | Specify range of the BOTTOM marker   |
