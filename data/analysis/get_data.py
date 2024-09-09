import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

def get_trap_data(filename = '../mosq_aaeg_trap-2017_2022.csv', replace = True): 
    '''
    Essa função faz o download dos dados de armadilhas dos mosquitos capturados. 
    '''
    
    df_m = pd.read_csv(filename, index_col = 'date')
    df_m.index = pd.to_datetime(df_m.index)

    df_m = df_m.resample('1M').sum()

    df_m = df_m.loc[~df_m.index.month.isin([2,4,6,8,10,12])]

    df_m['trapped'] = df_m.m_aaeg_f_m + df_m.m_aaeg_f_v

    df_m.index = pd.to_datetime(df_m.index)

    df_m.index = df_m.index.map(lambda t: t.replace(day=1))
    
    
    if replace: 
        try:
            idx = np.where(df_m.trapped == 0)[0][0]
            df_m.iloc[idx] = ((df_m.iloc[idx-1] + df_m.iloc[idx+1])/2).astype(int)

        except:
             print('Não há valores nulos em trapped')
    

    return df_m


def get_dengue_data(filename = '../dengue_cases-2010_2022.csv', mean = True):

    '''
    Essa função faz o download dos dados de dengue previamente limpos pelo Alex. 
    São retornadas as séries temporais de casos notificados, prováveis e confirmados
    em laboratório. 
    :params mean: boolean. If True, é aplicada uma média móvel de 7 dias nos dados.
    '''

    data = pd.read_csv(filename, index_col = 'dt_sin_pri')

    data.index = pd.to_datetime(data.index)

    if mean:
        data = data.rolling(window = 7).mean().dropna()


    return data 


def get_mos_trap():

    '''
    Essa função faz o download dos dados de armadilhas limpos e prontos para
    serem aplicados no fitting do modelo de edo.  
    '''

    data = pd.read_csv('../../../data/mosq_trapped_model.csv', index_col = 'Unnamed: 0')

    data.index = pd.to_datetime(data.index)

    return data 


def parse_date(date):
    
    """Transforma os dados no formato correto, acrescendo 0 no início de alguns dias e
    meses do ano para garantir que o pd.to_datetime não vai interpretar a data de forma 
    equivocada
    """
    
    new_date = ''
    
    for i in date.split('/'): 

        if len(i) == 1:

            new_date = new_date + '0'+ i + '/' 

        else:

            new_date =  new_date + i + '/' 
        
    new_date = new_date[:-1]
    
    return new_date


def get_weather_data(ini_date = None, end_date = None):
    ''''
    Essa função carrega os dados climáticos já preprocessados e salvos no github.
    '''

    we_data = pd.read_csv('../weather-2010_2022.csv')
    
    we_data.set_index('Data', inplace = True)

    we_data.index = pd.to_datetime(we_data.index)

    we_data = we_data.sort_index()

    if (type(ini_date) == str) and (type(end_date) == str):
         
         we_data = we_data.loc[ini_date:end_date]


    return we_data 

def plot_data(df):
    '''
    Essa função plota os dados de casos notificados diários e notificados lado a lado. 
    :params df: pd.DataFrame. O dataframe obrigatoriamente deve ter as colunas:
                            * `notified`
                            * `acum_notified`
    '''
    fig, ax = plt.subplots(1,2, figsize = (12,5))

    ax[0].plot(df.notified)

    ax[0].set_title('Casos Notificados diários')
    ax[0].grid()

    for tick in ax[0].get_xticklabels():
            tick.set_rotation(45)

    ax[1].plot(df.acum_notified)

    ax[1].set_title('Casos Notificados acumulados')
    ax[1].grid()

    for tick in ax[1].get_xticklabels():
            tick.set_rotation(45)

    plt.show()


def get_temp(start_date, end_date):
    '''
    Função que retorna um array com a temperatura média em um determinado intervalo de 
    tempo.
    :params start_date: string. Data no formato: %Y-%m-%d.
    :params end_date: string. Data no formato: %Y-%m-%d.
    :returns: array.
    '''
    
    df_we = get_weather_data()
    
    df_we = df_we.loc[(df_we.index >= start_date) & (df_we.index <= end_date)]
    
    return df_we['temp_mean-celsius'].values