from Experimento import *

import matplotlib.pyplot as plt


def teste_pop(df):
    nomes = df['Nome']
    pop = df['Pop']

    # grafico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(nomes, pop)

    plt.xlabel('grupos')
    plt.ylabel('pop')
    plt.title('Teste= peso do pop nos dados')

    # Rotacionar os nome
    plt.xticks(rotation=45)

    # Mostrar o gráfico
    plt.show()


def plot_values(df):

    plt.style.use('_mpl-gallery')

    x = df.columns.tolist()[0:-1] #['Pop', 'Sertanejo', 'Funk', 'Rock', 'Bandinha', 'Pisadinha',...),dtype='object')
    print(x)

    fig, ax = plt.subplots(figsize=(20, 5))

    colors = ['black','blue','green','yellow',]

    for i, linha in df.iterrows():
        y = linha.values[0:-1]
        ax.plot(x, y, label=f'grupo {i}',color=colors[i])

    ax.set(ylim=(0,1))
    ax.legend()
    fig.canvas.draw()
    plt.xticks(rotation=45)
    plt.ylabel('gostos')
    plt.savefig('C:\\Users\\gustavo.alberton\\Documents\\pythonProject1\\dispersão.png',dpi=300, bbox_inches='tight')
    plt.show(bbox_inches='tight')

def main():
    dfg = pd.read_csv('grupos.csv')
    #teste_pop(dfg)
    plot_values(dfg)


if __name__ == "__main__":
    main()