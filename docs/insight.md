# Início

## Perguntas de partida e hipóteses

### 1. Existem dados faltantes, se sim quantos e em quais variáveis?

   **Resp:** Não existe dados faltantes no conjunto de dados

### 2. Qual a distribuição dos dados (variável por variável)?

   **Resp:**

- Há 90 observações no conjunto de dados.
- Diet existem duas categorias (low fat, no fat) e Kind existem três categorias (rest, walking e running)
- A dieta mais comum é "no fat", com 45 instâncias.
- A atividade mais comum é "rest", com 30 instâncias.
- O pulso médio é de aproximadamente 99.7, variando de 80 a 150.
- O tempo médio é de aproximadamente 15.33, variando de 1 a 30.

#### 2.1 Distribuição das variáveis qualitativas

**Resp:**

- A diet está uniforme nas duas categorias
- O kind está uniforme nas três categorias

#### 2.2 Distribuição das variáveis quantitativas

**Resp:**

- A distribuição da variável id do voluntário para cada 1 repete 3 vezes, está uniformemente distribuída.
- A distribuição da pulse tem valores mais frequentes próximos do 91.
- A distribuição de time tem três modas, 1, 15 e 30 estão uniformemente distribuída em número de frequência.

### 3. Existe alguma relação entre o tipo de dieta e a pulsação dos voluntários durante diferentes tipos de atividades físicas?

**Resp:**

- No eixo y com pulse na categoria 'no fat' o tipo de atividade corrida demonstra uma mediana e uma máxima maior que as demais categorias
- Na categoria 'low fat' os tipos de atividade estão com as medianas aparentemente próximas, tirando a corrida apresenta uma pulsação maior e 1 outlier

### 4. Há alguma diferença na pulsação dos voluntários durante diferentes tipos de atividades físicas, considerando o tempo gasto?

**Resp:**

- Quando o tempo está em 1min, a pulsação dos diferentes tipos de atividades ficam pouco dispersos, correndo e caminhando são semelhantes
- Quando o tempo está em 15min, a pulsação para o tipo de atividade 'correndo' aumenta e fica mais disperso
- Quando o tempo está em 30min, a pulsação para o tipo de atividade 'correndo' fica mais elevado comparado aos outros, acima 110

### 5. Pulsação dos voluntários varia entre os diferentes tipos de dieta, independentemente do tipo de atividade física?

**Resp:**

- Para as duas categorias 'no fat' e 'low fat' em média para taxa metabólica há pouca diferença

### 6. Existe alguma correlação entre o tempo gasto em atividades físicas e a pulsação dos voluntários?

**Resp:**

- Existe uma correlação fraca positiva entre tempo gasto e pulsação

## Insights

Com a ajuda das visualizações criadas, bem como da análise em relação ao dicionário de dados, as informações mais relevantes que conseguimos adquirir são:

1) **Diferenças nas dietas e atividades:**

Parece haver uma tendência de que a categoria 'no fat' seja mais prevalente em todas as atividades (rest, walking e running), indicando possivelmente uma preferência dos participantes por essa dieta.

Para a categoria 'no fat', a atividade de corrida parece resultar em uma pulsação média e máxima mais elevada em comparação com as outras atividades.

Na categoria 'low fat', as medianas das pulsação parecem ser mais semelhantes entre as diferentes atividades, tirando a corrida apresenta uma pulsação maior e 1 outlier

2) **Distribuição do Tempo:**

O tempo gasto em minutos parece estar uniformemente distribuído tanto para a categoria 'no fat' quanto para a 'low fat', com o tempo de 1, 15 e 30 minutos sendo igualmente frequente.

Entretanto, quando o tempo é de 30 minutos, parece haver um aumento significativo na pulsação para a atividade de corrida, com valores acima de 110.

3) **Variação da pulsação com o tempo:**

Para um tempo de 1 minuto, as pulsações para correr e caminhar são semelhantes.

Com um tempo de 15 minutos, a pulsação para correr aumenta e se torna mais dispersa, sugerindo um maior esforço metabólico durante essa atividade em comparação com caminhar e descansar.

Quando o tempo é de 30 minutos, a pulsação para correr é significativamente maior do que para as outras atividades, indicando uma maior demanda metabólica durante corridas mais longas.

4) **Comparação entre dietas:**

Em média, parece haver pouca diferença na pulsação entre as categorias 'no fat' e 'low fat'.

A distribuição uniforme das dietas sugere que os participantes foram aleatoriamente atribuídos às diferentes dietas, o que é positivo para a validade dos resultados.

5) **Correlação entre tempo e pulsação:**

Existe uma correlação fraca positiva entre o tempo gasto em uma atividade e a pulsação, o que significa que, em geral, quanto mais tempo um voluntário gasta em uma atividade, maior é sua pulsação. No entanto, essa relação não é muito forte.
