
# Plano de Testes — D&D 5th Edition API
--- 
*Disciplina: Qualidade e Gerência de Produto de Software | Ferramenta: Postman | Data: Março/2026*
*Alunos: Felipe Silva Loschi, Felipe Ferreira, Guilherme Emergente e Pedro Henrique*

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
# Tabela de Casos de Teste — D&D 5e API

| ID     | Nome                                                                                                  | Pré-condição                        | Dados de Entrada                              | Ação                                   | Resultado Esperado                                                                 |
|--------|-------------------------------------------------------------------------------------------------------|-------------------------------------|-----------------------------------------------|----------------------------------------|------------------------------------------------------------------------------------|
| TC-001 | Status code é 200                                                                                     | API online e acessível              | index: animate-dead                           | GET /api/2014/spells/animate-dead      | Status 200 OK                                                                      |
| TC-002 | Mago e clérigo devem ser capazes de utilizar a magia                                                  | TC-001 passou                       | index: animate-dead                           | GET /api/2014/spells/animate-dead      | classes contém objetos com index "wizard" e "cleric"                               |
| TC-003 | O level da magia deve ser 3                                                                           | TC-001 passou                       | index: animate-dead                           | GET /api/2014/spells/animate-dead      | Campo level igual a 3                                                              |
| TC-004 | O material necessário para a magia deve ser um drop de sangue, uma peça de carne e uma gota de água  | TC-001 passou                       | index: animate-dead                           | GET /api/2014/spells/animate-dead      | Campo material igual a "A drop of blood, a piece of flesh, and a pinch of bone dust." |
| TC-005 | As urls retornadas devem ser válidas                                                                  | TC-001 passou                       | index: animate-dead                           | GET /api/2014/spells/animate-dead      | Todas as URLs de classes, subclasses e school seguem o padrão /api/2014/{tipo}/{index} |
| TC-006 | O tempo de casting não deve ser maior que 1 minuto                                                    | TC-001 passou                       | index: animate-dead                           | GET /api/2014/spells/animate-dead      | Valor numérico de casting_time não é maior que 1                                   |
| TC-007 | A magia não deve ser um ritual                                                                        | TC-001 passou                       | index: animate-dead                           | GET /api/2014/spells/animate-dead      | Campo ritual igual a false                                                         |
| TC-008 | O range da magia não deve ser maior que 10 feet                                                       | TC-001 passou                       | index: animate-dead                           | GET /api/2014/spells/animate-dead      | Valor numérico de range não é maior que 10                                         |
| TC-009 | Status code é 200                                                                                     | API online e acessível              | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | Status 200 OK                                                                      |
| TC-010 | Dano de magia no level 2 é 4d4                                                                        | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | damage_at_slot_level['2'] igual a "4d4"                                            |
| TC-011 | Mago deve ser capaz de utilizar a magia                                                               | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | classes contém objeto com index "wizard"                                           |
| TC-012 | O dano deve aumentar a cada level                                                                     | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | Para cada slot i (3 a 9), dano no slot i é maior que no slot i-1                   |
| TC-013 | Tamanho da lista de nível é igual a 8 (level 2 ao 9)                                                 | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | Object.keys(damage_at_slot_level) tem comprimento 8                                |
| TC-014 | Maior nível de magia é 9                                                                              | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | damage_at_slot_level possui a propriedade '9'                                      |
| TC-015 | O dano deve aumentar de 1d4 a cada nível                                                              | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | Para cada slot i (3 a 9), dano no slot i é maior que no slot i-1                   |
| TC-016 | Campos devem retornar uma url válida                                                                  | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | Todas as URLs de classes, subclasses, school e damage_type seguem o padrão /api/2014/{tipo}/{index} |
| TC-017 | Classes diferentes de mago não podem usar a magia                                                    | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | classes não contém objeto com index "cleric"                                       |
| TC-018 | O casting time não deve ser maior do que 1 turno                                                      | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | Valor numérico de casting_time não é maior que 1                                   |
| TC-019 | O range não deve ser maior do que 90 feet                                                             | TC-009 passou                       | index: acid-arrow                             | GET /api/2014/spells/acid-arrow        | Valor numérico de range não é maior que 90                                         |
| TC-020 | Status 200 OK - Alignments | API Online | GET /alignments | Realizar requisição GET | Status Code deve ser 200 |
| TC-021 | Integridade dos campos - Alignments | API Online | GET /alignments | Validar propriedades do JSON | "Todos os itens em results devem ter: index |  name e url" |
| TC-022 | Contagem de alinhamentos (Campo count) | API Online | GET /alignments | Verificar valor da chave count | O valor deve ser exatamente 9 |
| TC-023 | Quantidade na lista de resultados | API Online | GET /alignments | Contar itens no array results | Devem existir 9 itens na lista |
| TC-024 | Bloqueio de combinações inválidas | API Online | GET /alignments | Validar index contra lista proibida | "Não deve haver índices como ""chaotic-chaotic"" ou  |""good-good"""
| TC-025 | Performance - Alignments | API Online | GET /alignments | Medir tempo de resposta | O tempo deve ser inferior a 1000ms |
| TC-026 | Status 200 OK - Todos os Monstros | API Online | GET /monsters | Realizar requisição GET | Status Code deve ser 200 |
| TC-027 | Validação de lista não vazia | API Online | GET /monsters | Verificar array results | O campo results deve ser um array e não estar vazio |
| TC-028 | Quantidade total de monstros | API Online | GET /monsters | Contar itens no array results | A lista deve conter 334 itens |
| TC-029 | Sincronia Count vs Results | API Online | GET /monsters | Comparar count com length do array | Os valores devem ser idênticos |
| TC-030 | Integridade dos Monstros (Amostra) | Detalhes acessíveis | GET /monsters/{index} | "Validar campos essenciais (HP |  AC |  Atributos)" | Campos obrigatórios  |não podem ser vazios e devem ter tipos corretos
| TC-031 | Status 404 - Monstro Inexistente | API Online | GET /monsters/exemplo_nao_existe | Tentar buscar monstro inválido | Status Code deve ser 404 |
| TC-032 | Negativo - Status 200 para erro | API Online | GET /monsters/exemplo_nao_existe | Tentar buscar monstro inválido | O status NÃO deve ser 200 |
| TC-034 | Integridade Detalhada - Aboleth | API Online | GET /monsters/aboleth | Validar valores específicos do Aboleth | "Nome=""Aboleth"" |  Força=21 |   |Alinhamento=""lawful evil"" |  etc."
| TC-035 | Validação de Sub-listas - Aboleth | API Online | GET /monsters/aboleth | Verificar arrays de ações e proficiências | Arrays actions e special_abilities não  |podem estar vazios
| TC-037 | Negativo - Spellcasting Aboleth | API Online | GET /monsters/aboleth | "Buscar ""Spellcasting"" em special_abilities" | O monstro não deve possuir esta  |habilidade
| TC-039 | Método POST não permitido | Endpoint de leitura | POST /monsters/monstro_exemplo | Tentar criar um monstro via POST | Status Code deve ser 404 ou 405 |
| TC-040 | Formato de erro (HTML) | Endpoint de leitura | POST /monsters/monstro_exemplo | Verificar Header Content-Type | O tipo de conteúdo deve ser text/html |
| TC-041 | Mensagem de erro de método | Endpoint de leitura | POST /monsters/monstro_exemplo | Verificar corpo da resposta | "Deve conter o texto ""Cannot POST /api/ |2014/monsters"""
| TC-043 | Método DELETE não permitido | Endpoint de leitura | DELETE /monsters/aboleth | Tentar deletar um monstro | Status Code deve ser 404 ou 405 |
| TC-044 | Equipamento Basket possui campos obrigatórios | API online e acessível | index: basket | GET /api/2014/equipment/basket | Campos name, index, url e equipment_category presentes e corretos |
| TC-045 | Campo cost possui tipos corretos | API online e acessível | index: basket | GET /api/2014/equipment/basket | cost.quantity é number e cost.unit é string |
| TC-046 | Basket deve possuir categoria adventuring-gear | API online e acessível | index: basket | GET /api/2014/equipment/basket | equipment_category.index igual a "adventuring-gear" |
| TC-047 | Weight deve ser um número maior que zero | API online e acessível | index: basket | GET /api/2014/equipment/basket | weight é number e maior que 0 |
| TC-048 | Tempo de resposta é menos de 1s | API online e acessível | index: basket | GET /api/2014/equipment/basket | responseTime abaixo de 1000ms |
| TC-049 | Cada item da lista deve ter nome e URL | API online e acessível | — | GET /api/2014/equipment/ | Todos os itens em results possuem name (string não vazia) e url |
| TC-050 | Tempo de resposta é menos de 1s | API online e acessível | — | GET /api/2014/equipment/ | responseTime abaixo de 1000ms |
| TC-051 | Status deve ser 404 para equipamento inexistente | API online e acessível | index: banana | GET /api/2014/equipment/banana | Status Code 404 |
| TC-052 | Tempo de resposta é menos de 1s | API online e acessível | index: banana | GET /api/2014/equipment/banana | responseTime abaixo de 1000ms |
| TC-053 | Chain Mail deve possuir categoria de armor | API online e acessível | index: chain-mail | GET /api/2014/equipment/chain-mail | equipment_category.index igual a "armor" |
| TC-054 | Desvantagem em stealth condiz com o tipo de armadura | API online e acessível | index: chain-mail | GET /api/2014/equipment/chain-mail | Heavy: stealth_disadvantage true / Light: stealth_disadvantage false |
| TC-055 | Tempo de resposta é menos de 1s | API online e acessível | index: chain-mail | GET /api/2014/equipment/chain-mail | responseTime abaixo de 1000ms |
| TC-056 | Leather Armor deve possuir categoria de armor | API online e acessível | index: leather-armor | GET /api/2014/equipment/leather-armor | equipment_category.index igual a "armor" |
| TC-057 | Desvantagem em stealth condiz com o tipo de armadura | API online e acessível | index: leather-armor | GET /api/2014/equipment/leather-armor | Heavy: stealth_disadvantage true / Light: stealth_disadvantage false |
| TC-058 | Leather Armor possui peso fixo | API online e acessível | index: leather-armor | GET /api/2014/equipment/leather-armor | weight igual a 10 e é number |
| TC-059 | Tempo de resposta é menos de 1s | API online e acessível | index: leather-armor | GET /api/2014/equipment/leather-armor | responseTime abaixo de 1000ms |
| TC-060 | Dano base da Longsword | API online e acessível | index: longsword | GET /api/2014/equipment/longsword | damage_dice igual a "1d8" e damage_type.index igual a "slashing" |
| TC-061 | Longsword possui propriedade versatile | API online e acessível | index: longsword | GET /api/2014/equipment/longsword | Array properties contém objeto com index "versatile" |
| TC-062 | Dano com duas mãos da Longsword | API online e acessível | index: longsword | GET /api/2014/equipment/longsword | two_handed_damage.damage_dice igual a "1d10" e damage_type.index igual a "slashing" |
| TC-063 | Tempo de resposta é menos de 1s | API online e acessível | index: longsword | GET /api/2014/equipment/longsword | responseTime abaixo de 1000ms |
| TC-064 | Status da requisição de todas as classes deve ser 200 | API online e acessível | endpoint: classes | GET /api/2014/classes | Status igual a 200 |
| TC-065 | Contagem total de classes deve ser 12 | API online e acessível | endpoint: classes | GET /api/2014/classes | count igual a 12 |
| TC-066 | Primeira classe deve ser barbarian | API online e acessível | endpoint: classes | GET /api/2014/classes | results[0].index igual a "barbarian" |
| TC-067 | Cada classe deve conter apenas index, name e url | API online e acessível | endpoint: classes | GET /api/2014/classes | Cada item possui somente "index", "name" e "url" |
| TC-068 | URL da classe deve terminar com seu index | API online e acessível | endpoint: classes | GET /api/2014/classes | Último segmento da URL igual ao index |
| TC-069 | Classe cleric deve possuir spellcasting | API online e acessível | index: cleric | GET /api/2014/classes/cleric | Propriedade spellcasting existente |
| TC-070 | Habilidade de spellcasting do cleric deve ser wisdom | API online e acessível | index: cleric | GET /api/2014/classes/cleric | spellcasting.spellcasting_ability.index igual a "wis" |
| TC-071 | Cleric não deve possuir proficiency all-armor | API online e acessível | index: cleric | GET /api/2014/classes/cleric | Não existe proficiency com index "all-armor" |
| TC-072 | Cleric não deve conter saving throws inválidos | API online e acessível | index: cleric | GET /api/2014/classes/cleric | saving_throws não contém "str", "dex", "con", "int" |
| TC-073 | Método POST não deve ser permitido | API online e acessível | endpoint: artificer | POST /api/2014/artificer | Status 404 ou 405 |
| TC-074 | Método DELETE não deve ser permitido | API online e acessível | index: cleric | DELETE /api/2014/classes/cleric | Status 404 ou 405 |
| TC-075 | Status da classe barbarian deve ser 200 | API online e acessível | index: barbarian | GET /api/2014/classes/barbarian | Status igual a 200 |
| TC-076 | Hit die deve estar entre 6 e 12 | API online e acessível | index: barbarian | GET /api/2014/classes/barbarian | hit_die entre 6 e 12 |
| TC-077 | Classe deve conter subclasses | API online e acessível | index: barbarian | GET /api/2014/classes/barbarian | Propriedade subclasses existente |
| TC-078 | Classe deve possuir dois saving throws | API online e acessível | index: barbarian | GET /api/2014/classes/barbarian | saving_throws com tamanho 2 |
| TC-079 | proficiency_choices não deve ser vazio | API online e acessível | index: barbarian | GET /api/2014/classes/barbarian | proficiency_choices não vazio |
| TC-080 | Fighter não deve possuir spellcasting | API online e acessível | index: fighter | GET /api/2014/classes/fighter | Propriedade spellcasting inexistente |
| TC-081 | Fighter deve possuir proficiency all-armor | API online e acessível | index: fighter | GET /api/2014/classes/fighter | Existe proficiency com index "all-armor" |
| TC-082 | Fighter não deve conter saving throws inválidos | API online e acessível | index: fighter | GET /api/2014/classes/fighter | saving_throws não contém "dex", "int", "wis", "cha" |
| TC-083 | Classe inexistente deve retornar 404 | API online e acessível | index: bloodhunter | GET /api/2014/classes/bloodhunter | Status igual a 404 |

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
