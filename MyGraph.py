import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))
plt.show()

# How to setup Virtual Environment 1: Open Terminal, write ' py -3 -m venv introvenv', hit ENTER
# How to setup Virtual Environment 2: Next line of Terminal, write pathway '.\introvenv\Scripts\activate' (might be 'introvenv\Scripts\activate)
# How to setup Virtual Environment 3: Next line of Terminal, use 'pip install ______' and insert whichever library you need