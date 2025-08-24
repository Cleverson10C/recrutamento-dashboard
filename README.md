# Dashboard de Candidatos

Este projeto é um dashboard dinâmico para análise e segmentação de candidatos, desenvolvido com Python e Streamlit.

## Funcionalidades
- Visualização de candidatos por cidade e profissão
- Filtros dinâmicos (cidade, profissão)
- Listagem com acesso rápido aos links de currículo e carteira digital
- Exportação de listas filtradas em CSV
- Leitura dos dados diretamente de uma planilha Excel (`candidatos.xlsx`)

## Como rodar o projeto
1. Instale as dependências:
   ```bash
   pip install streamlit pandas openpyxl
   ```
2. Execute o dashboard:
   ```bash
   streamlit run app.py
   ```
3. O dashboard abrirá automaticamente no navegador (http://localhost:8501).

## Como atualizar os dados
- Os dados dos candidatos estão na planilha `candidatos.xlsx`. Basta editar a planilha para atualizar ou adicionar novos candidatos.

## Manutenção
- Para atualizar dependências, edite o arquivo `requirements.txt` (se existir)
 e rode `pip install -r requirements.txt`.
- Recomenda-se manter o Python atualizado.

## Orientação rápida para equipe
- Utilize os filtros na barra lateral para segmentar os candidatos.
- Clique nos links para acessar currículo ou carteira digital.
- Exporte listas filtradas usando o botão "Exportar lista filtrada (CSV)".
- Para atualizar ou adicionar candidatos, edite a planilha Excel.

---

Dúvidas ou sugestões? Entre em contato com o responsável pelo projeto.

