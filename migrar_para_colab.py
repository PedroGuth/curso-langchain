#!/usr/bin/env python3
"""
Script para migrar notebooks do curso para Google Colab
Adapta todos os notebooks para funcionar perfeitamente no Colab
"""

import os
import re
import glob
import json
from pathlib import Path

def migrar_notebook_colab(arquivo):
    """Migra um notebook para funcionar no Google Colab"""
    
    print(f"🔄 Migrando para Colab: {arquivo}")
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Parse do JSON do notebook
    try:
        notebook = json.loads(conteudo)
    except:
        print(f"❌ Erro ao parsear JSON: {arquivo}")
        return
    
    # Adicionar metadados do Colab
    if "metadata" not in notebook:
        notebook["metadata"] = {}
    
    notebook["metadata"]["colab"] = {
        "name": Path(arquivo).stem,
        "private_outputs": True,
        "provenance": []
    }
    
    # Substituições simples para Colab
    substituicoes = [
        # Substituir pip install por !pip install
        (r'pip install', '!pip install'),
        
        # Adicionar comentários sobre Colab
        (r'# Importando as bibliotecas necessárias',
         '# Importando as bibliotecas necessárias\n# 💡 Google Colab - Funciona no navegador!'),
        
        # Substituir configurações de API key
        (r'api_key=os\.getenv\(\'OPENAI_API_KEY\'\)',
         'api_key=os.getenv(\'OPENAI_API_KEY\')  # Configure sua API key no Colab'),
    ]
    
    # Aplicar substituições no conteúdo JSON
    conteudo_json = json.dumps(notebook, indent=2, ensure_ascii=False)
    
    for padrao, substituicao in substituicoes:
        conteudo_json = re.sub(padrao, substituicao, conteudo_json, flags=re.MULTILINE)
    
    # Salvar arquivo migrado
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo_json)
    
    print(f"✅ Migrado para Colab: {arquivo}")

def criar_arquivo_colab_instructions():
    """Cria arquivo com instruções para usar no Colab"""
    
    instrucoes = """# 🚀 **Como Usar Este Curso no Google Colab**

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
"""
    
    with open("COMO_USAR_COLAB.md", "w", encoding="utf-8") as f:
        f.write(instrucoes)
    
    print("✅ Arquivo COMO_USAR_COLAB.md criado!")

def main():
    """Função principal"""
    
    print("🚀 MIGRADOR PARA GOOGLE COLAB")
    print("=" * 50)
    
    # Encontrar todos os notebooks
    notebooks = glob.glob("notebooks/*.ipynb")
    
    if not notebooks:
        print("❌ Nenhum notebook encontrado!")
        return
    
    print(f"📁 Encontrados {len(notebooks)} notebooks")
    
    # Migrar cada notebook
    for notebook in notebooks:
        if "00_setup_colab" not in notebook:  # Pular o setup do Colab
            migrar_notebook_colab(notebook)
    
    # Criar arquivo de instruções
    criar_arquivo_colab_instructions()
    
    print("\n🎉 MIGRAÇÃO PARA COLAB CONCLUÍDA!")
    print("=" * 50)
    print("✅ Todos os notebooks foram adaptados para Google Colab")
    print("💡 Agora os alunos podem aprender no navegador!")
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. Abra [colab.research.google.com](https://colab.research.google.com)")
    print("2. Faça upload dos notebooks")
    print("3. Configure sua opção de LLM")
    print("4. Comece a aprender!")

if __name__ == "__main__":
    main() 