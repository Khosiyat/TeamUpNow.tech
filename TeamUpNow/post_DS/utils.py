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
        facecolor='none', edgecolor='none',
        backend=None
       )
    buffer.seek(0)
    image_png=buffer.getvalue()
    graph=base64.b64encode(image_png)
    graph=graph.decode('utf-8')
    buffer.close()
    return graph


############################################################### ------> BAR

def get_bar(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('score rating of')
    plt.bar(x,y, color='#18A558',  edgecolor='#f1f1f1')
    
    plt.xticks(rotation='vertical', color='#18A558')
    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph


 
def get_communication_skills(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,1.3))
    colors= ['#72B7B2', '#ED9F5F', '#DD8E8E']
    plt.title('communication skills', color='#008a3e', fontweight='book')
    plt.barh(x,y, color=colors,  
                    edgecolor='white',
                    linewidth=0,

                    )
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    ax.set_xticklabels(['NAIVE', '', 'EXPERIENCED', '',  '', 'EXPERT'])
    

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph
    

def get_team_work_skills(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,1))
    colors= ['#72B7B2', '#ED9F5F']
    plt.title('team work skills', color='#008a3e', fontweight='book')
    plt.barh(x,y, color=colors,  
                    edgecolor='white',
                    linewidth=0,

                    )
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    ax.set_xticklabels(['NAIVE', '', 'EXPERIENCED', '',  '', 'EXPERT'])
    

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph
    
def get_leadership_skills(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,1))
    colors= ['#DD8E8E', '#4C78A8']
    plt.title('leadership skills', color='#008a3e', fontweight='book')
    
    plt.barh(x,y, color=colors,  
                    edgecolor='white',
                    linewidth=0,

                    )
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    ax.set_xticklabels(['NAIVE', '', 'EXPERIENCED', '',  '', 'EXPERT'])
    

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph
    


# 6
def get_code_quality(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,2))

    colors= ['#72B7B2', '#ED9F5F', '#DD8E8E', '#4C78A8']

    plt.title('code quality', color='#008a3e', fontweight='book')

    plt.barh(x,y, color=colors,  
                    edgecolor='white',
                    linewidth=0,

                    )


    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
    ax.set_xticklabels(['NAIVE', '', 'EXPERIENCED', '',  '', 'EXPERT'])
    

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph

# 4
def get_problem_solving_skills(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,1.4))
    colors= ['#72B7B2', '#ED9F5F', '#DD8E8E', '#4C78A8']
    plt.title('problem solving Skills', color='#008a3e', fontweight='book')
    plt.barh(x,y, color=colors,  
                    edgecolor='white',
                    linewidth=0,

                    )
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    
    ax.set_xticklabels(['NAIVE', '', 'EXPERIENCED', '',  '', 'EXPERT'])
    

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph

