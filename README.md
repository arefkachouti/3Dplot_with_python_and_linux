# 3Dplot_with_python_and_linux

the first plot_path.py is a python script that plots trajectories and combine it with bash using the "argparse"
to execute this code via the terminal we must write this :

$ python plot_path.py -d "data1.txt" -t "first data" -c "r" 
-d : data path like for exemple "data1.txt"
-t :title of the graph
-c :color of the line

Plot_all is the bash script that reads the python script and plot the files we select :
./ plot_all data1.txt data2.txt


