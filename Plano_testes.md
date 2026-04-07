
# Plano de Testes — D&D 5th Edition API
--- 
*Disciplina: Qualidade e Gerência de Produto de Software | Ferramenta: Postman | Data: Março/2026*
*Alunos: preguica*

## 1. Escopo 
---
O sistema a ser testado é a D&D 5th Edition API (https://www.dnd5eapi.co), uma API REST pública que fornece dados do jogo de RPG Dungeons & Dragons em sua 5ª edição. 

A suíte de testes cobrirá os endpoits listados a seguir, validando os seguintes aspectos: 
- Recuperação de magias individuais por índice (ex: acid-arrow)
- Listagem de todas as magias disponíveis
- Integridade estrutural dos campos retornados (level, components, damage, etc)
- Comportamento da API para entradas inválidas, vazias ou nos limites (tipo nível 0 e nível 9)
- Consistência das URLs internas (URLs de tipos de dano e classes retornadas pela API)

**Endpoints Cobertos**
- https://www.dnd5eapi.co/api/2014/equipments/

- https://www.dnd5eapi.co/api/2014/alignments/

- https://www.dnd5eapi.co/api/2014/spells/
	- https://www.dnd5eapi.co/api/2014/spells/{spell}

- https://www.dnd5eapi.co/api/2014/monsters/
	- https://www.dnd5eapi.co/api/2014/monsters/{monster}

- https://www.dnd5eapi.co/api/2014/classes/

## 2. Objetivos 

---
A suíte de testes tem como objetivo garantir que: 
- Garantir a integridade do sistema testado
- Verificar a vulnerabilidade a falhas
- Verificar se o software é suficientemente otimizado
- Garantir a fidelidade ao conteúdo original


## 3. Estratégia de Testes 
---
Abordagem usada, tecncias de particionamento de equivalencia e analise de valor limite utilizadas

A abordagem utilizada para os testes foi a Caixa Preta, visto que testamos um sistema sem ter acesso ao seu código de funcionamento interno e tendo disponível apenas as entradas e saídas dos dados do sistema.
## 4. Ambiente
---
Tecnologias versões e dependências

Foram utilizadas as seguintes tecnologias
- Postman versão 12.+ (framework) 12+ (aplicativo) for windows
- Postman versão 12.+ (framework) 12+ (aplicativo) for linux

## 5. Descrição dos Casos de Teste
---
tabela com tudo, id nome, pre condicao, entrada ação e resultado
## 6. Critérios de Aceite
---
O sistema será considerado aceito a partir da execução dos testes e sua devida aprovação:

- Todos os end-points testados devem cumprir os requisitos estipulados de tempo de resposta.
- Existência de campos obrigatórios e os mesmos não nulos.
- Testes de valores de dados corretos de acordo com o requisito esperado
- Testes de regras de negócios (lógica interna correta)
- Testes de listas com dimensão e valores internos corretos
- Testes de URL existentes quando necessário e no padrão correto
- Bloqueios de requisições sem permissão ou inválidas
## 7. Riscos e Limitações
---
- Quantidade dos dados fornecidos pela API
- Falta de dados dentro de documentos internos da API ( dados desatualizados e incompletos)
- Falta de cobertura de endpoints, além de bloqueio por alto número de requisições
