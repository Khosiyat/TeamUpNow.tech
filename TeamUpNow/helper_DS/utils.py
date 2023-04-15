import matplotlib.pyplot as plt
import base64
from io import BytesIO


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

    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph

def get_bar_techSkills(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('Tech Skills | Candidate', color='#008a3e', fontweight='book')
    plt.barh(x,y, color='#18A558',  
                    edgecolor='white',
                    linewidth=0,

                    )
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()
    ax.set_xticklabels(['NAIVE', 'EXPERIENCED', '  EXPERT'])
    

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)

    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph


def get_bar_jobPerformence(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('Job Performence | Candidate', color='#008a3e', fontweight='book')
    plt.barh(x,y, color='#18A558',  edgecolor='#f1f1f1')
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()
    ax.set_xticklabels(['NAIVE', 'EXPERIENCED', '  EXPERT'])


    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)

    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
    plt.tight_layout()
    # plt.subplots()
    graph=get_graph()
    return graph


def get_bar_softSkill(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(4,3))
    plt.title('Soft Skills | Candidate', color='#008a3e', fontweight='book')
    plt.barh(x,y, color='#18A558',  edgecolor='#f1f1f1')
    
    plt.xticks(rotation=0, ha='left', color='#18A558', fontsize=7)
    ax = plt.subplot()
    ax.set_xticklabels(['NAIVE', 'EXPERIENCED', '     EXPERT'])

    
    plt.margins(0.02)
    plt.subplots_adjust(bottom=0.15)

    # plt.xlabel('Follow_recruiter_1', color='#18A558')
    # plt.ylabel('FollowER_recruiter_1', color='#18A558')
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

