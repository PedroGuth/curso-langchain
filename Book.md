# 🚀 **LANGCHAIN: O GUIA COMPLETO PARA IA QUE FUNCIONA**

*Por Pedro Guth - Seu instrutor descontraído de programação*

---

## **📚 ÍNDICE**

1. [🎯 **INTRODUÇÃO**](#introdução)
2. [🔧 **SETUP E CONFIGURAÇÃO**](#setup-e-configuração)
3. [💬 **PROMPTS - A ARTE DE FALAR COM IA**](#prompts)
4. [🔗 **CHAINS - CONECTANDO AS PEÇAS**](#chains)
5. [🧠 **MEMORY - LEMBRANDO DAS CONVERSAS**](#memory)
6. [🤖 **AGENTS - OS FUNCIONÁRIOS INTELIGENTES**](#agents)
7. [📄 **DOCUMENT LOADERS - IA QUE LÊ TUDO**](#document-loaders)
8. [🔍 **RAG - IA QUE SABE O QUE NÃO SABE**](#rag)
9. [🚀 **PROJETOS PRÁTICOS**](#projetos-práticos)
10. [🌐 **DEPLOY E PRODUÇÃO**](#deploy)
11. [🚀 **TÓPICOS AVANÇADOS**](#tópicos-avançados)

---

## **🎯 INTRODUÇÃO**

### **Tá, mas o que é LangChain mesmo?**

Imagina que você é um pedreiro e tem um monte de tijolos, cimento, areia e ferramentas espalhadas pelo terreno. Você **pode** construir uma casa, mas vai ser um trabalho do caralho e vai demorar uma eternidade.

Agora imagina que alguém te dá um **kit de construção** com tudo organizado, instruções claras e até uns moldes prontos. Muito mais fácil, né?

**LangChain é exatamente isso para IA!** 🧱

Sem LangChain, você tem que:
- Conectar APIs manualmente
- Gerenciar memória de conversas
- Implementar prompts do zero
- Fazer parsing de respostas
- E mais um monte de coisa chata

Com LangChain, você tem **componentes prontos** que se encaixam como peças de Lego. É tipo ter um **"Lego da IA"** - você junta as peças e faz coisas incríveis sem reinventar a roda.

### **Por que LangChain é tipo um "pedreiro inteligente"?**

LangChain não é só uma biblioteca, é um **framework completo** que te ajuda a:

1. **Organizar prompts** (como ter receitas de bolo prontas)
2. **Conectar diferentes IAs** (como ter um tradutor que fala com um analista)
3. **Lembrar de conversas** (como um garçom que nunca esquece seu pedido)
4. **Usar ferramentas externas** (como dar superpoderes para a IA)
5. **Processar documentos** (como ter um assistente que lê tudo pra você)

### **ChatGPT vs LangChain - A Diferença na Prática**

**ChatGPT**: É como ter um amigo super inteligente, mas que só pode conversar. Ele não pode:
- Acessar internet
- Executar código
- Lembrar de conversas antigas
- Conectar com outros sistemas

**LangChain**: É como ter um **exército de amigos inteligentes** cada um com uma especialidade, e você é o chefe que coordena tudo!

**💡 Dica do Pedro**: LangChain é especialmente útil quando você quer fazer algo mais complexo que uma simples conversa. É tipo a diferença entre pedir um Uber e ter um motorista particular que também é seu assistente pessoal.

---

## **🔧 SETUP E CONFIGURAÇÃO**

### **🎯 Por que Google Colab?**

O Google Colab é **perfeito** para aprender LangChain porque:
- ✅ **100% gratuito**
- ✅ **Sem instalação** - funciona no navegador
- ✅ **GPU gratuita** disponível
- ✅ **Compartilhamento fácil**
- ✅ **Backup automático** no Google Drive

### **🆓 Opções Disponíveis no Colab:**

#### **1. 🎭 Mock LLM (Recomendado para Iniciantes)**
- ✅ **Funciona imediatamente**
- ✅ **100% gratuito**
- ✅ **Respostas simuladas realistas**
- ✅ **Perfeito para aprender conceitos**

#### **2. 🤖 Google AI Studio (Recomendado para o projeto)**
- ✅ **Funciona imediatamente**
- ✅ **100% gratuito**
- ✅ **Respostas rápidas**
- ✅ **Perfeito para o curso**

#### **3. 🌐 Hugging Face (Modelos Reais)**
- ✅ **30.000 requisições/mês gratuitas**
- ✅ **Modelos reais de IA**
- ✅ **Fácil configuração**
- ✅ **Boa qualidade**

#### **4. 🔑 OpenAI (Para Quem Quiser)**
- ✅ **Melhor qualidade**
- ✅ **Modelos mais avançados**
- ❌ **Custo por uso**
- ❌ **Precisa de API key**

### **🔧 Instalação das Dependências**

```python
# Instalando as dependências necessárias
!pip install --quiet langchain openai python-dotenv
!pip install --quiet langchain-community langchain-core
!pip install --quiet --upgrade langchain-huggingface transformers sentencepiece torch
!pip install --quiet huggingface_hub
!pip install --quiet langchain-openai openai
!pip install --quiet langchain-google-genai
!pip install --quiet langchain-huggingface

# Para document loaders
!pip install --quiet pypdf python-docx beautifulsoup4 requests youtube-transcript-api

# Para vector stores
!pip install --quiet chromadb faiss-cpu

# Para agents e ferramentas
!pip install --quiet wikipedia duckduckgo-search

# Para deploy e interfaces
!pip install --quiet streamlit gradio fastapi uvicorn

# Para processamento de dados
!pip install --quiet pandas numpy matplotlib seaborn
```

### **💰 Comparação de Custos no Colab**

| Opção | Custo | Limites | Qualidade | Facilidade |
|-------|-------|---------|-----------|------------|
| **Mock LLM** | $0 | Nenhum | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Hugging Face** | $0 | 30K/mês | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Google AI Studio** | $0 | 20K/mês | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **OpenAI** | ~$5-20 | Sem limite | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**💡 Dica do Pedro**: Comece com Mock LLM para aprender os conceitos. Quando estiver confortável, migre para Google AI Studio ou OpenAI para respostas reais!

---

## **💬 PROMPTS - A ARTE DE FALAR COM IA**

### **Tá, mas o que é um Prompt?**

Imagina que você está em um restaurante. Se você disser "quero comida", o garçom vai ficar perdido. Mas se você disser "quero um X-Burger com batata frita e Coca-Cola", aí sim ele sabe exatamente o que trazer.

**Prompt é exatamente isso!** É a forma como você "pede" as coisas para a IA. 🍔

**Prompt ruim**: "Escreve algo sobre programação"
**Prompt bom**: "Escreve um artigo de 300 palavras sobre Python para iniciantes, com exemplos práticos e linguagem simples"

A diferença é **ABISMAL**! É como a diferença entre pedir "um carro" e pedir "um Honda Civic 2023, cor prata, automático, com ar condicionado".

### **Por que Prompts Importam Tanto?**

**Sem bons prompts**: A IA fica perdida, responde coisas genéricas, não entende o que você quer
**Com bons prompts**: A IA vira seu assistente pessoal, entende exatamente o que você precisa

É como a diferença entre ter um **estagiário perdido** e um **funcionário experiente**! 😅

### **Regras de Ouro para Prompts Bons** 📋

1. **Seja específico** - Não deixe a IA adivinhar
2. **Defina o formato** - Como você quer a resposta
3. **Dê contexto** - Explique o que você precisa
4. **Use exemplos** - Mostre o que você quer
5. **Defina o tom** - Formal, informal, técnico, etc.

**💡 Dica do Pedro**: Pense que você está explicando para um **estagiário muito inteligente, mas que não lê sua mente**!

### **Templates de Prompts - Como Ter Receitas Prontas**

Templates são como **receitas de bolo** que você pode reutilizar. Em vez de escrever o prompt do zero toda vez, você cria um modelo e só muda os ingredientes.

**Exemplo prático**:
- **Sem template**: Escrever o prompt completo toda vez
- **Com template**: "Traduza {texto} do {idioma_origem} para {idioma_destino}"

É como ter um **moldinho de bolo** - você só muda os ingredientes, mas a forma é sempre a mesma! 🍰

```python
from langchain.prompts import PromptTemplate

# Template para tradução
template_traducao = PromptTemplate(
    input_variables=["texto", "idioma_origem", "idioma_destino"],
    template="""
    Traduza o seguinte texto do {idioma_origem} para {idioma_destino}:

    TEXTO: {texto}

    INSTRUÇÕES:
    - Mantenha o tom e estilo original
    - Preserve a formatação
    - Seja preciso e natural
    - Responda apenas com a tradução
    """
)
```

### **Few-Shot Examples - Ensinando com Exemplos**

Few-shot examples são como **mostrar exemplos** para a IA antes de pedir algo. É como ensinar alguém a cozinhar mostrando como fazer o prato primeiro.

**Analogia**: Se você quer que alguém aprenda a fazer bolo, você:
1. **Mostra** como fazer um bolo
2. **Explica** cada passo
3. **Deixa** a pessoa fazer sozinha

Com IA é a mesma coisa! 🎂

### **Chain of Thought - Pensando em Voz Alta**

Chain of Thought é como fazer a IA **pensar em voz alta**. Em vez de dar a resposta direta, ela explica o processo de pensamento.

**Por que isso é útil?**
- **Transparência**: Você vê como a IA chegou na resposta
- **Debugging**: Fica mais fácil identificar erros
- **Aprendizado**: Você entende o processo
- **Confiança**: Você confia mais na resposta

É como ter um **professor que explica o passo a passo** em vez de só dar a resposta! 🧠

---

## **🔗 CHAINS - CONECTANDO AS PEÇAS**

### **Tá, mas o que são Chains?**

Imagina uma **linha de produção de uma fábrica**. Cada máquina faz uma coisa específica:
- Máquina 1: Corta o metal
- Máquina 2: Dobra o metal
- Máquina 3: Pinta o metal
- Máquina 4: Embalha o produto

O produto passa por cada máquina **em sequência** e sai pronto no final.

**Chains são exatamente isso para IA!** 🏭

**Chain** = Sequência de operações onde **uma coisa leva à outra**. É como ter um **pipeline** de processamento.

### **Por que Chains são Poderosas?**

**Sem Chains**: Você tem que fazer cada coisa manualmente, uma por vez
**Com Chains**: Você conecta tudo e deixa rolar automaticamente

É como a diferença entre **fazer cada prato individualmente** e ter uma **linha de produção**! 🍽️

### **LLMChain - A Chain Mais Básica**

LLMChain é como a **máquina mais simples** da nossa linha de produção. Ela pega um prompt, envia para a IA e retorna a resposta.

É como ter um **funcionário que só faz uma tarefa específica**:

```python
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Template para tradução
template_traducao = PromptTemplate(
    input_variables=["texto"],
    template="Traduza o seguinte texto para português: {texto}"
)

# NOVO: Usar operador pipe em vez de LLMChain
chain_traducao = template_traducao | llm

# Executar
resposta = chain_traducao.invoke({"texto": "Hello, how are you?"})
print(resposta.content)
```

### **SimpleSequentialChain - Conectando Múltiplas Chains**

Agora vamos conectar **múltiplas máquinas** na nossa linha de produção! SimpleSequentialChain é como ter várias máquinas conectadas onde **a saída de uma é a entrada da próxima**.

**Analogia**: É como uma **linha de produção de pizza**:
1. **Máquina 1**: Faz a massa
2. **Máquina 2**: Adiciona o molho
3. **Máquina 3**: Coloca os ingredientes
4. **Máquina 4**: Assa a pizza

Cada máquina pega o resultado da anterior e adiciona sua parte! 🍕

```python
# Chain 1: Análise de Sentimento
template_sentimento = PromptTemplate(
    input_variables=["texto"],
    template="""
    Analise o sentimento do seguinte texto e responda apenas com:
    - POSITIVO
    - NEGATIVO
    - NEUTRO

    TEXTO: {texto}
    """
)

chain_sentimento = template_sentimento | llm

# Chain 2: Geração de Resposta
template_resposta = PromptTemplate(
    input_variables=["sentimento"],
    template="""
    Com base no sentimento {sentimento}, gere uma resposta apropriada:

    - Se POSITIVO: Responda com entusiasmo e otimismo
    - Se NEGATIVO: Responda com empatia e sugestões de melhoria
    - Se NEUTRO: Responda de forma equilibrada e informativa

    Use linguagem informal e seja como o Pedro Guth.
    """
)

chain_resposta = template_resposta | llm

# Conectando as Chains em sequência
chain_completa = chain_sentimento | chain_resposta
```

### **SequentialChain - Chains com Múltiplas Entradas e Saídas**

SequentialChain é como ter uma **fábrica mais complexa** onde:
- Você pode ter **múltiplas entradas**
- Você pode ter **múltiplas saídas**
- As Chains podem **compartilhar informações**

**Analogia**: É como uma **cozinha de restaurante** onde:
- Você tem vários ingredientes (entradas)
- Vários chefs trabalham (chains)
- Vários pratos saem (saídas)
- Os chefs compartilham informações entre si

### **RouterChain - O Garçom Inteligente**

RouterChain é como ter um **garçom muito inteligente** que:
1. **Analisa o pedido** do cliente
2. **Decide** qual chef especializado deve preparar
3. **Envia** o pedido para o chef certo
4. **Retorna** o prato pronto

**Analogia**: É como um **sistema de roteamento** que decide qual caminho seguir baseado no conteúdo.

```python
# Especialista em tecnologia
tech_prompt = PromptTemplate(
    input_variables=["pergunta"],
    template="""
    Você é um especialista em tecnologia. Responda à pergunta:

    PERGUNTA: {pergunta}

    Use linguagem técnica mas acessível. Seja como o Pedro Guth explicando.
    """
)
chain_tech = tech_prompt | llm

# Especialista em culinária
culinaria_prompt = PromptTemplate(
    input_variables=["pergunta"],
    template="""
    Você é um chef de cozinha experiente. Responda à pergunta:

    PERGUNTA: {pergunta}

    Use linguagem culinária e dê dicas práticas. Seja como o Pedro Guth na cozinha.
    """
)
chain_culinaria = culinaria_prompt | llm

# Router (o garçom inteligente)
router_prompt = PromptTemplate(
    input_variables=["pergunta"],
    template="""
    Analise a pergunta e decida qual especialista deve responder:

    PERGUNTA: {pergunta}

    ESPECIALISTAS DISPONÍVEIS:
    - tecnologia: computadores, programação, apps, internet
    - culinaria: comida, receitas, cozinha, restaurantes

    Responda apenas com: tecnologia ou culinaria.
    """
)

router_chain = router_prompt | llm
```

---

## **🧠 MEMORY - LEMBRANDO DAS CONVERSAS**

### **Tá, mas o que é Memory?**

Imagina que você está conversando com um **garçom muito bom** vs um **garçom com amnésia**:

**Garçom com amnésia**:
- Você: "Quero um café"
- Garçom: "Aqui está seu café"
- Você: "Lembra que eu gosto sem açúcar?"
- Garçom: "Desculpe, não me lembro de você..." 😅

**Garçom com boa memória**:
- Você: "Quero um café"
- Garçom: "Aqui está seu café sem açúcar, como sempre!"
- Você: "Perfeito! E lembra que eu gosto quente?"
- Garçom: "Claro! Extra quente, como da última vez!" 😊

**Memory é exatamente isso!** É como dar **memória** para a IA, para ela lembrar do que vocês conversaram antes.

### **Por que Memory é Importante?**

**Sem Memory**: A IA esquece tudo a cada pergunta. É como conversar com alguém que tem Alzheimer - você tem que explicar tudo de novo.

**Com Memory**: A IA lembra do contexto, suas preferências, o que vocês falaram antes. É como ter um **amigo que nunca esquece**!

### **Tipos de Memory**

1. **ConversationBufferMemory** - Lembra de tudo (como uma vó com boa memória)
2. **ConversationSummaryMemory** - Faz resumos (como um assistente que anota)
3. **VectorStoreMemory** - Lembra por similaridade (como um cérebro organizado)
4. **EntityMemory** - Lembra de pessoas/coisas específicas (como um CRM)

### **ConversationBufferMemory - A Vó com Boa Memória**

ConversationBufferMemory é como ter uma **vó com memória de elefante** - ela lembra de **TUDO** que vocês conversaram, palavra por palavra.

**Vantagens**:
- Lembra de tudo
- Contexto completo
- Precisão total

**Desvantagens**:
- Pode ficar pesado com conversas longas
- Consome mais tokens
- Pode ficar confuso com muito contexto

```python
from langchain.memory import ConversationBufferMemory

# Criando ConversationBufferMemory
memory = ConversationBufferMemory()

# Usar memory diretamente com as mensagens
memory.save_context({"input": "Olá!"}, {"output": "Oi! Como vai?"})

# Carregar contexto anterior
chat_history = memory.load_memory_variables({})

# Criar mensagem com contexto
if chat_history.get("history"):
    mensagem_completa = f"Histórico: {chat_history['history']}\n\nPergunta atual: {pergunta}"
else:
    mensagem_completa = pergunta

# Enviar para o LLM
response = llm.invoke([HumanMessage(content=mensagem_completa)])

# Salvar na memory
memory.save_context({"input": pergunta}, {"output": response.content})
```

### **ConversationSummaryMemory - O Assistente que Anota**

ConversationSummaryMemory é como ter um **assistente que faz anotações** durante a reunião. Em vez de lembrar de tudo palavra por palavra, ele faz **resumos inteligentes**.

**Analogia**: É como a diferença entre:
- **Vó com boa memória**: Lembra de tudo, mas pode ficar confusa com muita informação
- **Assistente que anota**: Faz resumos organizados, mantém o essencial

### **Vantagens da SummaryMemory**

1. **Mais eficiente** - Usa menos tokens
2. **Mais organizado** - Informações resumidas
3. **Melhor para conversas longas** - Não fica pesado
4. **Foco no essencial** - Mantém o que importa

```python
from langchain.memory import ConversationSummaryMemory

# Criando ConversationSummaryMemory
summary_memory = ConversationSummaryMemory(
    llm=llm,  # Modelo que vai fazer os resumos
    max_token_limit=1000  # Limite de tokens para o resumo
)

# Usar memory diretamente
summary_memory.save_context({"input": "Olá!"}, {"output": "Oi! Como vai?"})
resumo = summary_memory.load_memory_variables({})
```

### **Sistema de Chatbot com Memory Completo**

Agora vamos criar um **chatbot mais avançado** que combina diferentes tipos de memory. É como ter um **assistente pessoal inteligente**!

```python
from langchain.memory import ConversationSummaryBufferMemory

# Memory híbrida: combina buffer e summary
memory_avancada = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=2000,  # Limite maior para conversas mais longas
    return_messages=True
)

# Template para assistente pessoal
template_assistente = PromptTemplate(
    input_variables=["history", "input"],
    template="""
    Você é o Pedro, um assistente pessoal descontraído e útil.

    HISTÓRICO DA CONVERSA:
    {history}

    USUÁRIO: {input}

    INSTRUÇÕES:
    - Use o histórico para personalizar suas respostas
    - Lembre-se de informações importantes sobre o usuário
    - Seja descontraído, use analogias e piadas leves
    - Fale como o Pedro Guth
    - Seja útil e prestativo
    """
)

# Usar operador pipe em vez de LLMChain
chain_assistente = template_assistente | llm
```

---

## **🤖 AGENTS - OS FUNCIONÁRIOS INTELIGENTES**

### **Tá, mas o que são Agents?**

Imagina que você é um **chefe de uma empresa** e tem funcionários especializados:

**Sem Agents**: Você tem que fazer tudo sozinho - pesquisar, calcular, escrever, analisar...
**Com Agents**: Você delega para funcionários especializados que sabem usar ferramentas!

**Agent** = IA que pode **tomar decisões** e **usar ferramentas** para completar tarefas.

### **Por que Agents são Poderosos?**

**Sem Agents**: IA só conversa, não pode fazer ações
**Com Agents**: IA pode pesquisar, calcular, executar código, etc.

É como a diferença entre **conversar com alguém** e **ter um assistente que pode usar computador, calculadora, internet...**

### **Criando Nossa Primeira Ferramenta**

Vamos criar um **agente de pesquisa** que pode buscar informações na internet:

```python
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import Tool
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

# Ferramenta de pesquisa
search_tool = DuckDuckGoSearchRun()

# Criar ferramentas com descrição
tools = [
    Tool(
        name="Pesquisa na Internet",
        func=search_tool.run,
        description="Use para buscar informações atualizadas na internet"
    )
]

# Memory para o agente
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Template para o agente
prompt = ChatPromptTemplate.from_messages([
    ("system", "Você é um assistente útil que pode pesquisar na internet."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Criar agente com sintaxe moderna
agent = create_openai_functions_agent(llm, tools, prompt)

# Executor do agente
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    memory=memory,
    verbose=True
)
```

### **Ferramentas Customizadas - Swiss Army Knife da IA**

Vamos criar ferramentas customizadas. É como dar **ferramentas específicas** para cada funcionário:

```python
from langchain.tools import BaseTool
from typing import Optional
import math

# Ferramenta de cálculo
class CalculadoraTool(BaseTool):
    name = "calculadora"
    description = "Use para fazer cálculos matemáticos"

    def _run(self, query: str) -> str:
        try:
            # Avalia expressão matemática com segurança
            allowed_names = {
                'abs': abs, 'round': round, 'min': min, 'max': max,
                'sum': sum, 'pow': pow, 'sqrt': math.sqrt
            }
            result = eval(query, {"__builtins__": {}}, allowed_names)
            return f"Resultado: {result}"
        except Exception as e:
            return f"Erro no cálculo: {e}"

# Ferramenta de análise de texto
class AnalisadorTextoTool(BaseTool):
    name = "analisador_texto"
    description = "Use para analisar textos (contar palavras, caracteres, etc.)"

    def _run(self, texto: str) -> str:
        palavras = len(texto.split())
        caracteres = len(texto)
        linhas = len(texto.split('\n'))

        return f"Análise do texto:\n- Palavras: {palavras}\n- Caracteres: {caracteres}\n- Linhas: {linhas}"
```

### **Agente Financeiro - Tomada de Decisão Inteligente**

Vamos criar um **agente financeiro** que pode analisar investimentos e dar conselhos:

```python
# Ferramenta de análise financeira
class AnaliseFinanceiraTool(BaseTool):
    name = "analise_financeira"
    description = "Use para analisar investimentos e dar conselhos financeiros"

    def _run(self, pergunta: str) -> str:
        # Simulação de análise financeira
        if "cdb" in pergunta.lower():
            return "CDB é um investimento de renda fixa seguro. Rentabilidade: 100-110% do CDI. Ideal para conservadores."
        elif "ações" in pergunta.lower():
            return "Ações são investimentos de renda variável. Maior risco, maior potencial de retorno. Ideal para arrojados."
        elif "tesouro" in pergunta.lower():
            return "Tesouro Direto é o investimento mais seguro do Brasil. Garantido pelo governo federal."
        else:
            return "Para investimentos, considere seu perfil de risco e objetivos. Diversificação é fundamental."

# Ferramenta de cálculo de juros compostos
class JurosCompostosTool(BaseTool):
    name = "juros_compostos"
    description = "Use para calcular juros compostos e projeções financeiras"

    def _run(self, query: str) -> str:
        try:
            # Exemplo: calcular juros compostos
            if "calcular" in query.lower():
                # Simulação simples
                principal = 1000
                taxa = 0.01  # 1% ao mês
                tempo = 12   # 12 meses

                montante = principal * (1 + taxa) ** tempo
                return f"Investimento de R$ {principal} por {tempo} meses a {taxa*100}% ao mês = R$ {montante:.2f}"
            else:
                return "Use 'calcular' para fazer projeções financeiras"
        except:
            return "Erro no cálculo financeiro"
```

---

## **📄 DOCUMENT LOADERS - IA QUE LÊ TUDO**

### **Tá, mas o que são Document Loaders?**

Imagina que você tem uma **biblioteca digital** que pode ler qualquer tipo de documento:

- 📄 **PDFs** - Relatórios, manuais, artigos
- 📊 **CSVs** - Dados, planilhas, estatísticas
- 🎥 **YouTube** - Vídeos, palestras, tutoriais
- 🌐 **Websites** - Páginas, blogs, notícias
- 📝 **Word** - Documentos, contratos, propostas

**Document Loaders** são como **tradutores especializados** que convertem qualquer formato em texto que a IA pode entender.

### **Por que Document Loaders são Importantes?**

**Sem Document Loaders**: IA só sabe o que você digita
**Com Document Loaders**: IA pode ler e analisar qualquer documento!

É como a diferença entre **ler apenas um livro** vs **ter acesso a uma biblioteca inteira**! 📚

### **Testando Diferentes Document Loaders**

```python
from langchain.document_loaders import (
    PyPDFLoader, 
    CSVLoader, 
    UnstructuredWordDocumentLoader,
    WebBaseLoader,
    YoutubeLoader
)
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Testando CSV Loader
csv_loader = CSVLoader('produtos.csv')
documentos_csv = csv_loader.load()

# Testando Text Loader
from langchain.document_loaders import TextLoader
text_loader = TextLoader('langchain_info.txt', encoding='utf-8')
documentos_texto = text_loader.load()

# Testando Web Loader
urls = ["https://python.org"]
web_loader = WebBaseLoader(urls)
documentos_web = web_loader.load()
```

### **Vector Stores - A Memória de Longo Prazo**

Vector Stores são como um **cérebro organizado** que:
1. **Converte texto em números** (vetores)
2. **Organiza por similaridade**
3. **Permite busca inteligente**

**Analogia**: É como ter uma **biblioteca onde os livros se organizam sozinhos** por assunto, e você pode encontrar qualquer informação rapidamente!

### **Por que Vector Stores são Importantes?**

**Sem Vector Stores**: IA esquece o que leu
**Com Vector Stores**: IA pode buscar e lembrar de qualquer informação

É como a diferença entre **ler um livro e esquecer** vs **ter uma biblioteca na cabeça**! 🧠

```python
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Text splitter para dividir documentos grandes
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # Tamanho de cada pedaço
    chunk_overlap=200,  # Sobreposição entre pedaços
    length_function=len
)

# Carregando e dividindo documentos
text_loader = TextLoader('langchain_info.txt', encoding='utf-8')
documentos = text_loader.load()

# Dividindo em pedaços menores
textos_divididos = text_splitter.split_documents(documentos)

# Criando embeddings
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

# Criando vector store
vectorstore = Chroma.from_documents(
    documents=textos_divididos,
    embedding=embeddings,
    collection_name="langchain_info"
)
```

### **Sistema de Busca Inteligente Completo**

Agora vamos criar um **sistema de busca inteligente** que combina document loaders com vector stores:

```python
class SistemaBuscaInteligente:
    def __init__(self):
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=os.getenv('OPENAI_API_KEY')
        )
        self.vectorstore = None
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
    
    def carregar_documento(self, caminho_arquivo, tipo="texto"):
        """Carrega um documento e adiciona ao vector store"""
        try:
            if tipo == "csv":
                loader = CSVLoader(caminho_arquivo)
            elif tipo == "texto":
                loader = TextLoader(caminho_arquivo, encoding='utf-8')
            else:
                return "Tipo de documento não suportado"
            
            documentos = loader.load()
            textos_divididos = self.text_splitter.split_documents(documentos)
            
            if self.vectorstore is None:
                self.vectorstore = Chroma.from_documents(
                    documents=textos_divididos,
                    embedding=self.embeddings,
                    collection_name="biblioteca_digital"
                )
            else:
                self.vectorstore.add_documents(textos_divididos)
            
            return f"✅ Documento carregado! {len(textos_divididos)} pedaços adicionados."
            
        except Exception as e:
            return f"❌ Erro: {e}"
    
    def buscar(self, query, k=3):
        """Busca documentos similares"""
        try:
            if self.vectorstore is None:
                return "❌ Nenhum documento carregado ainda."
            
            docs = self.vectorstore.similarity_search(query, k=k)
            return docs
            
        except Exception as e:
            return f"❌ Erro na busca: {e}"
```

---

## **🔍 RAG - IA QUE SABE O QUE NÃO SABE**

### **Tá, mas o que é RAG?**

Imagina que você é um **estudante muito inteligente** que está fazendo uma prova:

**Sem RAG**: Você só pode usar o que já sabe de cabeça. Se não souber, chuta ou inventa.
**Com RAG**: Você pode **consultar livros** antes de responder, garantindo que sua resposta seja precisa!

**RAG** = **Retrieval Augmented Generation**
- **Retrieval**: Busca informações relevantes
- **Augmented**: Aumenta o conhecimento da IA
- **Generation**: Gera respostas baseadas nas informações encontradas

### **Por que RAG é Revolucionário?**

**Problema tradicional**: IA só sabe o que foi treinada, não pode acessar informações atualizadas
**Solução RAG**: IA busca informações relevantes e gera respostas precisas

É como a diferença entre **um professor que só sabe o que estudou há 10 anos** vs **um professor que sempre consulta os livros mais recentes**! 📚

### **Criando Sistema RAG Básico**

```python
from langchain.chains import RetrievalQA

# Criando chain RAG
rag_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # Tipo de chain para RAG
    retriever=vectorstore.as_retriever(
        search_kwargs={"k": 3}  # Busca os 3 documentos mais relevantes
    ),
    return_source_documents=True,  # Retorna os documentos usados
    verbose=True
)

# Executando RAG
resultado = rag_chain({"query": "O que é Python e para que serve?"})
print(f"🤖 Resposta: {resultado['result']}")
print(f"📄 Documentos consultados: {len(resultado['source_documents'])}")
```

### **Sistema de Suporte Técnico com RAG**

Vamos criar um **sistema de suporte técnico inteligente** que usa RAG:

```python
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Template para suporte técnico
template_suporte = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    Você é um especialista em suporte técnico muito atencioso.
    
    Use as seguintes informações da base de conhecimento para responder:
    {context}
    
    PERGUNTA DO CLIENTE: {question}
    
    INSTRUÇÕES:
    - Responda de forma clara e didática
    - Use as informações da base de conhecimento
    - Seja prestativo e atencioso
    - Use linguagem informal como o Pedro Guth
    - Se não encontrar informação específica, seja honesto
    """
)

# Chain de suporte
chain_suporte = LLMChain(
    llm=llm,
    prompt=template_suporte
)

# Função para buscar contexto relevante
def buscar_contexto(pergunta, k=2):
    """Busca documentos relevantes para a pergunta"""
    try:
        docs = vectorstore.similarity_search(pergunta, k=k)
        contexto = "\n\n".join([doc.page_content for doc in docs])
        return contexto
    except Exception as e:
        return f"Erro na busca: {e}"

# Gerando resposta com contexto
contexto = buscar_contexto(pergunta)
resposta = chain_suporte.run({
    "context": contexto,
    "question": pergunta
})
```

### **Chatbot com RAG - Sistema Completo**

Agora vamos criar um **chatbot completo** que combina RAG com memory:

```python
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

# Memory para o chatbot
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Chatbot com RAG
chatbot_rag = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    memory=memory,
    return_source_documents=True,
    verbose=True
)

# Executando chatbot
resultado = chatbot_rag({"question": mensagem})
print(f"🤖 Chatbot: {resultado['answer'][:300]}...")

if resultado['source_documents']:
    print(f"📄 Consultou {len(resultado['source_documents'])} documentos")
```

---

## **🚀 PROJETOS PRÁTICOS**

### **Projeto 1: Chatbot para E-commerce**

Vamos criar um **chatbot inteligente para e-commerce** que:

- 🛍️ **Conhece todos os produtos**
- 💬 **Atende clientes 24/7**
- 🧠 **Lembra das preferências**
- 🔍 **Busca produtos inteligentemente**
- 💳 **Ajuda com compras**

É como ter um **vendedor digital super inteligente** que nunca dorme e conhece cada cliente! 🛒

#### **Por que este projeto é importante?**

**Problema real**: E-commerces perdem vendas por falta de atendimento
**Solução**: Chatbot que atende instantaneamente e converte vendas

É como a diferença entre **uma loja fechada** e **uma loja com vendedor 24h**! 🏪

#### **Criando Base de Produtos**

```python
produtos_ecommerce = """
CATÁLOGO DE PRODUTOS - TECHSTORE

SMARTPHONES:

iPhone 15 Pro Max
- Preço: R$ 9.999
- Categoria: Smartphone
- Marca: Apple
- Características: Tela 6.7", Chip A17 Pro, Câmera tripla 48MP
- Cores: Titânio Natural, Titânio Azul, Titânio Branco, Titânio Preto
- Capacidades: 256GB, 512GB, 1TB
- Garantia: 1 ano

Samsung Galaxy S24 Ultra
- Preço: R$ 8.999
- Categoria: Smartphone
- Marca: Samsung
- Características: Tela 6.8", Snapdragon 8 Gen 3, Câmera quádrupla 200MP
- Cores: Titânio Cinza, Titânio Preto, Titânio Violeta, Titânio Amarelo
- Capacidades: 256GB, 512GB, 1TB
- Garantia: 1 ano

NOTEBOOKS:

MacBook Pro 14" M3 Pro
- Preço: R$ 18.999
- Categoria: Notebook
- Marca: Apple
- Características: Chip M3 Pro, 14", 18GB RAM, 512GB SSD
- Cores: Space Gray, Silver
- Garantia: 1 ano

ACESSÓRIOS:

AirPods Pro 2ª Geração
- Preço: R$ 2.499
- Categoria: Fones de Ouvido
- Marca: Apple
- Características: Cancelamento de ruído ativo, Áudio espacial
- Cores: Branco
- Garantia: 1 ano

POLÍTICAS DA LOJA:

ENTREGA:
- Frete grátis para compras acima de R$ 500
- Entrega em 1-3 dias úteis
- Rastreamento em tempo real

PAGAMENTO:
- Cartão de crédito (até 12x)
- PIX (5% de desconto)
- Boleto bancário

GARANTIA:
- Todos os produtos têm garantia de fábrica
- Suporte técnico especializado
- Troca em até 7 dias

ATENDIMENTO:
- Chat 24/7
- WhatsApp: (11) 99999-9999
- Email: atendimento@techstore.com
"""
```

#### **Criando o Chatbot de E-commerce**

```python
# Carregando e processando base de produtos
from langchain.document_loaders import TextLoader

loader = TextLoader('produtos_techstore.txt', encoding='utf-8')
documentos = loader.load()

# Dividindo em pedaços menores
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
textos_divididos = text_splitter.split_documents(documentos)

# Criando vector store
embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv('OPENAI_API_KEY')
)

vectorstore = Chroma.from_documents(
    documents=textos_divididos,
    embedding=embeddings,
    collection_name="produtos_techstore"
)

# Criando memory para o chatbot
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Criando chatbot com RAG
from langchain.chains import ConversationalRetrievalChain

chatbot_ecommerce = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vectorstore.as_retriever(search_kwargs={"k": 3}),
    memory=memory,
    return_source_documents=True,
    verbose=True
)

print("🤖 Chatbot de E-commerce criado!")
print("🛍️ Vendedor digital pronto para atender!")
```

#### **Testando o Chatbot de E-commerce**

```python
conversas_teste = [
    "Olá! Estou procurando um smartphone bom para fotos.",
    "Qual a diferença entre iPhone 15 Pro Max e Samsung Galaxy S24 Ultra?",
    "Quanto custa o iPhone 15 Pro Max?",
    "Vocês têm frete grátis?",
    "Lembra do que eu estava procurando?",
    "Quais são as formas de pagamento?",
    "Preciso de um notebook para trabalho. O que você recomenda?"
]

for i, mensagem in enumerate(conversas_teste, 1):
    print(f"\n👤 Cliente {i}: {mensagem}")
    
    try:
        resultado = chatbot_ecommerce({"question": mensagem})
        print(f"🤖 Vendedor: {resultado['answer'][:300]}...")
        
        if resultado['source_documents']:
            print(f"📄 Consultou {len(resultado['source_documents'])} produtos")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print("-" * 40)
```

### **Projeto 2: Assistente de Estudos**

#### **Base de Conhecimento Acadêmica**

```python
material_estudo = """
INTRODUÇÃO À INTELIGÊNCIA ARTIFICIAL

DEFINIÇÃO E CONCEITOS BÁSICOS:

Inteligência Artificial (IA) é um campo da computação que busca criar sistemas
capazes de realizar tarefas que normalmente requerem inteligência humana.
A IA combina ciência da computação, matemática, psicologia e outras disciplinas.

HISTÓRICO DA IA:

A IA nasceu na década de 1950, com o teste de Turing proposto por Alan Turing.
O termo "Inteligência Artificial" foi cunhado em 1956 na Conferência de Dartmouth.
Desde então, a IA passou por vários "invernos" e "primaveras" de desenvolvimento.

TIPOS DE INTELIGÊNCIA ARTIFICIAL:

1. IA Fraca (Narrow AI):
   - Especializada em uma tarefa específica
   - Exemplos: Siri, Alexa, sistemas de recomendação
   - Não possui consciência ou inteligência geral

2. IA Forte (AGI - Artificial General Intelligence):
   - Inteligência geral como humanos
   - Pode realizar qualquer tarefa intelectual
   - Ainda não foi alcançada

3. Superinteligência:
   - Inteligência superior à humana
   - Conceito teórico e controverso

MACHINE LEARNING:

Machine Learning é um subcampo da IA que permite aos computadores aprender
sem serem explicitamente programados. Os algoritmos identificam padrões
nos dados para fazer previsões ou tomar decisões.

TIPOS DE MACHINE LEARNING:

1. Aprendizado Supervisionado:
   - Usa dados rotulados para treinar
   - Exemplos: classificação, regressão
   - Algoritmos: Random Forest, SVM, Redes Neurais

2. Aprendizado Não Supervisionado:
   - Encontra padrões em dados não rotulados
   - Exemplos: clustering, redução de dimensionalidade
   - Algoritmos: K-means, PCA, Autoencoders

3. Aprendizado por Reforço:
   - Aprende através de tentativa e erro
   - Usa recompensas e punições
   - Exemplos: jogos, robótica, carros autônomos

DEEP LEARNING:

Deep Learning é um subcampo do Machine Learning que usa redes neurais
com múltiplas camadas para aprender representações complexas dos dados.

CARACTERÍSTICAS:
- Múltiplas camadas de neurônios
- Aprendizado de features automático
- Requer grandes quantidades de dados
- Poder computacional significativo

APLICAÇÕES PRÁTICAS:

1. Visão Computacional:
   - Reconhecimento de imagens
   - Detecção de objetos
   - Processamento de vídeo

2. Processamento de Linguagem Natural:
   - Tradução automática
   - Análise de sentimentos
   - Chatbots inteligentes

3. Sistemas de Recomendação:
   - Netflix, Spotify, Amazon
   - Personalização de conteúdo
   - Marketing direcionado

4. Medicina e Saúde:
   - Diagnóstico por imagem
   - Descoberta de medicamentos
   - Medicina personalizada

DESAFIOS E LIMITAÇÕES:

1. Viés nos Dados:
   - Dados podem refletir preconceitos
   - Importante para justiça e equidade

2. Interpretabilidade:
   - Modelos complexos são difíceis de explicar
   - Importante para confiança e responsabilidade

3. Privacidade:
   - Coleta e uso de dados pessoais
   - Necessidade de proteção

4. Segurança:
   - Vulnerabilidades em sistemas de IA
   - Ataques adversariais

FUTURO DA IA:

O futuro da IA inclui:
- IA mais ética e responsável
- Automação de mais tarefas
- Integração com IoT e robótica
- Desenvolvimento de AGI (controverso)
- Regulamentações e políticas

CONCEITOS IMPORTANTES:

Overfitting: Modelo que memoriza dados de treino
Underfitting: Modelo muito simples para os dados
Cross-validation: Técnica para avaliar modelos
Feature Engineering: Criação de features relevantes
Hyperparameter Tuning: Otimização de parâmetros
"""

# Salvando material de estudo
with open('material_ia.txt', 'w', encoding='utf-8') as file:
    file.write(material_estudo)
```

#### **Funções Especializadas do Assistente**

```python
def gerar_resumo(texto, llm):
    """Gera resumo do material de estudo"""
    prompt = f"""
    Crie um resumo conciso e didático do seguinte texto sobre IA:
    
    {texto}
    
    O resumo deve:
    - Ser fácil de entender
    - Destacar os pontos principais
    - Usar linguagem clara
    - Ter no máximo 200 palavras
    """
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"Erro ao gerar resumo: {e}"

def criar_flashcards(texto, llm):
    """Cria flashcards para estudo"""
    prompt = f"""
    Crie 5 flashcards para estudo baseados no seguinte texto:
    
    {texto}
    
    Formato:
    Frente: [Pergunta]
    Verso: [Resposta]
    
    As perguntas devem ser claras e as respostas concisas.
    """
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"Erro ao criar flashcards: {e}"

def gerar_perguntas(texto, llm):
    """Gera perguntas de revisão"""
    prompt = f"""
    Crie 3 perguntas de revisão sobre o seguinte conteúdo:
    
    {texto}
    
    As perguntas devem:
    - Testar compreensão
    - Ser de diferentes níveis (fácil, médio, difícil)
    - Ter respostas claras
    """
    
    try:
        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content
    except Exception as e:
        return f"Erro ao gerar perguntas: {e}"
```

#### **Sistema Completo de Estudos**

```python
class AssistenteEstudos:
    def __init__(self, llm, vectorstore):
        self.llm = llm
        self.vectorstore = vectorstore
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
    
    def perguntar(self, pergunta):
        """Faz uma pergunta sobre o material"""
        try:
            # Buscando material relevante
            docs = self.vectorstore.similarity_search(pergunta, k=3)
            contexto = "\n\n".join([doc.page_content for doc in docs])
            
            # Gerando resposta
            prompt = f"""
            Você é um professor especialista em IA. Responda à pergunta do aluno
            usando o seguinte material de estudo:
            
            MATERIAL: {contexto}
            
            PERGUNTA: {pergunta}
            
            Responda de forma didática e clara, como o Pedro Guth explicando.
            """
            
            response = self.llm.invoke([HumanMessage(content=prompt)])
            return response.content
            
        except Exception as e:
            return f"Erro: {e}"
    
    def gerar_resumo_tema(self, tema):
        """Gera resumo de um tema específico"""
        try:
            docs = self.vectorstore.similarity_search(tema, k=3)
            texto = "\n\n".join([doc.page_content for doc in docs])
            return gerar_resumo(texto, self.llm)
        except Exception as e:
            return f"Erro: {e}"
    
    def criar_flashcards_tema(self, tema):
        """Cria flashcards de um tema"""
        try:
            docs = self.vectorstore.similarity_search(tema, k=2)
            texto = "\n\n".join([doc.page_content for doc in docs])
            return criar_flashcards(texto, self.llm)
        except Exception as e:
            return f"Erro: {e}"

# Criando instância do assistente
assistente = AssistenteEstudos(llm, vectorstore_estudos)
```

---

## **🎯 Módulo 9: Deploy e Produção**

### **Aula 9.1: Deploy Básico - Colocando na Rua**

#### **O que é Deploy?**

Imagina que você construiu uma **casa incrível** no seu computador:

**Sem Deploy**: A casa fica só no seu computador. Ninguém mais pode ver ou usar.
**Com Deploy**: A casa vai para a internet, todo mundo pode acessar e usar!

**Deploy** = **Colocar seu projeto na internet** para que outras pessoas possam usar.

#### **Por que Deploy é Importante?**

**Problema**: Projetos incríveis que ficam só no computador do desenvolvedor
**Solução**: Deploy para que todo mundo possa usar e se beneficiar

É como a diferença entre **ter uma receita incrível guardada** vs **abrir um restaurante**! 🍽️

### **Aula 9.2: Deploy com Streamlit - Interface Web Simples**

#### **Criando App Streamlit**

```python
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Configuração da página
st.set_page_config(
    page_title="Chatbot IA - Pedro Guth",
    page_icon="🤖",
    layout="wide"
)

# Título
st.title("🤖 Chatbot IA - Pedro Guth")
st.markdown("---")

# Sidebar com configurações
with st.sidebar:
    st.header("⚙️ Configurações")
    
    # API Key
    api_key = st.text_input(
        "🔑 OpenAI API Key",
        type="password",
        help="Sua chave da OpenAI"
    )
    
    # Modelo
    modelo = st.selectbox(
        "🤖 Modelo",
        ["gpt-3.5-turbo", "gpt-4"],
        index=0
    )
    
    # Temperature
    temperature = st.slider(
        "🌡️ Criatividade",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1
    )

# Área principal
if api_key:
    # Inicializando modelo
    llm = ChatOpenAI(
        model=modelo,
        temperature=temperature,
        api_key=api_key
    )
    
    # Chat
    st.header("💬 Conversa")
    
    # Inicializar chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Mostrar mensagens anteriores
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input do usuário
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Adicionar mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Gerar resposta
        with st.chat_message("assistant"):
            with st.spinner("🤖 Pensando..."):
                try:
                    response = llm.invoke([HumanMessage(content=prompt)])
                    st.markdown(response.content)
                    st.session_state.messages.append({"role": "assistant", "content": response.content})
                except Exception as e:
                    st.error(f"❌ Erro: {e}")
else:
    st.warning("⚠️ Configure sua API Key na sidebar para começar!")

# Footer
st.markdown("---")
st.markdown("*Desenvolvido com ❤️ por Pedro Guth*")
```

### **Aula 9.3: Deploy com Gradio - Interface Rápida**

#### **Criando Interface Gradio**

```python
import gradio as gr
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Carregando variáveis
load_dotenv()

def chatbot_gradio(message, history):
    """Função do chatbot para Gradio"""
    try:
        # Inicializando modelo
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=os.getenv('OPENAI_API_KEY')
        )
        
        # Gerando resposta
        response = llm.invoke([HumanMessage(content=message)])
        return response.content
        
    except Exception as e:
        return f"❌ Erro: {e}"

# Criando interface Gradio
demo = gr.ChatInterface(
    fn=chatbot_gradio,
    title="🤖 Chatbot IA - Pedro Guth",
    description="Chatbot inteligente desenvolvido com LangChain",
    examples=[
        ["O que é LangChain?"],
        ["Como funciona a IA?"],
        ["Me conte uma piada sobre programação"]
    ],
    theme="soft"
)

if __name__ == "__main__":
    demo.launch()
```

### **Aula 9.4: Deploy com FastAPI - API Profissional**

#### **Criando API com FastAPI**

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Carregando variáveis
load_dotenv()

# Criando app FastAPI
app = FastAPI(
    title="Chatbot IA API",
    description="API do Chatbot IA desenvolvido com LangChain",
    version="1.0.0"
)

# Modelos de dados
class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = "gpt-3.5-turbo"
    temperature: Optional[float] = 0.7

class ChatResponse(BaseModel):
    response: str
    model: str
    tokens_used: Optional[int] = None

# Rota principal
@app.get("/")
async def root():
    return {"message": "Chatbot IA API - Pedro Guth"}

# Rota de chat
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Verificar API key
        api_key = os.getenv('OPENAI_API_KEY')
        if not api_key:
            raise HTTPException(status_code=500, detail="API key não configurada")
        
        # Inicializando modelo
        llm = ChatOpenAI(
            model=request.model,
            temperature=request.temperature,
            api_key=api_key
        )
        
        # Gerando resposta
        response = llm.invoke([HumanMessage(content=request.message)])
        
        return ChatResponse(
            response=response.content,
            model=request.model
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Rota de saúde
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "chatbot-ia"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### **Aula 9.5: Monitoramento e Otimização**

#### **Sistema de Monitoramento**

```python
import time
import logging
from datetime import datetime

# Configurando logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class Monitoramento:
    def __init__(self):
        self.requests = 0
        self.errors = 0
        self.start_time = datetime.now()
    
    def log_request(self, success=True):
        """Registra uma requisição"""
        self.requests += 1
        if not success:
            self.errors += 1
        
        logger.info(f"Requisição {self.requests}: {'Sucesso' if success else 'Erro'}")
    
    def get_stats(self):
        """Retorna estatísticas"""
        uptime = datetime.now() - self.start_time
        error_rate = (self.errors / self.requests * 100) if self.requests > 0 else 0
        
        return {
            "total_requests": self.requests,
            "total_errors": self.errors,
            "error_rate": f"{error_rate:.2f}%",
            "uptime": str(uptime).split('.')[0]
        }

# Função de chat com monitoramento
monitor = Monitoramento()

def chat_com_monitoramento(message):
    """Chat com monitoramento de performance"""
    start_time = time.time()
    
    try:
        # Inicializando modelo
        llm = ChatOpenAI(
            model="gpt-3.5-turbo",
            temperature=0.7,
            api_key=os.getenv('OPENAI_API_KEY')
        )
        
        # Gerando resposta
        response = llm.invoke([HumanMessage(content=message)])
        
        # Calculando tempo
        execution_time = time.time() - start_time
        
        # Logging
        logger.info(f"Resposta gerada em {execution_time:.2f}s")
        monitor.log_request(success=True)
        
        return response.content
        
    except Exception as e:
        logger.error(f"Erro: {e}")
        monitor.log_request(success=False)
        return f"❌ Erro: {e}"
```

---

## **🚀 Módulo 10: Tópicos Avançados - Indo Além**

### **Aula 10.1: LangGraph - Fluxos Complexos**

#### **O que é LangGraph?**

Imagina que você está construindo um **plano de metrô** para a IA:

**Sem LangGraph**: A IA só anda em linha reta (A → B → C)
**Com LangGraph**: A IA pode pegar diferentes linhas, fazer baldeações, voltar atrás!

**LangGraph** = **Framework para criar fluxos complexos** onde a IA pode:
- 🛤️ **Tomar decisões** sobre qual caminho seguir
- 🔄 **Fazer loops** e voltar atrás
- 🎯 **Manter estado** durante o processo
- 🚦 **Controlar fluxo** com condições

#### **Por que LangGraph é Revolucionário?**

**Problema tradicional**: Fluxos lineares e rígidos
**Solução LangGraph**: Fluxos dinâmicos e inteligentes

É como a diferença entre **um roteiro de filme fixo** vs **um jogo de RPG onde você escolhe o caminho**! 🎮

#### **Criando Nosso Primeiro LangGraph**

```python
# Instalando LangGraph
!pip install langgraph

# Importando bibliotecas
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from langchain.schema import HumanMessage

# Carregando variáveis
load_dotenv()

# Modelo
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.getenv('OPENAI_API_KEY')
)

# Definindo o estado do nosso sistema
class EstadoAtendimento(TypedDict):
    """Estado do sistema de atendimento"""
    pergunta: str
    categoria: str
    resposta: str
    acao: str
    historico: list

# Criando função para categorizar a pergunta
def categorizar_pergunta(state: EstadoAtendimento) -> EstadoAtendimento:
    """Categoriza a pergunta do cliente"""
    pergunta = state["pergunta"]
    
    # Lógica de categorização
    if any(palavra in pergunta.lower() for palavra in ["preço", "custo", "valor", "quanto"]):
        categoria = "precos"
    elif any(palavra in pergunta.lower() for palavra in ["produto", "item", "comprar", "venda"]):
        categoria = "produtos"
    elif any(palavra in pergunta.lower() for palavra in ["problema", "erro", "bug", "ajuda"]):
        categoria = "suporte"
    else:
        categoria = "geral"
    
    # Atualizando estado
    state["categoria"] = categoria
    state["historico"].append(f"Categorizado como: {categoria}")
    
    return state

# Criando funções especializadas para cada categoria
def atender_precos(state: EstadoAtendimento) -> EstadoAtendimento:
    """Atende perguntas sobre preços"""
    resposta = """
    💰 INFORMAÇÕES SOBRE PREÇOS:
    
    • iPhone 15 Pro Max: R$ 9.999
    • Samsung Galaxy S24 Ultra: R$ 8.999
    • MacBook Pro 14": R$ 18.999
    • AirPods Pro: R$ 2.499
    
    💳 Formas de pagamento:
    • Cartão de crédito (até 12x)
    • PIX (5% de desconto)
    • Boleto bancário
    
    🚚 Frete grátis para compras acima de R$ 500!
    """
    
    state["resposta"] = resposta
    state["acao"] = "informacao_precos"
    state["historico"].append("Fornecidas informações sobre preços")
    
    return state

def atender_produtos(state: EstadoAtendimento) -> EstadoAtendimento:
    """Atende perguntas sobre produtos"""
    resposta = """
    📱 NOSSOS PRODUTOS:
    
    🍎 Apple:
    • iPhone 15 Pro Max - Câmera avançada, Chip A17 Pro
    • MacBook Pro 14" - Chip M3 Pro, ideal para trabalho
    • AirPods Pro - Cancelamento de ruído ativo
    
    📱 Samsung:
    • Galaxy S24 Ultra - Câmera 200MP, S Pen
    
    💻 Outros:
    • Dell XPS 13 Plus - Notebook premium
    
    🎯 Qual produto te interessa? Posso dar mais detalhes!
    """
    
    state["resposta"] = resposta
    state["acao"] = "catalogo_produtos"
    state["historico"].append("Apresentado catálogo de produtos")
    
    return state

def atender_suporte(state: EstadoAtendimento) -> EstadoAtendimento:
    """Atende problemas e suporte"""
    resposta = """
    🛠️ SUPORTE TÉCNICO:
    
    📞 Canais de atendimento:
    • WhatsApp: (11) 99999-9999
    • Email: suporte@techstore.com
    • Chat: 24/7 (você está usando agora!)
    
    ⏰ Horário: Segunda a sexta, 8h às 18h
    
    🔧 Tipos de suporte:
    • Problemas técnicos
    • Dúvidas sobre produtos
    • Garantia e trocas
    • Instalação e configuração
    
    Como posso te ajudar hoje?
    """
    
    state["resposta"] = resposta
    state["acao"] = "suporte_tecnico"
    state["historico"].append("Fornecido suporte técnico")
    
    return state

def atender_geral(state: EstadoAtendimento) -> EstadoAtendimento:
    """Atende perguntas gerais"""
    resposta = """
    👋 OLÁ! Sou o assistente da TechStore!
    
    🛍️ Como posso te ajudar?
    
    • 💰 Informações sobre preços
    • 📱 Catálogo de produtos
    • 🛠️ Suporte técnico
    • 📞 Falar com atendente humano
    
    É só me perguntar o que você precisa!
    """
    
    state["resposta"] = resposta
    state["acao"] = "atendimento_geral"
    state["historico"].append("Fornecido atendimento geral")
    
    return state

# Criando o grafo de decisão
def criar_grafo_atendimento():
    """Cria o grafo de atendimento"""
    
    # Criando o grafo
    workflow = StateGraph(EstadoAtendimento)
    
    # Adicionando nós (estações)
    workflow.add_node("categorizar", categorizar_pergunta)
    workflow.add_node("precos", atender_precos)
    workflow.add_node("produtos", atender_produtos)
    workflow.add_node("suporte", atender_suporte)
    workflow.add_node("geral", atender_geral)
    
    # Definindo o ponto de entrada
    workflow.set_entry_point("categorizar")
    
    # Definindo as rotas (linhas do metrô)
    def rotear_por_categoria(state: EstadoAtendimento) -> str:
        """Decide qual rota seguir baseado na categoria"""
        categoria = state["categoria"]
        return categoria
    
    # Conectando as rotas
    workflow.add_conditional_edges(
        "categorizar",
        rotear_por_categoria,
        {
            "precos": "precos",
            "produtos": "produtos",
            "suporte": "suporte",
            "geral": "geral"
        }
    )
    
    # Conectando ao final
    workflow.add_edge("precos", END)
    workflow.add_edge("produtos", END)
    workflow.add_edge("suporte", END)
    workflow.add_edge("geral", END)
    
    # Compilando o grafo
    app = workflow.compile()
    
    return app

# Testando o LangGraph
app_atendimento = criar_grafo_atendimento()

perguntas_teste = [
    "Quanto custa o iPhone 15 Pro Max?",
    "Quais produtos vocês têm da Apple?",
    "Meu iPhone não está carregando, o que faço?",
    "Olá! Como vocês estão?"
]

for i, pergunta in enumerate(perguntas_teste, 1):
    print(f"\n❓ Pergunta {i}: {pergunta}")
    
    try:
        # Estado inicial
        estado_inicial = {
            "pergunta": pergunta,
            "categoria": "",
            "resposta": "",
            "acao": "",
            "historico": []
        }
        
        # Executando o grafo
        resultado = app_atendimento.invoke(estado_inicial)
        
        print(f"🏷️  Categoria: {resultado['categoria']}")
        print(f"🎯 Ação: {resultado['acao']}")
        print(f"🤖 Resposta: {resultado['resposta'][:200]}...")
        print(f"📋 Histórico: {resultado['historico']}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print("-" * 40)
```

### **Aula 10.2: Integração com APIs Externas**

#### **Sistema de Integração com APIs**

```python
import requests
import json
from datetime import datetime

class SistemaIntegracao:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"  # API de exemplo
    
    def buscar_usuarios(self):
        """Busca usuários da API externa"""
        try:
            response = requests.get(f"{self.base_url}/users")
            return response.json()
        except Exception as e:
            return f"Erro ao buscar usuários: {e}"
    
    def buscar_posts(self, user_id=1):
        """Busca posts de um usuário"""
        try:
            response = requests.get(f"{self.base_url}/posts?userId={user_id}")
            return response.json()
        except Exception as e:
            return f"Erro ao buscar posts: {e}"
    
    def criar_post(self, titulo, corpo, user_id=1):
        """Cria um novo post"""
        try:
            data = {
                "title": titulo,
                "body": corpo,
                "userId": user_id
            }
            response = requests.post(f"{self.base_url}/posts", json=data)
            return response.json()
        except Exception as e:
            return f"Erro ao criar post: {e}"

# Criando ferramenta de API para LangChain
from langchain.tools import BaseTool
from typing import Optional

class APITool(BaseTool):
    name = "api_externa"
    description = "Use para acessar dados de APIs externas"
    sistema: SistemaIntegracao = None
    
    def _run(self, query: str) -> str:
        """Executa consultas na API externa"""
        try:
            if "usuários" in query.lower() or "user" in query.lower():
                usuarios = self.sistema.buscar_usuarios()
                return f"Usuários encontrados: {len(usuarios)}. Primeiro usuário: {usuarios[0]['name']}"
            
            elif "posts" in query.lower():
                posts = self.sistema.buscar_posts()
                return f"Posts encontrados: {len(posts)}. Primeiro post: {posts[0]['title']}"
            
            else:
                return "Comando não reconhecido. Use 'usuários' ou 'posts'."
                
        except Exception as e:
            return f"Erro na API: {e}"

# Criando instância
sistema_api = SistemaIntegracao()
api_tool = APITool()
api_tool.sistema = sistema_api
```

### **Aula 10.3: Sistema de Workflow Inteligente Completo**

#### **Workflow com LangGraph e APIs**

```python
class EstadoWorkflow(TypedDict):
    """Estado do workflow inteligente"""
    comando: str
    tipo_acao: str
    dados: dict
    resultado: str
    status: str
    timestamp: str

def analisar_comando(state: EstadoWorkflow) -> EstadoWorkflow:
    """Analisa o comando e decide a ação"""
    comando = state["comando"].lower()
    
    if "usuário" in comando or "user" in comando:
        state["tipo_acao"] = "buscar_usuarios"
    elif "post" in comando:
        if "criar" in comando or "novo" in comando:
            state["tipo_acao"] = "criar_post"
        else:
            state["tipo_acao"] = "buscar_posts"
    else:
        state["tipo_acao"] = "comando_invalido"
    
    state["timestamp"] = datetime.now().isoformat()
    return state

def executar_acao(state: EstadoWorkflow) -> EstadoWorkflow:
    """Executa a ação determinada"""
    tipo_acao = state["tipo_acao"]
    sistema = SistemaIntegracao()
    
    try:
        if tipo_acao == "buscar_usuarios":
            resultado = sistema.buscar_usuarios()
            state["resultado"] = f"Usuários encontrados: {len(resultado)}"
            state["status"] = "sucesso"
            
        elif tipo_acao == "buscar_posts":
            resultado = sistema.buscar_posts()
            state["resultado"] = f"Posts encontrados: {len(resultado)}"
            state["status"] = "sucesso"
            
        elif tipo_acao == "criar_post":
            resultado = sistema.criar_post(
                titulo="Post automático",
                corpo="Criado pelo sistema de IA"
            )
            state["resultado"] = f"Post criado com ID: {resultado.get('id')}"
            state["status"] = "sucesso"
            
        else:
            state["resultado"] = "Comando não reconhecido"
            state["status"] = "erro"
            
    except Exception as e:
        state["resultado"] = f"Erro: {e}"
        state["status"] = "erro"
    
    return state

def criar_workflow_completo():
    """Cria o workflow completo"""
    
    # Criando grafo
    workflow = StateGraph(EstadoWorkflow)
    
    # Adicionando nós
    workflow.add_node("analisar", analisar_comando)
    workflow.add_node("executar", executar_acao)
    
    # Definindo entrada e saída
    workflow.set_entry_point("analisar")
    workflow.add_edge("analisar", "executar")
    workflow.add_edge("executar", END)
    
    # Compilando
    app = workflow.compile()
    
    return app

# Testando o workflow completo
workflow_app = criar_workflow_completo()

comandos_teste = [
    "Buscar todos os usuários",
    "Mostrar posts do usuário 1",
    "Criar um novo post",
    "Comando inválido"
]

for i, comando in enumerate(comandos_teste, 1):
    print(f"\n🎯 Comando {i}: {comando}")
    
    try:
        # Estado inicial
        estado_inicial = {
            "comando": comando,
            "tipo_acao": "",
            "dados": {},
            "resultado": "",
            "status": "",
            "timestamp": ""
        }
        
        # Executando workflow
        resultado = workflow_app.invoke(estado_inicial)
        
        print(f"🔍 Ação: {resultado['tipo_acao']}")
        print(f"📊 Status: {resultado['status']}")
        print(f"📝 Resultado: {resultado['resultado']}")
        print(f"⏰ Timestamp: {resultado['timestamp']}")
        
    except Exception as e:
        print(f"❌ Erro: {e}")
    
    print("-" * 30)
```

---

## **🎉 Conclusão - Você é um Especialista em LangChain!**

### **O que Você Aprendeu**

Ao longo deste curso completo, você dominou:

✅ **Fundamentos**: O que é LangChain e por que é revolucionário
✅ **Prompts**: A arte de falar com IA de forma eficiente
✅ **Chains**: Como conectar funcionalidades como peças de Lego
✅ **Memory**: Como fazer a IA lembrar como um amigo
✅ **Agents**: Funcionários inteligentes que podem usar ferramentas
✅ **Document Loaders**: Como fazer a IA ler qualquer documento
✅ **RAG**: IA que consulta documentos antes de responder
✅ **Projetos Práticos**: Sistemas reais e funcionais
✅ **Deploy**: Como colocar projetos na internet
✅ **Tópicos Avançados**: LangGraph e integrações complexas

### **Comparação: Antes vs Depois**

| Aspecto | Antes do Curso | Depois do Curso |
|---------|----------------|-----------------|
| **Conhecimento** | Básico sobre IA | Especialista em LangChain |
| **Capacidade** | Usar ChatGPT | Criar aplicações de IA |
| **Projetos** | Nenhum | Sistemas completos |
| **Mercado** | Consumidor | Produtor de soluções |
| **Valor** | Baixo | Alto (desenvolvedor de IA) |

### **Próximos Passos Recomendados**

1. **🔄 Prática**: Continue construindo projetos
2. **🌐 Comunidade**: Participe de fóruns e grupos
3. **📚 Atualizações**: Mantenha-se atualizado com novas versões
4. **💼 Portfólio**: Crie um portfólio de projetos
5. **🚀 Deploy**: Coloque seus projetos na internet

### **Recursos Adicionais**

- **📖 Documentação Oficial**: [langchain.com](https://langchain.com)
- **🐙 GitHub**: [github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- **💬 Discord**: Comunidade oficial do LangChain
- **📺 YouTube**: Canais especializados em IA
- **📱 Redes Sociais**: Siga especialistas da área

### **Mensagem Final**

**Parabéns, meu consagrado!** 🎉

Você acabou de completar um dos cursos mais completos de LangChain disponíveis em português. Agora você tem o conhecimento e as ferramentas para:

- 🚀 **Criar aplicações de IA** que resolvem problemas reais
- 💼 **Se destacar no mercado** como desenvolvedor especializado
- 🌟 **Inovar** com soluções criativas e inteligentes
- 🎯 **Impactar** a vida das pessoas com tecnologia

**Lembre-se**: A IA é uma ferramenta poderosa, mas **você** é quem decide como usá-la. Use esse conhecimento para criar coisas incríveis e fazer a diferença no mundo!

**O futuro da programação é agora, e você está na vanguarda!** 🚀

---

**Desenvolvido com ❤️ por Pedro Guth**

*"A melhor forma de prever o futuro é criá-lo." - Peter Drucker*
