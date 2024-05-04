# `<Conjunto de dados de exercise>`

### Contexto

Um grupo de pessoas é levado e colocado em um experimento. O objetivo deste experimento é medir a pulsação das pessoas durante suas ações, dependendo se elas consomem gordura durante a dieta.

### Progresso

1. Análise exploratória do conjunto de dados
2. Tratamento de dados discrepantes e outliers
3. Normalização/transformação de dados
4. Separação de variáveis previsoras e classe
5. Aprendizado de máquina e treinamento

### Justificativa

Trabalhar com a metodologia CRISP-DM no conjunto de dados, usar aprendizado supervisionado para classificar um tipo de atividade `kind`

### Graphical abstract

[ ]  É desejável que também se insira um [graphical abstract](https://www.elsevier.com/authors/tools-and-resources/visual-abstract).

## Desenvolvedor

- [Mateus Balda Mota](https://github.com/matt-balda)

## Funcionalidades

Essa template foi inicialmente baseado no [template de ciência de dados do cookiecutter](https://drivendata.github.io/cookiecutter-data-science/), a template tem as seguintes características:

- Utilização do arquivo `pyproject.toml` como centralizador de dependências;
- Configuração para criação de aplicação `streamlit`;
- Utilização de [jupyter notebooks](https://jupyter.org/) para arquivos de análise;
- Documentação com o [mkdocs](https://www.mkdocs.org/) ([material design](https://squidfunk.github.io/mkdocs-material/) theme)

## Instruções

### Requisitos

- git
- Python 3.10.*
- Poetry `1.1.13` ou superior

É aconselhável o uso do `pyenv` para o gerenciamento de versões do Python.

### Execução

Navegar até a pasta local, usando o comando :

```
cd REPOSITORIO
```

Instalar as dependências do projeto utilizando o comando:

```
poetry install
```

Ativar o ambiente virtual criado pelo Poetry utilizando o comando:

```
poetry shell
```


### Organização de diretórios

```
.
├── data/              # Diretório contendo todos os arquivos de dados
│   ├── external/      # Arquivos de dados de fontes externas
│   ├── interim/       # Arquivos de dados intermediários
│   ├── processed/     # Arquivos de dados processados
│   └── raw/           # Arquivos de dados originais, imutáveis
├── docs/              # Documentação gerada através da biblioteca mkdocs
├── models/            # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/         # Diretório contendo todos os notebooks utilizados nos passos
├── references/        # Dicionários de dados, manuais e todo o material exploratório
├── src/               # Código fonte utilizado nesse projeto
│   ├── data/          # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/    # Classes e funções utilizadas para implantação do modelo
│   └── model/         # Classes e funções utilizadas para modelagem
├── app.py             # Arquivo com o código da aplicação do streamlit
├── Procfile           # Arquivo de configuração do heroku
├── pyproject.toml     # Arquivo de dependências para reprodução do projeto
├── poetry.lock        # Arquivo com sub-dependências do projeto principal
├── README.md          # Informações gerais do projeto
└── tasks.py           # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```
