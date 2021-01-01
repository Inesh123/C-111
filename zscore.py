import csv
import random 
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import pandas as pd
df = pd.read_csv('School2.csv')
data = df['Math_score'].tolist()
mean = statistics.mean(data)
std_deviation = statistics.stdev(data)
def randomsetofmean(counter):
    dataset = []
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
mean_list = []
for i in range(0,1000):
    setofmeans=randomsetofmean(100)
    mean_list.append(setofmeans)
standard_deviation = statistics.stdev(mean_list)
firststdstart,firststdend = mean - standard_deviation,mean + standard_deviation 
secondstdstart,secondstdend = mean - (2*standard_deviation),mean + (2*standard_deviation)
thirdstdstart,thirdstdend = mean - (3*standard_deviation),mean + (3*standard_deviation)
# fig = ff.create_distplot([mean_list],['student marks'],show_hist = False)
# fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name = 'mean'))
# fig.add_trace(go.Scatter(x = [firststdstart,firststdstart],y = [0,0.17],mode = 'lines',name = 'firststdstart'))
# fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.17],mode = 'lines',name = 'firststdend'))
# fig.add_trace(go.Scatter(x = [secondstdstart,secondstdstart],y = [0,0.17],mode = 'lines',name = 'secondstdstart'))
# fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.17],mode = 'lines',name = 'secondstdend'))
# fig.add_trace(go.Scatter(x = [thirdstdstart,thirdstdstart],y = [0,0.17],mode = 'lines',name = 'thirdstdstart'))
# fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.17],mode = 'lines',name = 'thirdstdend'))
# fig.show()
# df = pd.read_csv('data1.csv')
# data = df['Math_score'].tolist()
# mean_of_sample1 = statistics.mean(data)
# print('mean of sample 1',mean_of_sample1)
# fig = ff.create_distplot([mean_list],['student marks'],show_hist = False)
# fig.add_trace(go.Scatter(x = [mean_of_sample1,mean_of_sample1],y=[0,0.17],mode = 'lines',name ='mean of sample1'))
# fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name = 'mean'))
# fig.add_trace(go.Scatter(x = [firststdstart,firststdstart],y = [0,0.17],mode = 'lines',name = 'firststdstart'))
# fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.17],mode = 'lines',name = 'firststdend'))
# fig.add_trace(go.Scatter(x = [secondstdstart,secondstdstart],y = [0,0.17],mode = 'lines',name = 'secondstdstart'))
# fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.17],mode = 'lines',name = 'secondstdend'))
# fig.add_trace(go.Scatter(x = [thirdstdstart,thirdstdstart],y = [0,0.17],mode = 'lines',name = 'thirdstdstart'))
# fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.17],mode = 'lines',name = 'thirdstdend'))
# fig.show()
# df = pd.read_csv('data2.csv')
# data = df['Math_score'].tolist()
# mean_of_sample2 = statistics.mean(data)
# print('mean of sample 2',mean_of_sample2)
# fig = ff.create_distplot([mean_list],['student marks'],show_hist = False)
# fig.add_trace(go.Scatter(x = [mean_of_sample2,mean_of_sample2],y=[0,0.17],mode = 'lines',name ='mean of sample2'))
# fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name = 'mean'))
# fig.add_trace(go.Scatter(x = [firststdstart,firststdstart],y = [0,0.17],mode = 'lines',name = 'firststdstart'))
# fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.17],mode = 'lines',name = 'firststdend'))
# fig.add_trace(go.Scatter(x = [secondstdstart,secondstdstart],y = [0,0.17],mode = 'lines',name = 'secondstdstart'))
# fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.17],mode = 'lines',name = 'secondstdend'))
# fig.add_trace(go.Scatter(x = [thirdstdstart,thirdstdstart],y = [0,0.17],mode = 'lines',name = 'thirdstdstart'))
# fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.17],mode = 'lines',name = 'thirdstdend'))
# fig.show()
df = pd.read_csv('School_3_Sample.csv')
data = df['Math_score'].tolist()
mean_of_sample3 = statistics.mean(data)
print('mean of sample 3',mean_of_sample3)
fig = ff.create_distplot([mean_list],['student marks'],show_hist = False)
fig.add_trace(go.Scatter(x = [mean_of_sample3,mean_of_sample3],y=[0,0.17],mode = 'lines',name ='mean of sample3'))
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = 'lines',name = 'mean'))
fig.add_trace(go.Scatter(x = [firststdstart,firststdstart],y = [0,0.17],mode = 'lines',name = 'firststdstart'))
fig.add_trace(go.Scatter(x = [firststdend,firststdend],y = [0,0.17],mode = 'lines',name = 'firststdend'))
fig.add_trace(go.Scatter(x = [secondstdstart,secondstdstart],y = [0,0.17],mode = 'lines',name = 'secondstdstart'))
fig.add_trace(go.Scatter(x = [secondstdend,secondstdend],y = [0,0.17],mode = 'lines',name = 'secondstdend'))
fig.add_trace(go.Scatter(x = [thirdstdstart,thirdstdstart],y = [0,0.17],mode = 'lines',name = 'thirdstdstart'))
fig.add_trace(go.Scatter(x = [thirdstdend,thirdstdend],y = [0,0.17],mode = 'lines',name = 'thirdstdend'))
fig.show()
zscore = (mean_of_sample3 - mean)/standard_deviation
print('zscore is: ',zscore)