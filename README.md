# `<Conjunto de dados de exercise>`
[![Netlify Status](https://api.netlify.com/api/v1/badges/04ce011c-a1fd-4085-a2db-e7d2ab4aaf9e/deploy-status)](https://app.netlify.com/sites/dainty-froyo-9ce610/deploys)
<p align="center">
  <img src="https://github.com/matt-balda/avanti-bootcamp-cdd/assets/94808306/ceef18cb-e425-4f8b-84fa-82642b53c419" alt="output-onlinepngtools" width="600" height="300"/>
</p>

### Contexto

Um grupo de pessoas é levado e colocado em um experimento. O objetivo deste experimento é medir a pulsação das pessoas durante suas ações, dependendo se elas consomem gordura durante a dieta.

### Progresso

1. Análise exploratória do conjunto de dados
2. Tratamento de dados discrepantes e outliers
3. Normalização/transformação de dados
4. Separação de variáveis previsoras e classe
5. Aprendizado de máquina e treinamento

### Justificativa

Trabalhar com a metodologia CRISP-DM no conjunto de dados, usar aprendizado supervisionado para classificar o tipo de dieta `diet`

### Graphical abstract

[ ]  É desejável que também se insira um [graphical abstract](https://www.elsevier.com/authors/tools-and-resources/visual-abstract).

## Desenvolvedor

- [Mateus Balda Mota](https://github.com/matt-balda)

## Instruções

### Requisitos

| Ferramenta | Versão          |
|------------|-----------------|
| Git        | -               |
| Python     | 3.10.*          |
| Poetry     | `1.1.13` ou superior |

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
