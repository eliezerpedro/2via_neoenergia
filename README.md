# Download de Segunda via da fatura da Neoenergia

## Visão geral

Esse projeto faz o download da segunda via da fatura da Neoenergia.


## Variáveis de configuração

 

- CPF
- Senha
- Número do contrato

  

## Desafio

  

Este desafio usa apenas Python com a biblioteca Selenium. Foi dividido nas seguintes etapas:

  

1. Loga no site da Neoenergia
2. Seleciona o contrato definido no arquivo de configuração
3. Faz o download da segunda via da fatura mais recente
4. Salva o boleto no diretório /output
5. Checa se o boleto foi baixado e fecha o navegador

  

## Requerimentos

  



- Python 3.x
- Selenium
- undetected-chromedriver


  

## Como usar

  

1. Clone o repositório
2. Instale as dependências usando pip

  

```bash

pip  install  selenium
pip  install  undetected-chromedriver

```

  

3. Forneça as variáveis de configuração válidas no arquivo config.py

4. Execute o script Python

  

```bash

python  main.py

```


5. Assim que o script terminar de executar, você encontrará o arquivo .pdf no diretório /output. 
