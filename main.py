from Experimento import *
from agglomerativeClustering import *
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

    # Rotaciona os nome
    plt.xticks(rotation=45)
    plt.show()


def plot_values(df, title: str):

    plt.style.use('_mpl-gallery')

    plt.text(2.5, -2, 'Texto abaixo do gráfico', ha='center', va='center', fontsize=12)

    x = df.columns.tolist()[0:-1] #['Pop', 'Sertanejo', 'Funk', 'Rock', 'Bandinha', 'Pisadinha',...),dtype='object')
    print(x)

    fig, ax = plt.subplots(figsize=(20, 5))

    colors  = [
    'red', 'green', 'blue', 'orange', 'purple', 'brown', 'pink', 'gray', 'olive',
    'cyan', 'magenta', 'yellow', 'teal', 'indigo', 'salmon', 'lime', 'tan', 'violet', 'aqua', 'lightcoral'
    ]

    for i, linha in df.iterrows():
        y = linha.values[0:-1]
        ax.plot(x, y, label=f'grupo {i}',color=colors[i])


    #ax.set(ylim=(0,1))
    ax.legend()
    fig.canvas.draw()
    plt.xticks(rotation=45)

    plt.title(title)
    plt.ylabel('gostos')
    plt.savefig(f'comparacao{title}.png',dpi=300, bbox_inches='tight')
    plt.show(bbox_inches='tight')

def main():
    kfg = pd.read_csv('grupos.csv')
    #teste_pop(kfg)
    plot_values(kfg,'K-means')
    hdbdf = pd.read_csv('grupos2.csv')
    plot_values(hdbdf,'HDBSCAN')


if __name__ == "__main__":
    main()