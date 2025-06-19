# ECB_Nowcasting_Toolbox_Python
Python version of the public Nowcasting Toolbox of the European Central Bank

nowcasting_toolbox_py/
├── README.md
├── pyproject.toml
├── requirements.txt
├── setup.py
├── nowcasting_toolbox_py/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   └── loader.py               # funciones de carga y preprocesado
│   ├── models/
│   │   ├── __init__.py
│   │   ├── dfm.py                  # Dynamic Factor Model
│   │   ├── bvar.py                 # Bayesian VAR
│   │   └── bridge.py               # regresión “bridge”
│   ├── variable_selection/
│   │   ├── __init__.py
│   │   └── selector.py             # ranking y selección de variables
│   ├── evaluation/
│   │   ├── __init__.py
│   │   ├── metrics.py              # métricas de error (MSE, MAE…)
│   │   └── plots.py                # gráficos de precisión, heatmaps
│   └── utils/
│       ├── __init__.py
│       ├── dates.py                # alineación de series, manejo de vintages
│       └── io.py                   # I/O genérico, logs
└── tests/
    ├── __init__.py
    ├── test_data_loader.py
    ├── test_dfm.py
    └── test_selector.py

