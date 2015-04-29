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
usage: mkninepatch.py [-h] [-l1 LEFT1 LEFT1] [-l2 LEFT2 LEFT2]
                      [-l3 LEFT3 LEFT3] [-l4 LEFT4 LEFT4] [-t1 TOP1 TOP1]
                      [-t2 TOP2 TOP2] [-t3 TOP3 TOP3] [-t4 TOP4 TOP4]
                      [-r RIGHT RIGHT] [-b BOTTOM BOTTOM]
                      input_png output_png

$ mkninepatch input.png output.9.png -l1 10 20 -t 20 40 -r 30 60 -b 40 80
```


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
