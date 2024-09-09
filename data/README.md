# Pasta `data` — dados referentes ao projeto Arboviroses na Fronteira

Os dados brutos são: 

## `armadilhas_liraa_XY.csv`:

Dados de coleta das armadilhas de mosquito com unidade espacial. (latitude = X, longitude = Y e identificação do quarteirão).

## `mosquitos positivos 2017 a 2022.xlsx`:

Dados de coleta das armadilhas de mosquito com unidade espacial (latitude = X, longitude = Y e identificação do quarteirão). Esse dado fornece apenas o resultado das armadilhas em que foi encontrado algum mosquito infectado com alguma arbovirose (dengue, zika ou chik). 

Segue legenda das informações de Armadilhas relativas as duas tabelas acima:
* `tt_dep_aa` = Total de Depósitos de Aedes aegypti
* `tt_dep_aalb` = Total de Depósitos de Aedes albopictus
* `tt_dep_out` = Total de Depósitos de Outros mosquitos
* `m_aaeg_m_m` = Mosquito Aedes aegypti Macho Morto
* `m_aaeg_m_v` = Mosquito Aedes aegypti Macho Vivo
* `m_aaeg_f_m` = Mosquito Aedes aegypti Fêmea Morta
* `m_aaeg_f_v` = Mosquito Aedes aegypti Fêmea Viva
* `m_aalb_m_m` = Mosquito Aedes albopictus Macho Morto
* `m_aalb_m_v` = Mosquito Aedes albopictus Macho Vivo
* `m_aalb_f_m` = Mosquito Aedes albopictus Fêmea Morta
* `m_aalb_f_v` = Mosquito Aedes albopictus Fêmea Viva
* `m_out_m_m` = Mosquito Outros Macho Morto
* `m_out_m_v` = Mosquito Outros Macho Vivo
* `m_out_f_m` = Mosquito Outros Fêmea Morta
* `m_out_f_v` = Mosquito Outros Fêmea Viva


## `sinan_dengue_2010_2022_Foz_sem_identificacao.csv`

São os dados de notificação, com os dados individuais e variáveis similares as do SINAN. 

## IMPORTANTE

Podemos analisar os dados de armadilhas e de notifação de forma espacial utilizando a coluna `quarteirao`, presentes em ambos os datasets. Essa coluna representa geograficamente em qual quarteirão mora o paciente notificado, localizado pelo endereço informado no SINAN, ou onde fica a armadilha.

Na pasta, shapefile, temos os arquivos necessários para plotar esses quarteirões de forma espacial.

As tabelas abaixo, foram criadas **após um tratamento dos dados brutos** usando as funções no script `generate_data.py`.

## `weather-2010_2022.csv`

Arquivo contendo dados referentes ao clima de Foz do Iguaçu — PR, Brasil, entre 01/01/2010 e 30/06/2022. O arquivo foi criado usando a função `generate_data.weather_data()`. 

As variáveis constantes deste arquivo são:

* `date`: data do evento.
* `daily_precipitation-mm`: precipitação diária, em milímetros (`mm`).
* `temp_max-celsius`: temperatura máxima, em graus Celsius (`°C`).
* `temp_min-celsius`: temperatura mínima, em graus Celsius (`°C`).
* `temp_mean-celsius`: temperatura média, em graus Celsius (`°C`).
* `mean_relative_humidity-%`: porcentagem de umidade relativa (`%`).
* `mean_wind_speed-m_per_s`: velocidade média do vento, em metros por segundo (`m/s`).

## `mosq_aaeg_trap-2017_2022.csv`

Arquivo contendo dados referentes as coletas das armadilhas realizadas em Foz entre 2017 e 2022 agregados por dia. O arquivo foi criado usando a função `generate_data.total_mosquitos_traps()`. 


As variáveis constantes deste arquivo são:

* `date`: data de coleta.
* `tt_dep_aa`: total de depositos com mosquito encontrados.
* `m_aaeg_m_m`: total de mosquitos *aedes aegypti* machos mortos encontrados nas armadilhas.
* `m_aaeg_m_v`:total de mosquitos *aedes aegypti* machos vivos encontrados nas armadilhas.
* `m_aaeg_f_m`: total de mosquitos *aedes aegypti* fêmeas mortos encontrados nas armadilhas.
* `m_aaeg_f_v`:total de mosquitos *aedes aegypti* fêmeas vivos encontrados nas armadilhas.
* `n_traps`: Número de armadilhas coletadas.

## `mosq_aaeg_trap_pos_2017_2022.csv`

Arquivo contendo dados referentes as coletas das armadilhas realizadas em Foz entre 2017 e 2022 agregados por dia, **as quais, dentre os mosquitos vivos, foi encontrada a presença de vírus da dengue**, chik ou zika. O arquivo foi criado usando a função `generate_data.total_mosquitos_traps()`. 

As variáveis constantes deste arquivo são:

* `date`: data de coleta.
* `tt_dep_a_pos`: total de depositos com mosquito encontrados.
* `m_aaeg_m_m_pos`: total de mosquitos *aedes aegypti* machos mortos encontrados nas armadilhas.
* `m_aaeg_m_v_pos`:total de mosquitos *aedes aegypti* machos vivos encontrados nas armadilhas.
* `m_aaeg_f_m_pos`: total de mosquitos *aedes aegypti* fêmeas mortos encontrados nas armadilhas.
* `m_aaeg_f_v_pos`:total de mosquitos *aedes aegypti* fêmeas vivos encontrados nas armadilhas.
* `n_traps_pos`: Número de armadilhas coletadas.


## dengue_cases-2010_2022.csv

Neste arquivo temos os casos notificados de dengue, agregados pela data de primeiro sintomas, separados em três categorias: `notified`, `probable`, `lab_confirmed`. O arquivo foi criado usando a função `generate_data.dengue_cases()`. 

As curvas que iniciam com `acum` representam o valor acumulado da variável em questão.

As variáveis constantes desse arquivo são: 

* `dt_sin_pri`: data de primeiro sintomas;
* `notified`: casos notificados (todas as entradas da tabela);
* `probable`: casos prováveis. São os casos notificados menos os descartados (`classi_fin == 5`) e o de chikungunya (`classi_fin == 13`);
* `lab_confirmed`: casos de dengue confirmados em laboratório. Casos em que (`criterio == 1`) menos os descartados (`classi_fin == 5`) e o de chikungunya (`classi_fin == 13`);
