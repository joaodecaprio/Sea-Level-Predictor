import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Importar os dados
    df = pd.read_csv('epa-sea-level.csv')

    # Criar o scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], alpha=0.6, edgecolors='none')

    # Linha de melhor ajuste com todos os dados
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    y_all = res_all.slope * years_extended + res_all.intercept
    ax.plot(years_extended, y_all, color='red', linewidth=2, label='Fit: 1880–2050')

    # Linha de melhor ajuste usando dados a partir de 2000
    df_2000 = df[df['Year'] >= 2000]
    res_2000 = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_2000_extended = pd.Series(range(2000, 2051))
    y_2000 = res_2000.slope * years_2000_extended + res_2000.intercept
    ax.plot(years_2000_extended, y_2000, color='green', linewidth=2, label='Fit: 2000–2050')

    # Rótulos e título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Ajustar limites do eixo X para cobrir 1880–2050
    ax.set_xlim(1880, 2050)
    
    # Definir ticks específicos do eixo X
    ax.set_xticks([1850.0, 1875.0, 1900.0, 1925.0, 1950.0, 1975.0, 2000.0, 2025.0, 2050.0, 2075.0])

    # Grade e legenda
    ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
    ax.legend(loc='upper left')

    # Salvar imagem
    plt.tight_layout()
    plt.savefig('sea_level_plot.png')
    return plt.gca()