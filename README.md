# 🚗 Sistema de Gestión de Parqueadero con Tkinter 🅿️

## 📝 Descripción del Proyecto
Este proyecto implementa un sistema de gestión de parqueadero utilizando Python y la biblioteca Tkinter para la interfaz gráfica. 🖥️ El sistema permite asignar espacios de estacionamiento disponibles a usuarios registrados, liberar espacios ocupados y guardar la información en un archivo Excel. 📂

## 🌟 Características Principales
- **Asignación Automática de Espacios**: Los espacios disponibles se asignan aleatoriamente a los usuarios. 🎲
- **Interfaz Gráfica**: Proporciona una interfaz visual intuitiva para gestionar el parqueadero. 🖼️
- **Persistencia de Datos**: Guarda la información de los usuarios y sus matrículas en un archivo Excel (`base.xlsx`). 📊
- **Actualización en Tiempo Real**: La interfaz refleja el estado actual de los espacios de estacionamiento. ⏰

## 🛠️ Componentes del Sistema
- **Espacios de Estacionamiento**: Representados por botones en la interfaz. 🅿️
- **Entradas de Usuario**:
  - `Matrícula`: Identificador único del vehículo. 🆔
  - `Nombre`: Nombre del usuario. 👤
- **Botones**:
  - Botones numerados para representar los espacios de estacionamiento. 🔢
  - Botón "Estacionar" para registrar un nuevo vehículo. 🚘

## ⚙️ Funcionamiento
1. **Asignación de Espacios**:
   - El usuario ingresa su nombre y matrícula. ✍️
   - Si hay espacios disponibles, el sistema asigna uno aleatoriamente y actualiza la interfaz. 🎯
2. **Liberación de Espacios**:
   - Al hacer clic en un espacio ocupado, este se libera y se actualiza la interfaz. 🔓
3. **Guardado de Datos**:
   - La información del usuario se guarda en un archivo Excel (`base.xlsx`) en la hoja `Base`. 📋

## 📥 Requisitos
- **Python 3.x**
- Bibliotecas requeridas:
  - `tkinter`
  - `pandas`
  - `openpyxl`

## 🚀 Instalación
1. Instale las dependencias necesarias:
   ```bash
   pip install pandas openpyxl
