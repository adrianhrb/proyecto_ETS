# USE CASES SPECIFICATION

Use cases specification from [Diagram](img/Diagrama_casos_uso.drawio.png)

**_Actors:_**

| Actor           | Registered user                                                                                                             |
| --------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Characteristics | It's the user that can fully use the aplication, creating a team and competing to win making the best choices every weekend |
| Relations       | The registered user can also make the operations of the unregistered user, that only include creating a new account         |
| References      | From C.U.1 to C.U.11                                                                                                        |
| Notes           | -                                                                                                                           |
| Autors          | Adrián Herrera Brito                                                                                                        |
| Date            | 29/03/2023                                                                                                                  |

| Actor           | Unregistered user                                                                     |
| --------------- | ------------------------------------------------------------------------------------- |
| Characteristics | It's the user that is not registered and can create an account to use the application |
| Relations       | Any relation                                                                          |
| References      | C.U.12                                                                                |
| Notes           | -                                                                                     |
| Autors          | Adrián Herrera Brito, Alejandro Hernández Domínguez                                   |
| Date            | 29/03/2023                                                                            |

**_Use cases:_**

| Use case        | C.U.1 authenticate                                                                                                                       |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png)                                                                                    |
| Actor           | Registered user                                                                                                                          |
| Description     | This is the first step, the user needs to authenticate himself in the application with his credentials to be able to use all the options |
| Pre-Condiciones | - 13                                                                                                                                     |
| Post-Conditions | -                                                                                                                                        |
| Requirements    | Having a created account in the application                                                                                              |
| Notes           | -                                                                                                                                        |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez                                                                                      |
| Date            | 29/03/2023                                                                                                                               |

| Use case        | C.U.2 Create a team                                                 |
| --------------- | ------------------------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png)               |
| Actor           | Registered user                                                     |
| Description     | The user once authenticated can create a team with multiple options |
| Pre-Condiciones | Beeing authenticated in the application                             |
| Post-Conditions | -                                                                   |
| Requirements    | -                                                                   |
| Notes           | -                                                                   |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez                 |
| Date            | 29/03/2023                                                          |

| Use case        | C.U.3 Select driver                                   |
| --------------- | ----------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png) |
| Actor           | Registered user                                       |
| Description     | The user can select 5 drivers to the team             |
| Pre-Condiciones | Beeing in the option "create a team"                  |
| Post-Conditions | -                                                     |
| Requirements    | -                                                     |
| Notes           | -                                                     |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez   |
| Date            | 29/03/2023                                            |

| Use case        | C.U.4 Driver boost                                                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png)                                                                                        |
| Actor           | Registered user                                                                                                                              |
| Description     | The user can apply a boost to one driver, that means that the race weekend the driver will make more points to the user than in a normal one |
| Pre-Condiciones | Having, at least, three drivers to select one for the boost                                                                                  |
| Post-Conditions | -                                                                                                                                            |
| Requirements    | -                                                                                                                                            |
| Notes           | -                                                                                                                                            |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez                                                                                          |
| Date            | 29/03/2023                                                                                                                                   |

| Use case        | C.U.5 Select scuderia                                 |
| --------------- | ----------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png) |
| Actor           | Registered user                                       |
| Description     | The user can select 2 scuderias to the team           |
| Pre-Condiciones | Beeing in the option "create a team"                  |
| Post-Conditions | -                                                     |
| Requirements    | -                                                     |
| Notes           | -                                                     |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez   |
| Date            | 29/03/2023                                            |

| Use case        | C.U.6 Scuderia boost                                                                                                                             |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png)                                                                                            |
| Actor           | Registered user                                                                                                                                  |
| Description     | The user can apply a boost to one scuderia, that means that the race weekend the scuderia will make more points to the user than in a normal one |
| Pre-Condiciones | Having two scuderias                                                                                                                             |
| Post-Conditions | -                                                                                                                                                |
| Requirements    | -                                                                                                                                                |
| Notes           | -                                                                                                                                                |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez                                                                                              |
| Date            | 29/03/2023                                                                                                                                       |

| Use case        | C.U.7 Enter into a legaue                                                                                   |
| --------------- | ----------------------------------------------------------------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png)                                                       |
| Actor           | Registered user                                                                                             |
| Description     | The user can enter into a legaue with friends or other unknown users to compite for winning every F1 season |
| Pre-Condiciones | Beeing authenticated                                                                                        |
| Post-Conditions | -                                                                                                           |
| Requirements    | -                                                                                                           |
| Notes           | -                                                                                                           |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez                                                         |
| Date            | 29/03/2023                                                                                                  |

| Use case | C.U.8 Check league ranking                            |
| -------- | ----------------------------------------------------- |
| Sources  | [Use case diagram](img/Diagrama_casos_uso.drawio.png) |
| Actor    | Registered user 13                                    |

| Use case        | C.U.9 Create a league                                 |
| --------------- | ----------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png) |
| Actor           | Registered user                                       |
| Description     | The user can create a league                          |
| Pre-Condiciones | Beeing authenticated                                  |
| Post-Conditions | -                                                     |
| Requirements    | -                                                     |
| Notes           | -                                                     |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez   |
| Date            | 29/03/2023                                            |

13
| Use case | C.U.10 Invite to the league |
| --------------- | ------------------------------------------------------------- |
| Sources | [Use case diagram](img/Diagrama_casos_uso.drawio.png) |
| Actor | Registered user |
| Description | The user can invite some friends to the created league |
| Pre-Condiciones | Having a created league (Be the administrator of that league) |
| Post-Conditions | - |
| Requirements | - |
| Notes | - |
| Autor | Adrián Herrera Brito, Alejandro Hernández Domínguez |
| Date | 29/03/2023 |

| Use case        | C.U.11 Check global ranking                                                            |
| --------------- | -------------------------------------------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png)                                  |
| Actor           | Registered user                                                                        |
| Description     | The user can check the global ranking to check the best players with most points maked |
| Pre-Condiciones | Beeing authenticated                                                                   |
| Post-Conditions | -                                                                                      |
| Requirements    | -                                                                                      |
| Notes           | -                                                                                      |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez                                    |
| Date            | 29/03/2023                                                                             |

| Use case        | C.U.12 Register                                                                                                                                                 |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sources         | [Use case diagram](img/Diagrama_casos_uso.drawio.png)                                                                                                           |
| Actor           | Unregistered user, Registered user                                                                                                                              |
| Description     | The unregistered user can create an account and the registered user can create a new different account with other (and not used in the application) credentials |
| Pre-Condiciones | -                                                                                                                                                               |
| Post-Conditions | -                                                                                                                                                               |
| Requirements    | -                                                                                                                                                               |
| Notes           | -                                                                                                                                                               |
| Autor           | Adrián Herrera Brito, Alejandro Hernández Domínguez                                                                                                             |
| Date            | 29/03/2023                                                                                                                                                      |
