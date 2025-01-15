import matplotlib.pyplot as plt
import numpy as np
from src.black_scholes import black_scholes

def plot_option_prices(S_range, K, T, r, sigma):
    call_prices = [black_scholes(S, K, T, r, sigma, "call") for S in S_range]
    put_prices = [black_scholes(S, K, T, r, sigma, "put") for S in S_range]

    plt.figure(figsize=(10, 6))
    plt.plot(S_range, call_prices, label="Call Option Price")
    plt.plot(S_range, put_prices, label="Put Option Price")
    plt.xlabel("Stock Price (S)")
    plt.ylabel("Option Price")
    plt.title("Option Price vs Stock Price")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    S_range = np.linspace(50, 150, 100)
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    plot_option_prices(S_range, K, T, r, sigma)
