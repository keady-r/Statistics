from struct import pack
from sys import displayhook
from matplotlib.font_manager import FontProperties 
import numpy as np 
import pandas as pd 
import seaborn as sns 
import matplotlib.pyplot as plt 

file = 'iris.data' 
titles = ['Sepal Length','Sepal Width','Petal Length','Petal Width','Species'] 
sns.set(style="whitegrid")

try:
    with open (file, "rt") as f: 
        data = pd.read_csv(file, header=None, names=titles)
except FileNotFoundError:
    print("file was not found - please ensure nameing convention is correct 'irisi.data'")

print(' ', file=open("irisSummary.txt", "a"))
print ('Iris Data Summary', file=open("Iris_Data_Summary.txt", "w"))
print(" ", file=open("irisSummary.txt", "a"))
print('-------------------------------', file=open("irisSummary.txt", "a"))
print('Number of Samples in the Study under each Species Type', file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print (data ['Species'].value_counts(), file=open("irisSummary.txt", "a"))
print(' ------------------------------', file=open("irisSummary.txt", "a"))
print('Summary of analysis - Count, Mean, Standard Deviation, min, max, and 25th/50th/75th percentiles.', file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print(data.describe(), file=open("irisSummary.txt", "a"))

print('------------------------------', file=open("irisSummary.txt", "a"))
print ('Data of Sepal Length , Sepal Width, Petal Length, and Petal Width - Grouped by Species', file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print (data .groupby('Species').corr(), file=open("irisSummary.txt", "a"))
print(' ------------------------------', file=open("irisSummary.txt", "a"))
print ('Summary of statistical analysis grouped by species',file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print('min', file=open("irisSummary.txt", "a"))
print(data.groupby('Species').min(), file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print('max', file=open("irisSummary.txt", "a"))
print(data.groupby('Species').max(), file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print('mean', file=open("irisSummary.txt", "a"))
print(data.groupby('Species').mean(), file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print('median', file=open("irisSummary.txt", "a"))
print(data.groupby('Species').median(), file=open("irisSummary.txt", "a"))
print(' ', file=open("irisSummary.txt", "a"))
print('std', file=open("irisSummary.txt", "a"))
print(data.groupby('Species').std(), file=open("irisSummary.txt", "a"))
print(' ------------------------------', file=open("irisSummary.txt", "a"))
        


    
report = input("Would you like to generate and save a histogram for the Iris data set? (y/n): ")

if report == 'y' or report =='Y':
    
    settings = sns.FacetGrid(data,hue = "Species", height=3)
    settings.map(sns.histplot,"Petal Length").add_legend()
    plt.savefig('Histogram:PetalLength.png', dpi = 750)
    
    settings.map(sns.histplot,"Petal Width").add_legend()
    plt.savefig('Histogram:PetalWidth.png', dpi = 750)
    
    settings.map(sns.histplot,"Sepal Length").add_legend()
    plt.savefig('Histogram:SepalLength.png', dpi = 750)
  
    settings.map(sns.histplot,"Sepal Width").add_legend()
    plt.savefig('Histogram:SepalWidth.png', dpi = 750)

elif report == 'n' or report == 'N':
    print("Ok, No was selected - Histogram was not generated") 

else:
    print("No Valid entry was inputted - Histogram was not generated") 
plt.show()

            
#File1
def saveFile(filename):
    plt.savefig(filename)
    plt.clf()  

  
sns.scatterplot(data = data, x= "Petal Length", y = "Petal Width", legend = True, hue = "Species" )
plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"]) 
filename = "Scatter Plot: Petal Length vs Petal Width.jpg"
saveFile(filename)

sns.scatterplot(data = data, x= "Sepal Length", y = "Sepal Width", legend = True, hue = "Species" )
plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])
filename = "Scatter Plot: Sepal Length vs Sepal Width.jpg"
saveFile(filename)

sns.scatterplot(data = data, x= "Petal Length", y = "Sepal Length", legend = True, hue = "Species" )
plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])         
filename = "Scatter Plot: Petal Length vs Sepal Length.jpg"
saveFile(filename)

sns.scatterplot(data = data, x= "Petal Width", y = "Sepal Width", legend = True, hue = "Species" )
plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])        
filename = "Scatter Plot: Petal Width vs Sepal Width.jpg"
saveFile(filename)

sns.scatterplot(data = data, x= "Petal Width", y = "Sepal Length", legend = True, hue = "Species" )
plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])          
filename = "Scatter Plot: Petal Width vs Sepal Length.jpg"
saveFile(filename)

sns.scatterplot(data = data, x= "Petal Length", y = "Sepal Width", legend = True, hue = "Species" )
plt.legend(labels=["Iris_Setosa", "Iris_Virginica", "Iris_Versicolor"])          
filename = "Scatter Plot: Petal Length vs Sepal Width.jpg"
saveFile(filename)



join_reps = input ("Would you like to generate and save jointplot reports? (y/n):")
# #Joint Reports
if join_reps == 'y' or join_reps =='Y':
    sns.jointplot(data=data, x = "Petal Length", y = "Sepal Length", kind= "reg", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Length vs Sepal length")
    filename = "Joint Plots: Petal Length vs Sepal length.jpg"
    plt.savefig(filename)

    sns.jointplot(data=data, x = "Petal Length", y = "Sepal Length", hue = "Species", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Length vs Sepal length")
    filename = "Joint Plots: Petal Length vs Sepal length.jpg"
    plt.savefig(filename)

    sns.jointplot(data=data, x = "Petal Width", y = "Sepal Width", kind= "reg", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Width vs Sepal Width")
    filename = "Joint Plots: Petal Width vs Sepal Width.jpg"
    plt.savefig(filename)

    sns.jointplot(data=data, x = "Petal Width", y = "Sepal Width", hue = "Species", height=7, ratio=2, marginal_ticks=True)
    plt.suptitle("Petal Width vs Sepal Width")
    
    filename = "Joint Plots: Petal Width vs Sepal Width.jpg"
    saveFile(filename)

elif join_reps == 'n' or join_reps == 'N':
    print("Ok, No was selected - additional graphs were generated")
else:
    print("No valid option was selected - additional graphs were generated")


line_rep = input ("Would you like to generate and save line reports? (y/n):")
if line_rep == 'y' or line_rep =='Y':
    sns.set_theme(style="darkgrid") 

    sns.lineplot(x="Petal Length", y="Petal Width",hue="Species",data=data) 
    plt.suptitle("Petal Length vs Sepal Width")
    filename = "Line Graphs: Petal Length vs Petal Width.jpg"
    saveFile(filename)

    sns.lineplot(x="Sepal Length", y="Sepal Width", hue="Species",data=data)
    plt.suptitle("Sepal Length vs Sepal Width")
    filename = "Line Graphs: Sepal Length vs Sepal Width.jpg"
    saveFile(filename)
    
    sns.lineplot(x="Petal Length", y="Sepal Length",hue="Species",data=data)
    plt.suptitle("Petal Length vs Sepal length")
    filename = "Line Graphs: Petal Length vs Sepal Length.jpg"
    saveFile(filename)  
    
    sns.lineplot(x="Petal Width", y="Sepal Width",hue="Species",data=data)
    plt.suptitle("Petal Width vs Sepal Width")
    filename = "Line Graphs: Petal Width vs Sepal Width.jpg"
    saveFile(filename)
    
elif line_rep == 'n' or line_rep == 'N':
    print("Ok, No was selected - additional graphs were generated")
else:
    print("No valid option was selected - additional graphs were generated")
