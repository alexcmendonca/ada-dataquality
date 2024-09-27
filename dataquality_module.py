import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class DataQuality:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = self.load_data()

    def load_data(self):
        """Carrega o dataset a partir do caminho do arquivo especificado."""
        try:
            df = pd.read_csv(self.filepath)
            print(f"Arquivo carregado com sucesso: {self.filepath}")
            return df
        except FileNotFoundError:
            print(f"Erro: Arquivo não encontrado no caminho {self.filepath}")
            return None