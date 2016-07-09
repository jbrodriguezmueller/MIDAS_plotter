#!/usr/bin/env python
# MIDAS_plotter : Auxiliary scripts for MIDAS 
# Copyright (C) 2016 Beltran Rodriguez-Mueller
# Freely distributed under the MIT License
import os, numpy, random, argparse
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt

def read_data_file(argsdict,infile,the_min=0.001,include_end=False):
  filename = argsdict['in'] + "/" + infile
  f = open(filename)
  out_array = {}
  line1 = f.readline()
  line = line1.strip().split("\t")
  if include_end:
    header_x = line
  else:
    header_x = line[:-1]
  all_data_2b = []
  max_seen = 0.0
  header_y = []
  for line in f:
    line = line.strip().split("\t")
    all_vals = line[1:]
    all_vals = map( float, all_vals )
    if include_end:
      pass
    else:
      all_vals = all_vals[:-1]

    if max(all_vals) >= the_min:
      all_data_2b.append(all_vals)
      max_seen = max( max_seen, max(all_vals ) )
      header_y.append(line[0])
  f.close()
  out_array['xlabels'] = header_x
  out_array['ylabels'] = header_y
  out_array['all_data'] = numpy.array(all_data_2b)
  out_array['max_seen'] = max_seen
  return out_array
  
def main_plot(argsdict):
  plot_coverage(argsdict)
  plot_count(argsdict)

def plot_count(argsdict):
  the_vals = read_data_file(argsdict, 'count_reads.txt',the_min=argsdict['min_count'])
  max_seen = the_vals['max_seen']
  all_data = the_vals['all_data']
  the_xlabels = the_vals['xlabels']
  the_ylabels = the_vals['ylabels']

  fig = plt.figure(figsize=(argsdict['figsize_x'], argsdict['figsize_y']) )
  ax = fig.add_subplot(111)
  plt.pcolor(all_data,cmap='Greys')

  the_xlabels = the_xlabels[1:]
  ax.set_xticks(numpy.arange(all_data.shape[1])+0.5, minor=False)
  ax.set_xticklabels(the_xlabels, minor=False, fontsize=argsdict['x_font_size'])

  ax.set_yticks(numpy.arange(all_data.shape[0])+0.5, minor=False)
  ax.set_yticklabels(the_ylabels, minor=False, fontsize=argsdict['y_font_size'])

  plt.title(argsdict['title']+' - Counts')
  fig.savefig(argsdict['out']+"/"+'summary_counts.png',dpi=argsdict['dpi'])
  plt.close(fig)
  
def plot_coverage(argsdict):
  the_vals = read_data_file(argsdict, 'coverage.txt',the_min=argsdict['min_coverage'])
  max_seen = the_vals['max_seen']
  all_data = the_vals['all_data']
  the_xlabels = the_vals['xlabels']
  the_ylabels = the_vals['ylabels']

  fig = plt.figure(figsize=(argsdict['figsize_x'], argsdict['figsize_y']) )
  ax = fig.add_subplot(111)
  plt.pcolor(all_data,cmap='Greys')

  the_xlabels = the_xlabels[1:]
  ax.set_xticks(numpy.arange(all_data.shape[1])+0.5, minor=False)
  ax.set_xticklabels(the_xlabels, minor=False, fontsize=argsdict['x_font_size'])

  ax.set_yticks(numpy.arange(all_data.shape[0])+0.5, minor=False)
  ax.set_yticklabels(the_ylabels, minor=False, fontsize=argsdict['y_font_size'])

  plt.title(argsdict['title']+' - Coverage')
  fig.savefig(argsdict['out']+"/"+'summary_coverage.png',dpi=argsdict['dpi'])
  plt.close(fig)

def main():
  parser = argparse.ArgumentParser(description='Makes pretty pictures from MIDAS results')
  parser.add_argument('--in',  help='Input directory', required=True)
  parser.add_argument('--out', help='Output directory', required=True)
  parser.add_argument('--title', help='Base title for figures', required=False, default='Base Title ')
  parser.add_argument('--dpi', type=int, help='DPI of PNG figures', required=False, default=150)
  parser.add_argument('--type', type=str, help='Type of result = {species | genes | snps | speciesgenes | all}', default='species' )
  parser.add_argument('--min_coverage', type=float,
                      help='A species has to have at least this coverage to be shown on the reduced coverage plot', default=0.001 )
  parser.add_argument('--min_count', type=int,
                      help='A species has to have at least this read count in at least one env to be shown on the reduced count plot', default=5 )
  parser.add_argument('--x_font_size', type=int, help='Font size for labels on x axis', required=False, default=8)
  parser.add_argument('--y_font_size', type=int, help='Font size for labels on y axis', required=False, default=7)
  parser.add_argument('--figsize_x', type=float, help='Figure size X', required=False, default=8)
  parser.add_argument('--figsize_y', type=float, help='Figure size Y', required=False, default=11)
  args = parser.parse_args()
  argsdict = vars(args)
  theDir = argsdict['in']
  outDir = argsdict['out']
  print "all done doing nothing!"
  main_plot(argsdict)

if __name__ == "__main__":
  main()
