# MIDAS_plotter
MIDAS auxiliary scripts

1) get MIDAS and install it:

see https://github.com/snayfach/MIDAS

2) get MIDAS_plotter 

```git clone https://github.com/jbrodriguezmueller/MIDAS_plotter```

Install it

```
cd MIDAS_plotter
chmod 755 midas_plotter.py
cp midas_plotter.py /path/to/MIDAS/scripts
```
That will ensure it's
2) get the tutorial running. once your tutorial is running and you have the two species done, find the output of `merge_species.py`

let's assume that the output goes into a directory called "merged_species" :
then running these commands:
```
mkdir plots
midas_plotter.py --in merged_species/ --out plots --min_coverage=0.05 --dpi=300
```
Will give you a couple of nice coverage and read count plots.
