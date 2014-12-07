#
# Build a PDF with all the notebooks 
#
TEMPLATE=chapter
NOTEBOOK_DIR=../notebooks/
NOTEBOOKS=0-Introduction.ipynb Syllabus.ipynb\
          I-Python.ipynb I.II-Iterables.ipynb\
          II-IPython.ipynb III-Numpy.ipynb IV-SciPy.ipynb\
          V-Matplotlib.ipynb VI-Pandas.ipynb\
	  VII-Tips-and-Tricks.ipynb VIII-Benchmarks.ipynb\
	  IX-Randomness.ipynb X-FFT.ipynb

LATEXFILES=$(NOTEBOOKS:.ipynb=.tex)

.ipynb.tex:
	ipython nbconvert --to latex --template $(TEMPLATE) $<

#all: $(LATEXFILES) buildpdf
all: latexfiles buildpdf

latexfiles:
	ipython nbconvert --to latex --template $(TEMPLATE) $(NOTEBOOK_DIR)0-Introduction.ipynb $(NOTEBOOK_DIR)Syllabus.ipynb
	ipython nbconvert --to latex --template $(TEMPLATE) $(NOTEBOOK_DIR)I-Python.ipynb $(NOTEBOOK_DIR)I.II-Iterables.ipynb
	ipython nbconvert --to latex --template $(TEMPLATE) $(NOTEBOOK_DIR)II-IPython.ipynb $(NOTEBOOK_DIR)III-Numpy.ipynb $(NOTEBOOK_DIR)IV-SciPy.ipynb
	ipython nbconvert --to latex --template $(TEMPLATE) $(NOTEBOOK_DIR)V-Matplotlib.ipynb $(NOTEBOOK_DIR)VI-Pandas.ipynb
	ipython nbconvert --to latex --template $(TEMPLATE) $(NOTEBOOK_DIR)VII-Tips-and-Tricks.ipynb $(NOTEBOOK_DIR)VIII-Benchmarks.ipynb
	ipython nbconvert --to latex --template $(TEMPLATE) $(NOTEBOOK_DIR)IX-Randomness.ipynb $(NOTEBOOK_DIR)X-FFT.ipynb

buildpdf: latexfiles
	pdflatex PFF-Introduction-ISEG2014.tex
    
