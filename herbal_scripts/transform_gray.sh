#!/bin/bash

echo "Step 1: convert all odts in this folder to pdf"

unoconv -f pdf *.odt

echo "Step 2: convert all pdfs in this folder to ps"

for i in *.pdf;
do pdftops $i;
rm $i;
done

echo "Step 3: scale all ps in this folder from A4 to A5"

for i in *.ps;
do psresize -PA4 -pA5 $i "scaled_"$i;
done

echo "Step 4: convert all scaled ps back to pdf"

for i in "scaled_"*.ps;
do ps2pdf -sPAPERSIZE=a5 $i;
done

echo "Step 5: remove all ps"

for i in *.ps;
do rm $i;
done

echo "Step 6: put all scaled pdfs together in brief.pdf, gedicht.pdf and verhaal.pdf"

mkdir -p love;
pdftk *.pdf cat output love/love.pdf;
pdftk scaled_brief_*.pdf cat output love/brief.pdf;
pdftk scaled_verhaal_*.pdf cat output love/verhaal.pdf;
pdftk scaled_gedicht_*.pdf cat output love/gedicht.pdf;

echo "Step 7: convert brief.pdf, gedicht.pdf and verhaal.pdf to grayscale + PDF1.3"

for i in *.pdf;
do gs -sOutputFile=love/$1 -sDEVICE=pdfwrite -sColorConversionStrategy=Gray -dProcessColorModel=/DeviceGray -dCompatibilityLevel=1.3 -dNOPAUSE -dBATCH love/"grey_"$1 < /dev/null;
done

echo "Step 8: remove all scaled pdfs"

for i in "scaled_"*.pdf;
do rm $i;
done