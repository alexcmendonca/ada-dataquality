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

    def null_count(self):
        """Conta os valores nulos por coluna."""
        return self.df.isnull().sum()

    def unique_count(self):
        """Conta os valores únicos por coluna."""
        return self.df.nunique()

    def describe_numerics(self):
        """Retorna as estatísticas descritivas das colunas numéricas."""
        return self.df.describe()

    def value_counts_categorical(self):
        """Retorna a contagem de valores para colunas categóricas."""
        categorical_columns = self.df.select_dtypes(include=['object']).columns
        return {col: self.df[col].value_counts() for col in categorical_columns}

    def plot_distributions(self, max_categories=10):
        """Gera gráficos de distribuição para colunas categóricas e numéricas com limitação no eixo X."""
        
        # Colunas categóricas
        categorical_columns = self.df.select_dtypes(include=['object']).columns
        
        for col in categorical_columns:
            unique_values = self.df[col].nunique()

            if unique_values > max_categories:
                # Se há mais categorias do que o limite, cria gráficos em partes
                parts = (unique_values // max_categories) + 1
                for part in range(parts):
                    plt.figure(figsize=(10, 6))
                    sns.countplot(data=self.df, x=col, 
                                  order=self.df[col].value_counts().index[part * max_categories:(part + 1) * max_categories])
                    plt.title(f'Distribuição da coluna categórica: {col} (Parte {part + 1})')
                    plt.xticks(rotation=45)
                    plt.tight_layout()
                    plt.show()
            else:
                # Se o número de categorias é menor ou igual ao limite, exibe normalmente
                plt.figure(figsize=(10, 6))
                sns.countplot(data=self.df, x=col, order=self.df[col].value_counts().index)
                plt.title(f'Distribuição da coluna categórica: {col}')
                plt.xticks(rotation=90)
                plt.tight_layout()
                plt.show()
    
    def plot_numeric_distributions(self):
        """Gera gráficos de distribuição para colunas numéricas."""
        numeric_columns = self.df.select_dtypes(include=['number']).columns
        for col in numeric_columns:
            plt.figure(figsize=(8, 6))
            sns.histplot(data=self.df, x=col, kde=True)
            plt.title(f'Distribuição da coluna numérica: {col}')
            plt.tight_layout()
            plt.show()

    def run_analysis(self, max_categories=10):
        """Executa todas as análises e gera um relatório básico."""
        print("Iniciando análise de qualidade de dados...\n")
        
        print("Contagem de valores nulos:")
        print(self.null_count())
        
        print("\nContagem de valores únicos:")
        print(self.unique_count())
        
        print("\nEstatísticas descritivas das colunas numéricas:")
        print(self.describe_numerics())
        
        print("\nContagem de valores nas colunas categóricas:")
        for col, counts in self.value_counts_categorical().items():
            print(f"\nColuna: {col}")
            print(counts)
        
        print("\nGerando gráficos de distribuição para colunas categóricas...")
        self.plot_distributions(max_categories=max_categories)
        
        print("\nGerando gráficos de distribuição para colunas numéricas...")
        self.plot_numeric_distributions()