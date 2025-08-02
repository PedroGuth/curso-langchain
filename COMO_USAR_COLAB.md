# 🚀 **Como Usar Este Curso no Google Colab**

## **🎯 Por que Google Colab?**

- ✅ **100% gratuito** - Sem custos ocultos
- ✅ **Sem instalação** - Funciona no navegador
- ✅ **GPU gratuita** - Para processamento rápido
- ✅ **Compartilhamento fácil** - Compartilhe seus notebooks
- ✅ **Backup automático** - Salva no Google Drive

## **🚀 Como Começar:**

### **1. Abra o Google Colab:**
- Vá para [colab.research.google.com](https://colab.research.google.com)
- Faça login com sua conta Google

### **2. Carregue um notebook:**
- Clique em "Arquivo" > "Fazer upload do notebook"
- Selecione um dos notebooks do curso
- Ou copie e cole o conteúdo

### **3. Configure o LLM:**
- Execute a primeira célula (setup)
- Escolha sua opção:
  - **Mock LLM**: Gratuito, respostas simuladas
  - **Hugging Face**: Gratuito com limites
  - **OpenAI**: Melhor qualidade, custo por uso

### **4. Aprenda!**
- Execute as células uma por vez
- Experimente com os códigos
- Faça os exercícios propostos

## **🆓 Opções Gratuitas:**

### **Mock LLM (Recomendado para Iniciantes):**
```python
# Já configurado no notebook
# Respostas simuladas para aprender conceitos
# 100% gratuito, funciona sempre
```

### **Hugging Face:**
```python
# Configure seu token
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "seu_token"

# Use modelo gratuito
from langchain_community.llms import HuggingFaceHub
llm = HuggingFaceHub(
    repo_id="google/flan-t5-base",
    model_kwargs={"temperature": 0.7, "max_length": 512}
)
```

### **OpenAI (Para Quem Quiser):**
```python
# Configure sua API key
os.environ["OPENAI_API_KEY"] = "sua_chave"

# Use modelo da OpenAI
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    api_key=os.environ["OPENAI_API_KEY"]
)
```

## **💡 Dicas para o Colab:**

### **Execução de Células:**
- **Shift + Enter**: Executa célula atual
- **Ctrl + Enter**: Executa célula sem ir para próxima
- **Alt + Enter**: Executa célula e cria nova

### **Atalhos Úteis:**
- **Ctrl + M + A**: Inserir célula acima
- **Ctrl + M + B**: Inserir célula abaixo
- **Ctrl + M + D**: Deletar célula

### **Configurações:**
- **Runtime > Change runtime type**: Escolha GPU se necessário
- **Runtime > Restart runtime**: Reinicia o ambiente
- **File > Save a copy in Drive**: Salva no Google Drive

## **🚨 Problemas Comuns:**

### **Erro de dependências:**
```python
# Execute esta célula primeiro
!pip install langchain langchain-community python-dotenv
```

### **Erro de API key:**
```python
# Configure sua chave
import os
os.environ["OPENAI_API_KEY"] = "sua_chave_aqui"
```

### **Notebook lento:**
- Use Runtime > Change runtime type > GPU
- Reinicie o runtime se necessário

## **🎓 Conclusão:**

**Google Colab é perfeito para aprender LangChain!**

- **Sem instalação** - Funciona no navegador
- **100% gratuito** - Sem custos ocultos
- **GPU disponível** - Para processamento rápido
- **Compartilhamento fácil** - Compartilhe seus projetos

**💡 Dica do Pedro**: Comece com Mock LLM para aprender os conceitos. Quando estiver confortável, configure Hugging Face ou OpenAI para respostas reais!

---

**🚀 Bora codar no Colab, meu consagrado!** 💪
