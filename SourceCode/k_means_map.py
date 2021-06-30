#!/usr/bin/env python3
import sys

#-----------Khoi tao tam cum-------------
centroids=[]
#0
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,51,159,253,159,50,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48,238,252,252,252,237,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,54,227,253,252,239,233,252,57,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,60,224,252,253,252,202,
84,252,253,122,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,163,252,252,252,253,252,252,96,189,253,167,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,51,238,253,253,190,114,253,228,47,79,255,168,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,48,238,252,252,179,12,75,121,21,0,0,253,243,50,0,0,0,0,0,0,0,0,0,0,0,0,0,38,165,253,233,208,84,0,
0,0,0,0,0,253,252,165,0,0,0,0,0,0,0,0,0,0,0,0,7,178,252,240,71,19,28,0,0,0,0,0,0,253,252,195,0,0,0,
0,0,0,0,0,0,0,0,0,57,252,252,63,0,0,0,0,0,0,0,0,0,253,252,195,0,0,0,0,0,0,0,0,0,0,0,0,198,253,190,
0,0,0,0,0,0,0,0,0,0,255,253,196,0,0,0,0,0,0,0,0,0,0,0,76,246,252,112,0,0,0,0,0,0,0,0,0,0,253,252,
148,0,0,0,0,0,0,0,0,0,0,0,85,252,230,25,0,0,0,0,0,0,0,0,7,135,253,186,12,0,0,0,0,0,0,0,0,0,0,0,85,
252,223,0,0,0,0,0,0,0,0,7,131,252,225,71,0,0,0,0,0,0,0,0,0,0,0,0,85,252,145,0,0,0,0,0,0,0,48,165,
252,173,0,0,0,0,0,0,0,0,0,0,0,0,0,0,86,253,225,0,0,0,0,0,0,114,238,253,162,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,85,252,249,146,48,29,85,178,225,253,223,167,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,85,252,252,
252,229,215,252,252,252,196,130,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,28,199,252,252,253,252,252,233,
145,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,128,252,253,252,141,37,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#1
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,124,253,255,63,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,96,
244,251,253,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,127,251,251,253,62,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,68,236,251,211,31,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,60,228,251,
251,94,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,155,253,253,189,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,20,253,251,235,66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,205,253,251,126,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,104,251,253,184,15,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,80,240,251,193,23,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,32,253,253,253,159,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,151,251,251,251,39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
48,221,251,251,172,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,234,251,251,196,12,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,251,251,89,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,159,255,
253,253,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,48,228,253,247,140,8,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,64,251,253,220,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,251,253,
220,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,193,253,220,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#2
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,25,100,122,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,33,151,
208,252,252,252,146,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,152,244,252,253,224,211,252,232,40,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,15,152,239,252,252,252,216,31,37,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,96,252,252,252,252,217,29,0,37,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,181,252,252,220,
167,30,0,0,77,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,128,58,22,0,0,0,0,100,252,252,60,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,157,252,252,60,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,110,121,122,121,202,252,194,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,53,179,253,253,255,253,253,
228,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,54,227,252,243,228,170,242,252,252,231,117,6,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,6,78,252,252,125,59,0,18,208,252,252,252,252,87,7,0,0,0,0,0,0,0,0,0,0,0,0,5,135,
252,252,180,16,0,21,203,253,247,129,173,252,252,184,66,49,49,0,0,0,0,0,0,0,0,3,136,252,241,106,17,
0,53,200,252,216,65,0,14,72,163,241,252,252,223,0,0,0,0,0,0,0,0,105,252,242,88,18,73,170,244,252,
126,29,0,0,0,0,0,89,180,180,37,0,0,0,0,0,0,0,0,231,252,245,205,216,252,252,252,124,3,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,207,252,252,252,252,178,116,36,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,
93,143,121,23,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
#3
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,42,118,219,166,118,118,6,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,103,242,254,254,254,254,254,66,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,18,232,254,254,254,254,254,238,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,104,244,254,224,
254,254,254,141,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,207,254,210,254,254,254,34,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,84,206,254,254,254,254,41,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
24,209,254,254,254,171,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,91,137,253,254,254,254,112,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,40,214,250,254,254,254,254,254,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,81,247,254,254,254,254,254,254,146,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,110,246,254,254,
254,254,254,171,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,73,89,89,93,240,254,171,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,128,254,219,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,254,
254,214,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,138,254,254,116,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,19,177,90,0,0,0,0,0,25,240,254,254,34,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,164,254,215,63,36,0,51,89,
206,254,254,139,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,57,197,254,254,222,180,241,254,254,253,213,11,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,140,105,254,254,254,254,254,254,236,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,7,117,117,165,254,254,239,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#4
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,189,190,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,143,247,153,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,136,247,242,86,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,192,252,187,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,62,185,18,0,0,0,0,89,236,217,47,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,216,253,60,
0,0,0,0,212,255,81,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,206,252,68,0,0,0,48,242,253,89,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,131,251,212,21,0,0,11,167,252,197,5,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,29,232,
247,63,0,0,0,153,252,226,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,219,252,143,0,0,0,116,249,252,103,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,4,96,253,255,253,200,122,7,25,201,250,158,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,92,252,252,253,217,252,252,200,227,252,231,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,87,251,247,231,65,
48,189,252,252,253,252,251,227,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,190,221,98,0,0,0,42,196,252,253,252,
252,162,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,111,29,0,0,0,0,62,239,252,86,42,42,14,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,15,148,253,218,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,121,252,231,28,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,221,251,129,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,218,252,160,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,122,252,82,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#5
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,3,18,18,18,126,136,175,26,166,255,247,127,0,0,0,0,0,0,0,0,0,0,0,0,30,36,
94,154,170,253,253,253,253,253,225,172,253,242,195,64,0,0,0,0,0,0,0,0,0,0,0,49,238,253,253,253,253,
253,253,253,253,251,93,82,82,56,39,0,0,0,0,0,0,0,0,0,0,0,0,18,219,253,253,253,253,253,198,182,247,
241,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,80,156,107,253,253,205,11,0,43,154,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,14,1,154,253,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,139,253,190,2,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,190,253,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,35,241,225,160,108,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,81,240,253,253,119,25,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,186,253,253,150,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,16,93,252,253,187,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,249,253,249,
64,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,46,130,183,253,253,207,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,39,148,229,253,253,253,250,182,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,114,221,253,253,
253,253,201,78,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,23,66,213,253,253,253,253,198,81,2,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,18,171,219,253,253,253,253,195,80,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,172,226,
253,253,253,253,244,133,11,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,136,253,253,253,212,135,132,16,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#6
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,34,169,250,40,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,58,242,221,143,17,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,75,247,143,10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,37,245,184,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,192,200,14,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,139,247,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,231,183,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,125,243,50,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,195,184,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,61,251,41,0,0,0,64,43,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,152,210,7,0,96,237,254,247,107,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,250,84,0,6,223,84,13,87,246,72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,43,254,80,0,56,151,0,0,0,147,
193,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,254,41,0,13,19,0,0,0,42,253,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,67,254,13,0,0,0,0,0,0,14,253,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,68,255,13,0,0,0,0,0,0,77,240,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,254,13,0,0,0,0,0,5,181,147,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,25,229,105,0,0,0,0,5,156,213,20,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,107,246,105,14,49,95,217,
209,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,107,246,253,253,240,130,6,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#7
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,115,121,162,253,253,213,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,63,107,170,251,252,252,252,252,250,214,0,0,0,0,0,0,0,0,0,0,0,0,0,0,25,192,226,226,241,
252,253,202,252,252,252,252,252,225,0,0,0,0,0,0,0,0,0,0,0,0,0,68,223,252,252,252,252,252,39,19,39,
65,224,252,252,183,0,0,0,0,0,0,0,0,0,0,0,0,0,186,252,252,252,245,108,53,0,0,0,150,252,252,220,20,0,
0,0,0,0,0,0,0,0,0,0,0,70,242,252,252,222,59,0,0,0,0,0,178,252,252,141,0,0,0,0,0,0,0,0,0,0,0,0,0,
185,252,252,194,67,0,0,0,0,17,90,240,252,194,67,0,0,0,0,0,0,0,0,0,0,0,0,0,83,205,190,24,0,0,0,0,
0,121,252,252,209,24,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,77,247,252,248,106,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,253,252,252,102,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
134,255,253,253,39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,183,253,252,107,2,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,10,102,252,253,163,16,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,13,
168,252,252,110,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,252,252,217,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,40,155,252,214,31,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,165,252,
252,106,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,43,179,252,150,39,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,137,252,221,39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,252,79,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#8
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,203,229,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,
47,47,30,95,254,215,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,154,185,185,223,253,253,133,175,255,188,
19,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,110,253,253,253,246,161,228,253,253,254,92,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,128,245,253,158,137,21,0,48,233,253,233,8,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,139,254,223,
25,0,0,36,170,254,244,106,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,55,212,253,161,11,26,178,253,236,113,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,7,155,253,228,80,223,253,253,109,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,141,253,253,253,254,253,154,29,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,110,253,253,
253,254,179,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,3,171,254,254,254,179,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,171,253,253,253,253,178,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,26,123,
254,253,203,156,253,200,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,93,253,254,121,13,93,253,158,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,64,239,253,76,8,32,219,253,126,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,133,254,191,0,5,108,234,254,106,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,132,253,190,5,85,
253,236,154,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,153,253,169,192,253,253,77,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,112,253,253,254,236,129,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,17,
118,243,191,113,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0])