def get_bar_techSkills(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('_____________-', color='#008a3e', fontweight='book')
    plt.barh(x,y, color='#18A558',  
                    edgecolor='white',
                    linewidth=0,

                    )
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    ax.set_xticklabels(['NAIVE', 'EXPERIENCED', '  EXPERT'])
    

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph


def get_bar_jobPerformence(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('Job Performence | Candidate', color='#008a3e', fontweight='book')
    plt.barh(x,y, color='#18A558',  edgecolor='#f1f1f1')
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    ax.set_xticklabels(['NAIVE', 'EXPERIENCED', '  EXPERT'])


    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    
    plt.tight_layout()
    
    graph=get_graph()
    return graph


def get_bar_softSkill(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('Soft Skills | Candidate', color='#008a3e', fontweight='book')
    plt.barh(x,y, color='#18A558',  edgecolor='#f1f1f1')
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()

    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

    ax.set_xticklabels(['NAIVE', 'EXPERIENCED', '     EXPERT'])

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)

    plt.tight_layout()
    graph=get_graph()
    return graph


def get_bar_chart_profile(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('Profile Rating | Evaluator', color='#008a3e', fontweight='book')
    plt.bar(x,y, color='#18A558',  edgecolor='#f1f1f1')
    
    plt.xticks(rotation=90, color='#18A558')

    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)
    plt.tight_layout()
    
    graph=get_graph()
    return graph

############################################################### ------> PIE CHART

def get_pie(x_data,y_label):

    explode = (0, 0.04, 0.07, 0.05, 0.08)
    colors = ['#ff4040','#ffa500','#18A558','#ff4040','#ffa500']

    plt.switch_backend('AGG')
    plt.pie(x_data,explode=explode, colors=colors,  labels=y_label, autopct='%1.1f%%',
        shadow=True, startangle=90)
    plt.xticks(rotation=45, color='#18A558')
    plt.tight_layout()
    graph=get_graph()
    return graph


def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{v:d}'.format(v=val)
    return my_format

def get_pie_postDashboard_projects(x_data,y_label):

    colors = ['#F58518','#F58518','#4C78A8','#F58518','#4C78A8']
    

    plt.switch_backend('AGG')
    plt.subplots(figsize=(2.5, 1.6), subplot_kw=dict(aspect="equal"))
    
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
    plt.tight_layout()
    graph=get_graph()
    return graph


def get_pie_post_projects(x_data,y_label):

    colors = ['#F58518','#F58518','#4C78A8','#F58518','#4C78A8']
    

    plt.switch_backend('AGG')
    plt.subplots(figsize=(3.5, 3), subplot_kw=dict(aspect="equal"))
    
    plt.pie(x_data, 
            colors=colors,  
            labels=y_label, 
            shadow=True, 
            wedgeprops=dict(width=0.1), 
            startangle=-40,
            autopct='%1.1f%%',
            # autopct = autopct_format(x_data)
            )

    plt.xticks(rotation=45, color='#18A558')
    plt.tight_layout()
    graph=get_graph()
    return graph





def get_bar_chart_postDashboard_quality(x,y):

    colors = ['#F58518', '#4C78A8']
    labels = ['conciseness', 'relevancy']

    plt.switch_backend('AGG')
    # plt.figure(figsize=(0.2,0.1))
    plt.title('Quality of the Post', color='#008a3e', fontweight='book')
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








############################################################### ------> PLOT

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


############################################################### ------> SCATTER

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





class BubbleChart:
    def __init__(self, area, bubble_spacing=0):
        """
        Setup for bubble collapse.

        Parameters
        ----------
        area : array-like
            Area of the bubbles.
        bubble_spacing : float, default: 0
            Minimal spacing between bubbles after collapsing.

        Notes
        -----
        If "area" is sorted, the results might look weird.
        """
        area = np.asarray(area)
        r = np.sqrt(area / np.pi)

        self.bubble_spacing = bubble_spacing
        self.bubbles = np.ones((len(area), 4))
        self.bubbles[:, 2] = r
        self.bubbles[:, 3] = area
        self.maxstep = 2 * self.bubbles[:, 2].max() + self.bubble_spacing
        self.step_dist = self.maxstep / 2

        # calculate initial grid layout for bubbles
        length = np.ceil(np.sqrt(len(self.bubbles)))
        grid = np.arange(length) * self.maxstep
        gx, gy = np.meshgrid(grid, grid)
        self.bubbles[:, 0] = gx.flatten()[:len(self.bubbles)]
        self.bubbles[:, 1] = gy.flatten()[:len(self.bubbles)]

        self.com = self.center_of_mass()

    def center_of_mass(self):
        return np.average(
            self.bubbles[:, :2], axis=0, weights=self.bubbles[:, 3]
        )

    def center_distance(self, bubble, bubbles):
        return np.hypot(bubble[0] - bubbles[:, 0],
                        bubble[1] - bubbles[:, 1])

    def outline_distance(self, bubble, bubbles):
        center_distance = self.center_distance(bubble, bubbles)
        return center_distance - bubble[2] - \
            bubbles[:, 2] - self.bubble_spacing

    def check_collisions(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        return len(distance[distance < 0])

    def collides_with(self, bubble, bubbles):
        distance = self.outline_distance(bubble, bubbles)
        idx_min = np.argmin(distance)
        return idx_min if type(idx_min) == np.ndarray else [idx_min]

    def collapse(self, n_iterations=50):
        """
        Move bubbles to the center of mass.

        Parameters
        ----------
        n_iterations : int, default: 50
            Number of moves to perform.
        """
        for _i in range(n_iterations):
            moves = 0
            for i in range(len(self.bubbles)):
                rest_bub = np.delete(self.bubbles, i, 0)
                # try to move directly towards the center of mass
                # direction vector from bubble to the center of mass
                dir_vec = self.com - self.bubbles[i, :2]

                # shorten direction vector to have length of 1
                dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))

                # calculate new bubble position
                new_point = self.bubbles[i, :2] + dir_vec * self.step_dist
                new_bubble = np.append(new_point, self.bubbles[i, 2:4])

                # check whether new bubble collides with other bubbles
                if not self.check_collisions(new_bubble, rest_bub):
                    self.bubbles[i, :] = new_bubble
                    self.com = self.center_of_mass()
                    moves += 1
                else:
                    # try to move around a bubble that you collide with
                    # find colliding bubble
                    for colliding in self.collides_with(new_bubble, rest_bub):
                        # calculate direction vector
                        dir_vec = rest_bub[colliding, :2] - self.bubbles[i, :2]
                        dir_vec = dir_vec / np.sqrt(dir_vec.dot(dir_vec))
                        # calculate orthogonal vector
                        orth = np.array([dir_vec[1], -dir_vec[0]])
                        # test which direction to go
                        new_point1 = (self.bubbles[i, :2] + orth *
                                      self.step_dist)
                        new_point2 = (self.bubbles[i, :2] - orth *
                                      self.step_dist)
                        dist1 = self.center_distance(
                            self.com, np.array([new_point1]))
                        dist2 = self.center_distance(
                            self.com, np.array([new_point2]))
                        new_point = new_point1 if dist1 < dist2 else new_point2
                        new_bubble = np.append(new_point, self.bubbles[i, 2:4])
                        if not self.check_collisions(new_bubble, rest_bub):
                            self.bubbles[i, :] = new_bubble
                            self.com = self.center_of_mass()

            if moves / len(self.bubbles) < 0.1:
                self.step_dist = self.step_dist / 2

    def plot(self, ax, labels, colors):
        """
        Draw the bubble plot.

        Parameters
        ----------
        ax : matplotlib.axes.Axes
        labels : list
            Labels of the bubbles.
        colors : list
            Colors of the bubbles.
        """
        for i in range(len(self.bubbles)):
            circ = plt.Circle(
                self.bubbles[i, :2], self.bubbles[i, 2], color=colors[i])
            ax.add_patch(circ)
            ax.text(*self.bubbles[i, :2], labels[i],
                    horizontalalignment='center', verticalalignment='center')








def get_bubblePlot(x, y):
    plt.switch_backend('AGG')
    

    data_bubblePlot = {
        'y_data': y,
        'x_data': x,
        'color': ['#72B7B2', '#E45756', '#DD8E8E', '#4C78A8', '#ED9F5F']
    }


    bubble_chart = BubbleChart(area=data_bubblePlot['x_data'],
                           bubble_spacing=0.1)

    bubble_chart.collapse()

    fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
    bubble_chart.plot(
        ax, data_bubblePlot['y_data'], data_bubblePlot['color'])
    ax.axis("off")
    ax.relim()
    ax.autoscale_view()
    ax.set_title('Candidate Skills', color='#ED9F5F')

    plt.show()
    
    graph=get_graph()
    return graph



