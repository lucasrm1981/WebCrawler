# WebCrawler

Este código Python faz scraping de dados de preços de criptomoedas do site crypto.com e os organiza em um DataFrame do pandas, em seguida, salva os dados em formatos CSV e JSON.

Vamos analisar o código linha por linha:

    from pprint import pprint: Importa a função pprint do módulo pprint para exibir dados de forma mais legível na saída.

    import requests: Importa o módulo requests para fazer solicitações HTTP.

    from bs4 import BeautifulSoup: Importa a classe BeautifulSoup do módulo bs4 para fazer parsing de documentos HTML.

    Define a função get_table_heading(table) que extrai os cabeçalhos da tabela HTML.

    Define a função extract_crypto_data(table) que extrai os dados das criptomoedas da tabela HTML.

    if __name__ == '__main__': Esta linha verifica se o script está sendo executado como um programa principal.

    Define a URL do site de onde os dados serão extraídos.

    Faz uma solicitação HTTP para a URL especificada.

    Usa BeautifulSoup para analisar o conteúdo HTML da página.

    Encontra a tabela na página HTML.

    Chama a função get_table_heading(table) para obter os cabeçalhos da tabela.

    Chama a função extract_crypto_data(table) para obter os dados das criptomoedas.

    Usa pprint para imprimir os cabeçalhos e os dados das criptomoedas.

    from pandas import DataFrame: Importa a classe DataFrame do módulo pandas.

    Cria um DataFrame pandas chamado crypto_df com os dados extraídos e os cabeçalhos.

    Salva o DataFrame em um arquivo CSV chamado result.csv sem incluir o índice.

    Salva o DataFrame em um arquivo JSON chamado result.json sem incluir o índice.

Este código é útil para extrair dados de preços de criptomoedas de uma página da web e armazená-los em formatos comuns para análise posterior.