#9
centroids.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,18,105,227,253,253,122,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,57,199,253,252,252,252,252,159,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,20,211,252,232,152,
73,167,252,215,6,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,197,252,182,0,0,0,37,235,243,47,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,188,252,103,0,0,0,37,235,229,27,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,189,
253,86,8,43,139,190,211,45,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,232,252,200,201,252,252,84,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,213,245,252,253,252,242,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,56,84,253,252,160,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,45,253,252,38,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,89,255,253,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,80,253,189,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,179,232,84,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,15,225,252,115,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,153,252,
164,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,68,245,243,79,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,32,237,245,82,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,9,148,252,169,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,106,253,196,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
54,228,129,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0])
#-------Ket thuc viec khoi tao tam cum--------
#tinh toan khoang cach giua cac anh
def calculate_distance(centroid, image):
    distance=0.0
    for i in range(784):
        distance+=pow(centroid[i]-image[i],2)
    return pow(distance,0.5)
#qua trinh map
def map():
    global centroids
    for line in sys.stdin:
        line=line.rstrip('\n')
        values=line.split(',')
        img=[]
        for value in values:
            img.append(float(value))
        min_distance=1000000000
        key=-1
        for i in range(10):
            distance=calculate_distance(centroids[i],img)
            if distance<min_distance:
                key=i
                min_distance=distance
        output=str(key)
        output+=f',{line},1'
        print(output)

map()