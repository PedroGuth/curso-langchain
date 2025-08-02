#!/usr/bin/env python3
"""
Script para migrar notebooks do curso para opções gratuitas
Substitui OpenAI por Ollama, Hugging Face ou Mock LLM
"""

import os
import re
import glob
from pathlib import Path

def migrar_notebook(arquivo):
    """Migra um notebook para usar opções gratuitas"""
    
    print(f"🔄 Migrando: {arquivo}")
    
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    
    # Substituições para remover dependências da OpenAI
    substituicoes = [
        # Remover imports da OpenAI
        (r'from langchain_openai import ChatOpenAI', 
         'from langchain_community.llms import Ollama  # Opção gratuita'),
        
        # Substituir ChatOpenAI por Ollama
        (r'ChatOpenAI\([^)]*\)', 
         'Ollama(model="llama2")'),
        
        # Remover configurações de API key
        (r'api_key=os\.getenv\(\'OPENAI_API_KEY\'\)', 
         '# api_key removida - usando modelo local'),
        
        # Substituir OpenAIEmbeddings
        (r'from langchain\.embeddings import OpenAIEmbeddings',
         'from langchain_community.embeddings import OllamaEmbeddings'),
        
        (r'OpenAIEmbeddings\([^)]*\)',
         'OllamaEmbeddings(model="llama2")'),
        
        # Adicionar comentário sobre opções gratuitas
        (r'# Importando as bibliotecas necessárias',
         '# Importando as bibliotecas necessárias\n# 💡 Usando opções gratuitas (Ollama)'),
    ]
    
    # Aplicar substituições
    for padrao, substituicao in substituicoes:
        conteudo = re.sub(padrao, substituicao, conteudo, flags=re.MULTILINE)
    
    # Adicionar célula de setup gratuito no início
    setup_gratuito = '''
# 🆓 SETUP GRATUITO - SEM CUSTOS!
# Esta célula configura um LLM gratuito para o curso

import os
from dotenv import load_dotenv

# Carregando variáveis (se existirem)
load_dotenv()

# Função para configurar LLM gratuito
def get_llm():
    """Retorna o melhor LLM disponível gratuitamente"""
    
    # Tentativa 1: Ollama (recomendado)
    try:
        from langchain_community.llms import Ollama
        return Ollama(model="llama2")
    except:
        pass
    
    # Tentativa 2: Hugging Face
    try:
        from langchain_community.llms import HuggingFaceHub
        if os.getenv("HUGGINGFACEHUB_API_TOKEN"):
            return HuggingFaceHub(
                repo_id="google/flan-t5-base",
                model_kwargs={"temperature": 0.7, "max_length": 512}
            )
    except:
        pass
    
    # Opção 3: Mock LLM (sempre funciona)
    from langchain.llms.fake import FakeListLLM
    respostas = [
        "Aqui está a resposta:", "Vou te ajudar:", "Essa é uma boa pergunta!",
        "Deixe-me explicar:", "Aqui estão as informações:", "Vou criar um exemplo:"
    ]
    return FakeListLLM(responses=respostas)

# Configurando o LLM
llm = get_llm()

print("🚀 LLM gratuito configurado com sucesso!")
print(f"🤖 Tipo: {type(llm).__name__}")
print("💡 Agora você pode usar 'llm' em todos os exemplos do curso!")
'''
    
    # Inserir setup gratuito após a primeira célula de markdown
    if '# 🆓 SETUP GRATUITO' not in conteudo:
        # Encontrar posição para inserir
        pos = conteudo.find('"cells": [')
        if pos != -1:
            # Encontrar o final da primeira célula
            end_first_cell = conteudo.find('},', pos) + 2
            conteudo = conteudo[:end_first_cell] + setup_gratuito + conteudo[end_first_cell:]
    
    # Salvar arquivo migrado
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)
    
    print(f"✅ Migrado: {arquivo}")

def main():
    """Função principal"""
    
    print("🚀 MIGRADOR PARA OPÇÕES GRATUITAS")
    print("=" * 50)
    
    # Encontrar todos os notebooks
    notebooks = glob.glob("notebooks/*.ipynb")
    
    if not notebooks:
        print("❌ Nenhum notebook encontrado!")
        return
    
    print(f"📁 Encontrados {len(notebooks)} notebooks")
    
    # Migrar cada notebook
    for notebook in notebooks:
        if "00_setup_gratuito" not in notebook:  # Pular o setup gratuito
            migrar_notebook(notebook)
    
    print("\n🎉 MIGRAÇÃO CONCLUÍDA!")
    print("=" * 50)
    print("✅ Todos os notebooks foram migrados para opções gratuitas")
    print("💡 Agora os alunos podem aprender sem gastar dinheiro!")
    print("\n📋 PRÓXIMOS PASSOS:")
    print("1. Instale Ollama: https://ollama.ai")
    print("2. Execute: ollama pull llama2")
    print("3. Ou configure Hugging Face: huggingface.co")
    print("4. Ou use Mock LLM (já funciona)")

if __name__ == "__main__":
    main() 