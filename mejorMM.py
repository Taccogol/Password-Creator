import yfinance as yf
import numpy as np
import pandas as df
import matplotlib.pyplot as plt

# Definir el símbolo de la acción y el período de tiempo
symbol = "AAPL"
start_date = "2016-01-01"
end_date = "2022-01-01"

# Obtener los datos de Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Calcular los rendimientos logarítmicos
log_returns = np.log(data['Close']/data['Close'].shift(1))

# Definir los valores para las medias móviles a evaluar
ma_values = range(5, 51, 5)

# Calcular el MSE y AIC para cada combinación de medias móviles
mse_results = []
aic_results = []
for ma in ma_values:
    data[f"SMA_{ma}"] = data['Close'].rolling(ma).mean()
    log_returns_ma = log_returns - log_returns.rolling(ma).mean()
    residuals = log_returns_ma.dropna()
    mse = np.mean(residuals**2)
    mse_results.append(mse)
    n = len(residuals)
    k = 2  # número de parámetros en el modelo (media y varianza)
    aic = n*np.log(mse) + 2*k
    aic_results.append(aic)

# Encontrar las dos medias móviles con menor MSE y AIC
best_mse_indices = np.argsort(mse_results)[:2]
best_aic_indices = np.argsort(aic_results)[:2]
best_mse_moving_averages = [ma_values[i] for i in best_mse_indices]
best_aic_moving_averages = [ma_values[i] for i in best_aic_indices]

# Imprimir las dos medias móviles con menor MSE y AIC
print("Las dos medias móviles con menor MSE son:", best_mse_moving_averages)
print("Las dos medias móviles con menor AIC son:", best_aic_moving_averages)

# Calcular las señales de compra y venta basadas en las medias móviles seleccionadas
for ma in best_mse_moving_averages:
    data[f"SMA_{ma}"] = data['Close'].rolling(ma).mean()

buy_signals = (data['SMA_'+str(best_mse_moving_averages[0])] > data['SMA_'+str(best_mse_moving_averages[1])]) & \
              (data['SMA_'+str(best_mse_moving_averages[0])].shift(1) < data['SMA_'+str(best_mse_moving_averages[1])].shift(1))
sell_signals = (data['SMA_'+str(best_mse_moving_averages[0])] < data['SMA_'+str(best_mse_moving_averages[1])]) & \
               (data['SMA_'+str(best_mse_moving_averages[0])].shift(1) > data['SMA_'+str(best_mse_moving_averages[1])].shift(1))

# Graficar los precios de cierre y las medias móviles seleccionadas
# Graficar los precios de cierre y las medias móviles seleccionadas
fig, ax = plt.subplots(figsize=(15,10))
ax.plot(df.index, df['Close'], label='Precio de cierre')
ax.plot(df.index, df[ema1], label=f'{ema1} días EMA')
ax.plot(df.index, df[ema2], label=f'{ema2} días EMA')
ax.set_xlabel('Fecha')
ax.set_ylabel('Precio de cierre')
ax.legend()
plt.show()

# Calcular el retorno de la estrategia de compra y venta basada en las medias móviles seleccionadas
df['Posicion'] = np.where(df[ema1] > df[ema2], 1, 0)
df['Retorno'] = df['Close'].pct_change() * df['Posicion'].shift(1)
retorno_total = (df['Retorno'] + 1).cumprod()[-1]

# Imprimir las medias móviles seleccionadas y los retornos
print(f'Las medias móviles seleccionadas son {ema1} y {ema2}')
print(f'El retorno total de la estrategia es {retorno_total}')
