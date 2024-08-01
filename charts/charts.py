import matplotlib.pyplot as plt

def generate_pie_chart():
    labels1 = ['A', 'B', 'C']
    values = [150, 112, 234]

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels1)
    plt.savefig('pie.png')
    plt.close()
    print ('fin')
