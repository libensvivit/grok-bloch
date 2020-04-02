from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from qiskit import QuantumCircuit, QuantumRegister

q = QuantumRegister(1)
qc = QuantumCircuit(q)

qc.x()
qc.y()
qc.h()

qc.draw()

driver = webdriver.Chrome(r'C:/chromedriver/chromedriver.exe')
driver.get("http://127.0.0.1:5500/")
driver.execute_script("console.log('LOL')")

