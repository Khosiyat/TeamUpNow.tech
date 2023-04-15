import matplotlib.pyplot as plt
import plotly.express as px
import base64
from io import BytesIO

import numpy as np
import pandas as pd



def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, dpi='figure', format=None, metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto',
        backend=None
       )
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,3))
    plt.title('score rating of')
    plt.plot(x,y, color='#18A558',  edgecolor='#f1f1f1')
    plt.xticks(rotation=45, color='#18A558')
    plt.xlabel('Follow_recruiter_1', color='#18A558')
    plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph



def get_bar(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,3))
    plt.title('score rating of')
    plt.bar(x,y, color='#18A558',  edgecolor='#f1f1f1')
    plt.xticks(rotation=0, color='#18A558')
    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph



def get_scatter(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(7,3))
    plt.title('score rating of')
    plt.scatter(x,y, color='#18A558',  edgecolor='#f1f1f1')
    plt.xticks(rotation=45, color='#18A558')
    plt.xlabel('Follow_recruiter_1', color='#18A558')
    plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph



def get_scatter_yearTechStack(x,y):
    N = 50
    area = sum([y])**2
    colors = ['#18A558', '#FFA500', '#E9967A', '#FFFF00', '#DC143C', '#9370DB', '#FF6347']

    plt.switch_backend('AGG')
    fig= plt.figure(figsize=(7,3))
    fig.set_figwidth(7)
    fig.set_figheight(5)

    plt.title('Worked year of Tech Stacks')
    plt.scatter(x,y,  edgecolor='#f1f1f1', s=area, c=colors, alpha=0.5)
    plt.xticks(rotation=45, color='#18A558')
    plt.xlabel('Tech Stack', color='#18A558')
    plt.ylabel('worked year', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph





def get_bar_chart_profile(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('Profile Rating | Evaluator', color='#008a3e', fontweight='book')
    plt.bar(x,y, color='#18A558',  edgecolor='#f1f1f1')
    
    plt.xticks(rotation=90, color='#18A558')

    # plt.set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi, 5 * np.pi])
    # plt.set_xticklabels(['0', r'$\pi$', r'2$\pi$', r'3$\pi$', r'4$\pi$', r'5$\pi$'])

    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)

    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph


def get_bar_chart_profileDashboard_interaction(x,y):

    colors = ['#F58518', '#4C78A8']
    labels = ['TeemingUp', 'TeemedUp']

    plt.switch_backend('AGG')
    # plt.figure(figsize=(0.2,0.1))
    plt.title('INTERACTION', color='#008a3e', fontweight='book')
    plt.bar(labels,y, width=0.2,  edgecolor=colors, fill=False, linewidth=5)
    
    plt.xticks(color='#18A558')

    plt.rc('font', size=9.4)
        
    fig, ax = plt.subplots(figsize=(1.7,1.6))
    rects1 = ax.bar(labels,y, width=0.07, edgecolor=colors, fill=False, linewidth=5)

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
    plt.grid(False)
    # plt.axis('off')

    ax = plt.gca() 
    ax.get_yaxis().set_visible(False) 
    ax.legend()
    ax.bar_label(rects1, padding=3) 
    plt.tight_layout() 
    graph=get_graph()
    return graph



def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format
    
def get_pie_profileDashboard_projects(x_data,y_label):

    # plt.xkcd() 


    # colors = ['#ff4040','#ffa500','#18A558']
    colors = ['#4C78A8', '#F58518']
    

    plt.switch_backend('AGG')
    # fig =plt.figure(figsize=(2,2),dpi=100)

    # plt.title('score rating of')
    # plt.pie(x,y, color='#18A558',  edgecolor='#f1f1f1')
    plt.subplots(figsize=(2, 1.6), subplot_kw=dict(aspect="equal"))
    
    plt.pie(x_data, 
            colors=colors,  
            labels=y_label, 
            shadow=True, 
            wedgeprops=dict(width=0.1), 
            startangle=-40,
            # autopct='%1.1f%%',
            autopct = autopct_format(x_data)
            )

    plt.xticks(rotation=45, color='#18A558')
    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph



def get_pie(x_data,y_label):
    # plt.xkcd() 
    colors = ['#ff4040','#ffa500','#18A558']
    

    plt.switch_backend('AGG')
    plt.figure(figsize=(7,3))
    # plt.title('score rating of')
    # plt.pie(x,y, color='#18A558',  edgecolor='#f1f1f1')
    plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
    
    plt.pie(x_data, 
            colors=colors,  
            labels=y_label, 
            shadow=True, 
            wedgeprops=dict(width=0.1), 
            startangle=-40,
            # autopct='%1.1f%%',
            autopct = autopct_format(x_data)
            )
            

    plt.xticks(rotation=45, color='#18A558')
    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    graph=get_graph()
    return graph



# import plotly.figure_factory as ff
# from plotly.offline import plot
# import plotly.express as px

# def get_gantChart(df):

#     plt.switch_backend('AGG')
#     plt.figure(figsize=(7,3))
    
#     fig = px.timeline(
# 						df, 
# 						x_start="Start", 
# 						x_end="Finish", 
# 						y="Responsible", 
# 						color="Responsible", 
# 						text='Project', 
# 						height=300, 
# 						width=1100, 
# 						color_discrete_sequence=px.colors.qualitative.T10,  #DARK CHOICE
						
						

# 						)
                        
                        
#     fig.update_layout({
#     'plot_bgcolor': 'rgba(0,0,0,0)',
#     'paper_bgcolor': 'rgba(0,0,0,0)'
# 	})
    
#     # fig = ff.create_gantt(df)
#     fig.update_yaxes(autorange="reversed")
#     plot(fig, output_type="div")
    
#     plt.tight_layout()
#     graph=get_graph()
#     return graph


# def stacked_bar(x_data,y_label):
#     segments = 4
    

#     percentages = ['Back End','Front End','Containers','DB','DS','Back End','Front End','Containers']
    
#     y_pos = np.arange(len(y_label))
    
#     fig = plt.figure(figsize=(20,8))
#     ax = fig.add_subplot(111)
    
#     colors ='rgwm'
#     # colors =[
#     #         'Pastel1', 'Pastel2', 'Paired', 'Accent',
#     #         'Dark2', 'Set1', 'Set2', 'Set3',
#     #         'tab10', 'tab20', 'tab20b', 'tab20c']
#     patch_handles = []
# 	# left alignment of x_data starts at zero
#     left = np.zeros(len(y_label)) 
#     for i, d in enumerate(x_data):
#         patch_handles.append(ax.barh(y_pos, d, 
# 		color=colors[i%len(colors)], align='center', 
# 		left=left))
#         left += d

# 	# search all of the bar segments and annotate
#     for j in range(len(patch_handles)):
#         for i, patch in enumerate(patch_handles[j].get_children()):
#             bl = patch.get_xy()
#             x = 0.5*patch.get_width() + bl[0]
#             y = 0.5*patch.get_height() + bl[1]
#             ax.text(x,y,
#                     percentages, color = 'white', ha = 'left', va = 'center')

#     # for bar, disease in zip(ax.patches, percentages[::-1]):
#     #     ax.text(0.1, bar.get_y()+bar.get_height()/2, disease, color = 'white', ha = 'left', va = 'center') 
    
            
#     ax.set_yticks(y_pos)
#     ax.set_yticklabels(y_label)
#     ax.set_xlabel('Allocated Time')
#     # plt.show()
    
#     plt.tight_layout()
#     graph=get_graph()
#     return graph





# from matplotlib.patches import ConnectionPatch

# def stacked_bar():
#     # make figure and assign axis objects
#     fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
#     fig.subplots_adjust(wspace=0)

#     # pie chart parameters
#     overall_ratios = [.56, .27, .17]
#     labels = ['TOTAL WORKED MONTHS', '???????', '???????']
#     explode = [0.1, 0, 0]
#     # rotate so that first wedge is split by the x-axis
#     angle = -180 * overall_ratios[0]
#     wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
#                         labels=labels, explode=explode)

#     # bar chart parameters
#     age_ratios = [.33, .54, .07, .06]
#     age_labels = ['Django', 'Python', 'Containers', 'Developer']
#     bottom = 1
#     width = .2

#     # Adding from the top matches the legend.
#     for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
#         bottom -= height
#         bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
#                     alpha=0.1 + 0.25 * j)
#         ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

#     ax2.set_title('Tech Stacks')
#     ax2.legend()
#     ax2.axis('off')
#     ax2.set_xlim(- 2.5 * width, 2.5 * width)

#     # use ConnectionPatch to draw lines between the two plots
#     theta1, theta2 = wedges[0].theta1, wedges[0].theta2
#     center, r = wedges[0].center, wedges[0].r
#     bar_height = sum(age_ratios)

#     # draw top connecting line
#     x = r * np.cos(np.pi / 180 * theta2) + center[0]
#     y = r * np.sin(np.pi / 180 * theta2) + center[1]
#     con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
#                         xyB=(x, y), coordsB=ax1.transData)
#     con.set_color([0, 0, 0])
#     con.set_linewidth(4)
#     ax2.add_artist(con)

#     # draw bottom connecting line
#     x = r * np.cos(np.pi / 180 * theta1) + center[0]
#     y = r * np.sin(np.pi / 180 * theta1) + center[1]
#     con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
#                         xyB=(x, y), coordsB=ax1.transData)
#     con.set_color([0, 0, 0])
#     ax2.add_artist(con)
#     con.set_linewidth(4)


#     plt.tight_layout()
#     graph=get_graph()
#     return graph

#     # plt.show()







# def stacked_bar():

#     fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

#     recipe = ["Django",
#           "Python",
#           "SQL",
#           "Containers",
#           "DB",
#           "Matplotlib"]

#     data = [225, 90, 50, 60, 100, 5]

#     wedges, texts = ax.pie(data, 
#                             wedgeprops=dict(width=0.2), 
#                             startangle=-40, 
#                             # autopct = autopct_format(data)
#                             # autopct='%.1f%%'
#                             )


#     bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
#     kw = dict(arrowprops=dict(arrowstyle="-"),
#             bbox=bbox_props, zorder=0, va="center")

#     for i, p in enumerate(wedges):
#         ang = (p.theta2 - p.theta1)/2. + p.theta1
#         y = np.sin(np.deg2rad(ang))
#         x = np.cos(np.deg2rad(ang))
#         horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
#         connectionstyle = "angle,angleA=0,angleB={}".format(ang)
#         kw["arrowprops"].update({"connectionstyle": connectionstyle})
#         ax.annotate(recipe[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
#                     horizontalalignment=horizontalalignment, **kw)

#     ax.set_title("Teck Stack Proportion")


#     plt.tight_layout()
#     graph=get_graph()
#     return graph





