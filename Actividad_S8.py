#Problema: Calcular la propina de un restaurante. Cuando vas a comer con amigos hay que tener en cuenta ciertas cosas
# Saber cuanto es el total de la cuenta, elegir que porcentaje de propina dejar, decidir entre cuantas personas 
# dividir la cuenta y ver cuanto le toca pagar a cada uno (incluyendo propina). Aunque en general al momento de pagar
# no se le da tanta complicación a veces ya sea por conveniencia o por etiqueta, es bueno tener en cuenta estos aspectos.#

import sys 
from PyQt5.QtWidgets import(QApplication, QWidget, QVBoxLayout,
                    QLabel, QLineEdit, QComboBox, QSpinBox, QPushButton)

class TipCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora de Propina")
        self.setGeometry(300, 300, 300, 250)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # 1. QLineEdit - Ingresar total de la cuenta
        self.total_input = QLineEdit()
        self.total_input.setPlaceholderText("Ingresa el total, ej: 150.50")
        layout.addWidget(QLabel("Total de la cuenta ($):"))
        layout.addWidget(self.total_input)

        # 2. QComboBox - Seleccionar porcentaje de propina
        self.tip_combo = QComboBox()
        self.tip_combo.addItems(["10%", "15%", "18%", "20%", "25%"])
        layout.addWidget(QLabel("Porcentaje de propina:"))
        layout.addWidget(self.tip_combo)

        # 3. QSpinBox - Número de personas
        self.people_spin = QSpinBox()
        self.people_spin.setMinimum(1)
        self.people_spin.setMaximum(20)
        self.people_spin.setValue(2)
        layout.addWidget(QLabel("Número de personas:"))
        layout.addWidget(self.people_spin)

        # 4. QLabel - Mostrar resultado
        self.result_label = QLabel("Cada persona paga: $0.00")
        self.result_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #2e7d32;")
        layout.addWidget(self.result_label)

        # 5. QPushButton - Calcular
        self.calc_button = QPushButton("Calcular Propina")
        self.calc_button.clicked.connect(self.calculate)
        layout.addWidget(self.calc_button)

        self.setLayout(layout)


    def calculate(self):
        try:
            total = float(self.total_input.text())
            tip_percent = int(self.tip_combo.currentText().replace("%", ""))
            people = self.people_spin.value()    

            tip_amount = total * (tip_percent / 100)
            total_con_propina = total + tip_amount
            por_persona = total_con_propina / people

            self.result_label.setText(f"Cada persona paga: ${por_persona:.2f}")
        except ValueError:
            self.result_label.setText("Por favor, ingresa un número válido")
        except Exception as e:
            self.result_label.setText("Error en el cálculo")

#Ejecutar la app                    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TipCalculator()
    window.show()
    sys.exit(app.exec_())



