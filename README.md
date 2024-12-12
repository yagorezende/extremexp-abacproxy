# ExtremeXP Policy Access Control
![ExtremeXP](https://img.shields.io/badge/ExtremeXP-121011?style=for-the-badge&logo=extremexp&logoColor=black)
![Python](https://img.shields.io/badge/python-121011?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23121011.svg?style=for-the-badge&logo=flask&logoColor=white)
![Web3](https://img.shields.io/badge/web3-121011?style=for-the-badge&logo=web3.js&logoColor=white)
![Solidity](https://img.shields.io/badge/Solidity-%23121011.svg?style=for-the-badge&logo=solidity&logoColor=white)
![Hyperledger](https://img.shields.io/badge/hyperledger-121011?style=for-the-badge&logo=hyperledger&logoColor=white)
![Docker](https://img.shields.io/badge/docker-121011?style=for-the-badge&logo=docker&logoColor=white)
![Metamask](https://img.shields.io/badge/metamask-121011?style=for-the-badge&logo=metamask&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Keycloak](https://img.shields.io/badge/keycloak-121011?style=for-the-badge&logo=keycloak&logoColor=white)

This project provides a proxy for the ExtremeXP internal modules, enabling the Access Control Based. 

> Note: The translator project is based on the [XACML](https://www.oasis-open.org/committees/xacml/) standard 
and the [Solidity](https://soliditylang.org/) programming language.

## Project Architecture

![Project Architecture](./docs/ExtremeXP-ABAC%20Proxy.png "Project Architecture")


## Getting Started
```bash
# install the project development environment
make install
# run the project
make run
```
The server will be running on http://localhost:5522.
The Swagger documentation is available on the root page.


## Development Progress
#### Overall progress: 
![](https://geps.dev/progress/50)

#### Tasks:
- [x] Project Basic Structure (Flask API + Proxy + kickoff script)
- [x] Integrate with the Keycloak Authorization Server (OAuth or MetaMask)
- [ ] Dockerize the project
- [ ] Integrate with the [ExtremeXP Portal](https://github.com/ExtremeXP-VU/ExtremeXP-portal)
