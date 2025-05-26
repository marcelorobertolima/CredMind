import json

##################################################################################################
#Dados Basicos Empresa
##################################################################################################
def dadosTeste_BigDataCorp_DadosBasicos_Empresa():
    
    jsonStr = '''
                {
                    "DadosEmpresa": {
                        "Result": [
                            {
                                "MatchKeys": "doc{80379001000128}",
                                "BasicData": {
                                    "TaxIdNumber": "80379001000128",
                                    "TaxIdCountry": "Brazil",
                                    "AlternativeIdNumbers": {},
                                    "OfficialName": "FLYSHOES BRAZIL LTDA",
                                    "TradeName": "FLYSHOES BRAZIL",
                                    "Aliases": {
                                        "UnstandardizedRFOfficialName": "FLYSHOES BRAZIL LTDA",
                                        "UnstandardizedRFTradeName": "FLYSHOES BRAZIL"
                                    },
                                    "NameUniquenessScore": 1,
                                    "OfficialNameUniquenessScore": 1,
                                    "TradeNameUniquenessScore": 0.5,
                                    "FoundedDate": "1987-12-22T00:00:00Z",
                                    "Age": 36,
                                    "IsHeadquarter": true,
                                    "HeadquarterState": "PR",
                                    "IsConglomerate": false,
                                    "TaxIdStatus": "ATIVA",
                                    "TaxIdOrigin": "Receita Federal",
                                    "TaxIdStatusDate": "2024-05-03T00:00:00Z",
                                    "TaxIdStatusRegistrationDate": "2006-12-21T00:00:00Z",
                                    "TaxRegime": "LUCRO PRESUMIDO",
                                    "CompanyType_ReceitaFederal": "DEMAIS",
                                    "TaxRegimes": {
                                        "Simples": false
                                    },
                                    "Activities": [
                                        {
                                            "IsMain": true,
                                            "Code": "4642701",
                                            "Activity": "COMERCIO ATACADISTA DE ARTIGOS DO VESTUARIO E ACESSORIOS, EXCETO PROFISSIONAIS E DE SEGURANCA"
                                        },
                                        {
                                            "IsMain": false,
                                            "Code": "4643501",
                                            "Activity": "COMERCIO ATACADISTA DE CALCADOS"
                                        },
                                        {
                                            "IsMain": false,
                                            "Code": "4643502",
                                            "Activity": "COMERCIO ATACADISTA DE BOLSAS, MALAS E ARTIGOS DE VIAGEM"
                                        },
                                        {
                                            "IsMain": false,
                                            "Code": "4781400",
                                            "Activity": "COMERCIO VAREJISTA DE ARTIGOS DO VESTUARIO E ACESSORIOS"
                                        },
                                        {
                                            "IsMain": false,
                                            "Code": "4782201",
                                            "Activity": "COMERCIO VAREJISTA DE CALCADOS"
                                        }
                                    ],
                                    "LegalNature": {
                                        "Code": "2062",
                                        "Activity": "SOCIEDADE EMPRESARIA LIMITADA"
                                    },
                                    "SpecialSituation": "",
                                    "CreationDate": "2012-12-21T00:00:00Z",
                                    "LastUpdateDate": "2024-05-03T00:00:00Z",
                                    "AdditionalOutputData": {
                                        "Capital": "TREZENTOS MIL REAIS",
                                        "CapitalRS": "300000.00",
                                        "NIRE": "",
                                        "NIRECompanySize": "",
                                        "NIREHeadquartersType": "",
                                        "NIREHeadquartersCapital": "0",
                                        "NIRELastCaptureDate": "0001-01-01T12:00:00Z",
                                        "COMEX": null,
                                        "COMEXLastUpdate": "0001-01-01T12:00:00Z"
                                    },
                                    "HistoricalData": {
                                        "HasChangedTradeName": true,
                                        "HasChangedTaxRegime": true,
                                        "HistoricalDataEvolution": {
                                            "TradeName": [
                                                {
                                                    "Value": "FLYSHOES BRAZIL",
                                                    "StartDate": "2023-12-01T00:00:00Z"
                                                },
                                                {
                                                    "Value": "FLY SEM LIMITES",
                                                    "StartDate": "2022-06-01T00:00:00Z",
                                                    "EndDate": "2023-12-01T00:00:00Z"
                                                },
                                                {
                                                    "Value": "MARIALVA LIMPEZA CONSERVACAO E MANUTENCAO",
                                                    "StartDate": "2012-12-21T00:00:00Z",
                                                    "EndDate": "2022-06-01T00:00:00Z"
                                                }
                                            ],
                                            "TaxRegime": [
                                                {
                                                    "Value": "LUCRO PRESUMIDO",
                                                    "StartDate": "2024-02-01T00:00:00Z"
                                                },
                                                {
                                                    "Value": "LTDA",
                                                    "StartDate": "2022-06-01T00:00:00Z",
                                                    "EndDate": "2024-02-01T00:00:00Z"
                                                },
                                                {
                                                    "Value": "LUCRO PRESUMIDO",
                                                    "StartDate": "2012-12-21T00:00:00Z",
                                                    "EndDate": "2022-06-01T00:00:00Z"
                                                }
                                            ]
                                        }
                                    }
                                },
                                "ExtendedAddresses": {
                                    "TotalAddresses": 5,
                                    "TotalActiveAddresses": 3,
                                    "TotalWorkAddresses": 4,
                                    "TotalPersonalAddresses": 1,
                                    "TotalUniqueAddresses": 1,
                                    "TotalAddressPassages": 9,
                                    "TotalBadAddressPassages": 0,
                                    "OldestAddressPassageDate": "2012-01-01T00:00:00Z",
                                    "NewestAddressPassageDate": "2024-05-03T00:00:00Z",
                                    "Addresses": [
                                        {
                                            "OwnHeadquarters": false,
                                            "Typology": "AV",
                                            "Title": "",
                                            "AddressMain": "AVENIDA NAIHMA NAME",
                                            "Number": "1121",
                                            "Complement": "",
                                            "Neighborhood": "JARDIM SAO MIGUEL",
                                            "ZipCode": "87070877",
                                            "City": "MARINGA",
                                            "State": "PR",
                                            "Country": "BRASIL",
                                            "Type": "OFFICIAL REGISTRATION",
                                            "AddressCurrentlyInRFSite": true,
                                            "ComplementType": "",
                                            "BuildCode": "B6B974EACE88974A5BBD779B1A045C82A43CAC2462C43567EA555C72EEE39100",
                                            "BuildingCode": "B6B974EACE88974A5BBD779B1A045C82A43CAC2462C43567EA555C72EEE39100",
                                            "HouseholdCode": "B6B974EACE88974A5BBD779B1A045C82A43CAC2462C43567EA555C72EEE39100",
                                            "AddressEntityAge": 126,
                                            "AddressEntityTotalPassages": 2,
                                            "AddressEntityBadPassages": 0,
                                            "AddressEntityCrawlingPassages": 2,
                                            "AddressEntityValidationPassages": 0,
                                            "AddressEntityQueryPassages": -1,
                                            "AddressEntityMonthAveragePassages": 0.48,
                                            "AddressGlobalAge": 538,
                                            "AddressGlobalTotalPassages": 6,
                                            "AddressGlobalBadPassages": 0,
                                            "AddressGlobalCrawlingPassages": 6,
                                            "AddressGlobalValidationPassages": 0,
                                            "AddressGlobalQueryPassages": -1,
                                            "AddressGlobalMonthAveragePassages": 0.34,
                                            "AddressNumberOfEntities": 3,
                                            "Priority": 1,
                                            "IsMainForEntity": true,
                                            "IsRecentForEntity": true,
                                            "IsMainForOtherEntity": true,
                                            "IsRecentForOtherEntity": true,
                                            "IsActive": true,
                                            "IsRatified": true,
                                            "IsLikelyFromAccountant": false,
                                            "LastValidationDate": "0001-01-01T00:00:00",
                                            "EntityFirstPassageDate": "2023-12-29T00:00:00Z",
                                            "EntityLastPassageDate": "2024-05-03T00:00:00Z",
                                            "GlobalFirstPassageDate": "2022-11-25T00:00:00Z",
                                            "GlobalLastPassageDate": "2024-05-16T00:00:00Z",
                                            "CreationDate": "2023-12-29T00:00:00Z",
                                            "LastUpdateDate": "2024-05-03T00:00:00Z",
                                            "HasOptIn": false,
                                            "Latitude": 0,
                                            "Longitude": 0
                                        },
                                        {
                                            "OwnHeadquarters": false,
                                            "Typology": "AV",
                                            "Title": "",
                                            "AddressMain": "TAMANDARE",
                                            "Number": "115",
                                            "Complement": "SALA 17",
                                            "Neighborhood": "ZONA 07",
                                            "ZipCode": "87020010",
                                            "City": "MARINGA",
                                            "State": "PR",
                                            "Country": "BRASIL",
                                            "Type": "RESIDENCE",
                                            "AddressCurrentlyInRFSite": true,
                                            "ComplementType": "",
                                            "BuildCode": "374EBCB7E5E5BD7261D4BFD69E02E210A1DF1238CB65B86095013B3299DE1A7B",
                                            "BuildingCode": "374EBCB7E5E5BD7261D4BFD69E02E210A1DF1238CB65B86095013B3299DE1A7B",
                                            "HouseholdCode": "374EBCB7E5E5BD7261D4BFD69E02E210A1DF1238CB65B86095013B3299DE1A7B",
                                            "AddressEntityAge": 240,
                                            "AddressEntityTotalPassages": 2,
                                            "AddressEntityBadPassages": 0,
                                            "AddressEntityCrawlingPassages": 2,
                                            "AddressEntityValidationPassages": 0,
                                            "AddressEntityQueryPassages": -1,
                                            "AddressEntityMonthAveragePassages": 0.27,
                                            "AddressGlobalAge": 689,
                                            "AddressGlobalTotalPassages": 6,
                                            "AddressGlobalBadPassages": 0,
                                            "AddressGlobalCrawlingPassages": 6,
                                            "AddressGlobalValidationPassages": 0,
                                            "AddressGlobalQueryPassages": -1,
                                            "AddressGlobalMonthAveragePassages": 0.26,
                                            "AddressNumberOfEntities": 2,
                                            "Priority": 3,
                                            "IsMainForEntity": false,
                                            "IsRecentForEntity": false,
                                            "IsMainForOtherEntity": false,
                                            "IsRecentForOtherEntity": false,
                                            "IsActive": true,
                                            "IsRatified": false,
                                            "IsLikelyFromAccountant": false,
                                            "LastValidationDate": "0001-01-01T00:00:00",
                                            "EntityFirstPassageDate": "2022-11-25T00:00:00Z",
                                            "EntityLastPassageDate": "2024-05-03T00:00:00Z",
                                            "GlobalFirstPassageDate": "2022-11-25T00:00:00Z",
                                            "GlobalLastPassageDate": "2024-05-16T00:00:00Z",
                                            "CreationDate": "2022-11-25T00:00:00Z",
                                            "LastUpdateDate": "2024-05-03T00:00:00Z",
                                            "HasOptIn": false,
                                            "Latitude": 0,
                                            "Longitude": 0
                                        }
                                    ]
                                }
                            }
                        ]
                    }
                }'''
   
    DadosTeste = json.loads(jsonStr)

    return DadosTeste

##################################################################################################
#KYC da Emprea - PEP
##################################################################################################
def dadosTeste_BigDataCorp_KYC_Empresa():
    jsonStr = '''   
    {
        "DadosEmpresa": {
            "Result": [
                {
                    "MatchKeys": "doc{03061040000131}",
                    "KycData": {
                        "PEPHistory": [
                            {
                                "Level": "2",
                                "JobTitle": "PEERS",
                                "Department": "FAZENDA SANTA RITA S/A",
                                "Motive": "PUBLIC COMPANY EMPLOYEE",
                                "Source": "RepresentanteDB",
                                "TaxId": "01355214670",
                                "FirstLevelPEPTaxId": "00657573604",
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "2028-06-29T00:00:00Z",
                                "CreationDate": "2024-07-12T19:41:27Z",
                                "LastUpdateDate": "2024-07-12T19:41:27Z"
                            },
                            {
                                "Level": "2",
                                "JobTitle": "SECRETARIO PARLAMENTAR",
                                "Department": "GABINETES DOS DEPUTADOS",
                                "Motive": "MOTHER OF 30802172172",
                                "Source": "BIGDATACORP",
                                "TaxId": "52387054172",
                                "FirstLevelPEPTaxId": "30802172172",
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "2029-05-30T00:00:00Z",
                                "CreationDate": "2024-07-12T19:41:27Z",
                                "LastUpdateDate": "2024-07-12T19:41:27Z"
                            }
                        ],
                        "IsCurrentlyPEP": true,
                        "SanctionsHistory": [
                            {
                                "Source": "ofac",
                                "Type": "Money Laundering",
                                "StandardizedSanctionType": "FINANCIAL CRIMES",
                                "MatchRate": 53,
                                "NameUniquenessScore": 0.04166667,
                                "Details": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL HOLDING, S.R.O.",
                                    "remarks": "(linked to: kocner, marian)"
                                },
                                "NormalizedDetails": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL HOLDING, S.R.O."
                                },
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "9999-12-31T23:59:59.9999999",
                                "CreationDate": "2024-07-17T03:03:43.543",
                                "LastUpdateDate": "2024-07-17T03:03:43.543",
                                "IsCurrentlyPresentOnSource": false,
                                "WasRecentlyPresentOnSource": true
                            },
                            {
                                "Source": "ofac",
                                "Type": "Money Laundering",
                                "StandardizedSanctionType": "FINANCIAL CRIMES",
                                "MatchRate": 48,
                                "NameUniquenessScore": 0.04166667,
                                "Details": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL CASA GRANDE - ULCINJ, MONTENEGRO"
                                },
                                "NormalizedDetails": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL CASA GRANDE - ULCINJ, MONTENEGRO"
                                },
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "9999-12-31T23:59:59.9999999",
                                "CreationDate": "2024-07-17T03:03:06.531",
                                "LastUpdateDate": "2024-07-17T03:03:06.531",
                                "IsCurrentlyPresentOnSource": false,
                                "WasRecentlyPresentOnSource": true
                            },
                            {
                                "Source": "ofac",
                                "Type": "Money Laundering",
                                "StandardizedSanctionType": "FINANCIAL CRIMES",
                                "MatchRate": 46,
                                "NameUniquenessScore": 0.04166667,
                                "Details": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL CASA GRANDE - SARAJEVO, BOSNIA AND HERZEGOVINA"
                                },
                                "NormalizedDetails": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL CASA GRANDE - SARAJEVO, BOSNIA AND HERZEGOVINA"
                                },
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "9999-12-31T23:59:59.9999999",
                                "CreationDate": "2024-07-17T03:03:06.263",
                                "LastUpdateDate": "2024-07-17T03:03:06.263",
                                "IsCurrentlyPresentOnSource": false,
                                "WasRecentlyPresentOnSource": true
                            },
                            {
                                "Source": "ofac",
                                "Type": "Money Laundering",
                                "StandardizedSanctionType": "FINANCIAL CRIMES",
                                "MatchRate": 46,
                                "NameUniquenessScore": 0.04166667,
                                "Details": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL PLAZA",
                                    "remarks": "(linked to: hernandez salas transnational criminal organization)"
                                },
                                "NormalizedDetails": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL PLAZA"
                                },
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "9999-12-31T23:59:59.9999999",
                                "CreationDate": "2024-07-17T03:04:01.104",
                                "LastUpdateDate": "2024-07-17T03:04:01.104",
                                "IsCurrentlyPresentOnSource": false,
                                "WasRecentlyPresentOnSource": true
                            },
                            {
                                "Source": "ofac",
                                "Type": "Money Laundering",
                                "StandardizedSanctionType": "FINANCIAL CRIMES",
                                "MatchRate": 28,
                                "NameUniquenessScore": 0.04166667,
                                "Details": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTELERA LOPEZ MATEOS S.A. DE C.V.",
                                    "SanctionAliases|MatchRate": "HOTEL LAS TORRES|54",
                                    "remarks": "(linked to: hernandez salas transnational criminal organization)"
                                },
                                "NormalizedDetails": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTELERA LOPEZ MATEOS S.A. DE C.V.",
                                    "SanctionAliasesAndMatchRate": "HOTEL LAS TORRES|54"
                                },
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "9999-12-31T23:59:59.9999999",
                                "CreationDate": "2024-07-17T03:02:54.747",
                                "LastUpdateDate": "2024-07-17T03:02:54.747",
                                "IsCurrentlyPresentOnSource": false,
                                "WasRecentlyPresentOnSource": true
                            },
                            {
                                "Source": "ofac",
                                "Type": "Money Laundering",
                                "StandardizedSanctionType": "FINANCIAL CRIMES",
                                "MatchRate": 25,
                                "NameUniquenessScore": 0.04166667,
                                "Details": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL CASONA DE PIEDRA",
                                    "SanctionAliases|MatchRate": "HOTEL AMANECER|24"
                                },
                                "NormalizedDetails": {
                                    "OriginalName": "HOTEL IPE",
                                    "SanctionName": "HOTEL CASONA DE PIEDRA",
                                    "SanctionAliasesAndMatchRate": "HOTEL AMANECER|24"
                                },
                                "StartDate": "0001-01-01T00:00:00",
                                "EndDate": "9999-12-31T23:59:59.9999999",
                                "CreationDate": "2024-07-17T03:04:21.804",
                                "LastUpdateDate": "2024-07-17T03:04:21.804",
                                "IsCurrentlyPresentOnSource": false,
                                "WasRecentlyPresentOnSource": true
                            }
                        ],
                        "IsCurrentlySanctioned": true
                    }
                }
            ]
        },
        "General": {
            "System": "BigDataCorpKYC",
            "Version": "3.0",
            "Data": {
                "DateTime": "2024-07-17T13:20:00.000Z"
            }
        }
    }'''

    DadosTeste = json.loads(jsonStr)

    return DadosTeste

##################################################################################################
#Socios da Empresa
##################################################################################################
def dadosTeste_BigDataCorp_Socios_Empresa():
    jsonStr = '''
    {
    "DadosEmpresa": {
        "Result": [
            {
                "MatchKeys": "doc{34717533000100}",
                "Relationships": {
                    "Relationships": [
                        {
                            "RelatedEntityTaxIdNumber": "01551772906",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "ROBSON LUIS GARCIA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO-ADMINISTRADOR",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "21556452000124",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "NEXT ADMINISTRACAO DE BENS PROPRIOS LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-01-02T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "21556466000148",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "FIRENZE ADMINISTRACAO DE BENS PROPRIOS LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-01-02T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "28222625000117",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "GJM SERVICOS E PARTICIPACOES LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-12-23T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2023-12-05T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "39494480000120",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "SBOING PARTICIPACOES LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-12-23T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2023-12-05T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "52573721000194",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "INFINITY ADMINISTRADORA DE BENS PROPRIOS LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-12-23T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2023-12-05T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "61530921953",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "JACKSON ANDRE DE SA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "ADMINISTRADOR",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-02-10T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-02-10T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "81212046900",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "SILVANO BOING",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-11-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-11-08T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "81598394053",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "EDUARDO PUTZ",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-11-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-11-08T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "83177957053",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "RAFAEL VIANA TREIN",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-11-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-11-08T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "01551772906",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "ROBSON LUIS GARCIA",
                            "RelationshipType": "REPRESENTANTELEGAL",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-03-11T00:00:00Z",
                            "LastUpdateDate": "2023-03-11T00:00:00Z",
                            "RelationshipStartDate": "2023-03-11T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "07309095901",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "ALINE APARECIDA DA SILVA",
                            "RelationshipType": "Employee",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "MTE",
                            "CreationDate": "2022-08-16T00:00:00Z",
                            "LastUpdateDate": "2022-08-16T00:00:00Z",
                            "RelationshipStartDate": "2021-02-01T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "00801905966",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "MILENA RZATKI NUNES",
                            "RelationshipType": "Employee",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "MTE",
                            "CreationDate": "2022-08-06T00:00:00Z",
                            "LastUpdateDate": "2022-08-06T00:00:00Z",
                            "RelationshipStartDate": "2021-03-01T00:00:00Z",
                            "RelationshipEndDate": "2021-03-24T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "08693075926",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "BRUNA DOS ANJOS",
                            "RelationshipType": "Employee",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "MTE",
                            "CreationDate": "2022-08-20T00:00:00Z",
                            "LastUpdateDate": "2022-08-20T00:00:00Z",
                            "RelationshipStartDate": "2021-09-13T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        }
                    ],
                    "CurrentRelationships": [
                        {
                            "RelatedEntityTaxIdNumber": "01551772906",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "ROBSON LUIS GARCIA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO-ADMINISTRADOR",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "21556452000124",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "NEXT ADMINISTRACAO DE BENS PROPRIOS LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-01-02T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "21556466000148",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "FIRENZE ADMINISTRACAO DE BENS PROPRIOS LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-01-02T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "28222625000117",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "GJM SERVICOS E PARTICIPACOES LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-12-23T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2023-12-05T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "39494480000120",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "SBOING PARTICIPACOES LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-12-23T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2023-12-05T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "52573721000194",
                            "RelatedEntityTaxIdType": "CNPJ",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "INFINITY ADMINISTRADORA DE BENS PROPRIOS LTDA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-12-23T00:00:00Z",
                            "LastUpdateDate": "2024-06-08T00:00:00Z",
                            "RelationshipStartDate": "2023-12-05T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "01551772906",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "ROBSON LUIS GARCIA",
                            "RelationshipType": "REPRESENTANTELEGAL",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2023-03-11T00:00:00Z",
                            "LastUpdateDate": "2023-03-11T00:00:00Z",
                            "RelationshipStartDate": "2023-03-11T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "07309095901",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "ALINE APARECIDA DA SILVA",
                            "RelationshipType": "Employee",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "MTE",
                            "CreationDate": "2022-08-16T00:00:00Z",
                            "LastUpdateDate": "2022-08-16T00:00:00Z",
                            "RelationshipStartDate": "2021-02-01T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "08693075926",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "BRUNA DOS ANJOS",
                            "RelationshipType": "Employee",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "MTE",
                            "CreationDate": "2022-08-20T00:00:00Z",
                            "LastUpdateDate": "2022-08-20T00:00:00Z",
                            "RelationshipStartDate": "2021-09-13T00:00:00Z",
                            "RelationshipEndDate": "9999-12-31T23:59:59.9999999"
                        }
                    ],
                    "HistoricalRelationships": [
                        {
                            "RelatedEntityTaxIdNumber": "61530921953",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "JACKSON ANDRE DE SA",
                            "RelationshipType": "QSA",
                            "RelationshipName": "ADMINISTRADOR",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-02-10T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-02-10T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "81212046900",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "SILVANO BOING",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-11-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-11-08T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "81598394053",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "EDUARDO PUTZ",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-11-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-11-08T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "83177957053",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "RAFAEL VIANA TREIN",
                            "RelationshipType": "QSA",
                            "RelationshipName": "SOCIO",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "RECEITA FEDERAL",
                            "CreationDate": "2019-09-26T00:00:00Z",
                            "LastUpdateDate": "2023-11-08T00:00:00Z",
                            "RelationshipStartDate": "2019-08-30T00:00:00Z",
                            "RelationshipEndDate": "2023-11-08T00:00:00Z"
                        },
                        {
                            "RelatedEntityTaxIdNumber": "00801905966",
                            "RelatedEntityTaxIdType": "CPF",
                            "RelatedEntityTaxIdCountry": "Brazil",
                            "RelatedEntityName": "MILENA RZATKI NUNES",
                            "RelationshipType": "Employee",
                            "RelationshipName": "",
                            "RelationshipLevel": "Direct",
                            "RelationshipDataOrigin": "MTE",
                            "CreationDate": "2022-08-06T00:00:00Z",
                            "LastUpdateDate": "2022-08-06T00:00:00Z",
                            "RelationshipStartDate": "2021-03-01T00:00:00Z",
                            "RelationshipEndDate": "2021-03-24T00:00:00Z"
                        }
                    ],
                    "IsFamilyCompany": false,
                    "IsFamilyOperated": false,
                    "TotalRelationships": 14,
                    "TotalOwners": 10,
                    "TotalEmployees": 3,
                    "TotalOwned": 0
                }
            }
        ],
        "QueryId": "333e5750-6aec-4b1d-9b9b-8f4c0f7c789f",
        "ElapsedMilliseconds": 104,
        "QueryDate": "2024-07-18T14:27:48.0664915Z",
        "Status": {
            "relationships": [
                {
                    "Code": 0,
                    "Message": "OK"
                }
            ]
        },
        "Evidences": {}
    }
}
    '''
    
    DadosTeste = json.loads(jsonStr)
    
    return DadosTeste

##################################################################################################
#Dados teste do Relatorio HTML
##################################################################################################
def dadosTeste_RelatorioProcessos():
    jsonStr = '''
        [
    {
        "Number": "10054042320248260568",
        "CourtType": "CIVEL",
        "Status": "DISTRIBUIDO",
        "Value": 716826,
        "94": null,
        "LastMovementDate": "2025-02-15T00:00:00",
        "LastMovement": "DEFIRO A REALIZACAO DE PENHORA ON-LINE, JUNTO AO SISTEMA SISBAJUD, COM REPETICAO POR 30 DIAS.",
        "Summary": "Ação de execução de título extrajudicial, com valor de R$ 716.826,94, atualmente em trâmite.",
        "Parties": [
        {
            "Type": "CLAIMANT",
            "Name": "BANCO BRADESCO S A",
            "Doc": "60746948000112",
            "Polarity": "ACTIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "LAWYER",
            "Name": "NILTON CARLOS VIEIRA",
            "Doc": "05239642850",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "CLAIMED",
            "Name": "3TM DISTRIBUIDORA DE EMBALAGENS LTDA",
            "Doc": "37819100000154",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "CLAIMED",
            "Name": "TRICIA AMUROV PERES MANTOVANI",
            "Doc": "21661087841",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": false
        },
        {
            "Type": "CLAIMED",
            "Name": "THAIS AMUROV PERES MANTOVANI CALDAS",
            "Doc": "",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": false
        },
        {
            "Type": "REPORTER",
            "Name": "DANILO PINHEIRO SPESSOTTO",
            "Doc": "13752791810",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "LAWYER",
            "Name": "ANDRE PAULA MATTOS CARAVIERI",
            "Doc": "30415311861",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        }
        ],
        "Mentions": {
        "FUNDO": false,
        "FIDC": false,
        "Sec": false,
        "Securitizadora": false
        },
        "Resumo": {
        "Processo": "10054042320248260568",
        "Tipo": "EXECUCAO DE TITULO EXTRAJUDICIAL",
        "AssuntoPrincipal": "ESPECIES DE CONTRATOS",
        "TipoDaCorte": "CIVEL",
        "Status": "DISTRIBUIDO",
        "Valor": 716826,
        "94": null,
        "DataDaUltimaMovimentacao": "2025-02-15T00:00:00",
        "UltimaMovimentacao": "DEFIRO A REALIZACAO DE PENHORA ON-LINE, JUNTO AO SISTEMA SISBAJUD, COM REPETICAO POR 30 DIAS."
        }
    },
    {
        "Number": "10005704020258260568",
        "CourtType": "CIVEL",
        "Status": "DISTRIBUIDO",
        "Value": 183695,
        "88": null,
        "LastMovementDate": "2025-02-12T00:00:00",
        "LastMovement": "MANDADO EXPEDIDO MANDADO N: 568.2025/001713-0 SITUACAO: AGUARDANDO CUMPRIMENTO EM 11/02/2025 LOCAL: OFICIAL DE JUSTICA - REGINA MARTA DE NARDI",
        "Summary": "Ação de execução de título extrajudicial visando ao pagamento do valor de R$183.695,88 decorrente do inadimplemento da CCB N. 866515.",
        "Parties": [
        {
            "Type": "REPORTER",
            "Name": "MISAEL DOS REIS FAGUNDES",
            "Doc": "08782452865",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "CLAIMANT",
            "Name": "COOPERATIVA DE CREDITO CREDINTER LTDA SICOOB CREDINTER",
            "Doc": "",
            "Polarity": "ACTIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "LAWYER",
            "Name": "LIVIA CORREA CRUVINEL",
            "Doc": "09676004642",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "CLAIMED",
            "Name": "3TM DISTRIBUIDORA DE EMBALAGENS LTDA",
            "Doc": "37819100000154",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "CLAIMED",
            "Name": "TRICIA AMUROV PERES MANTOVANI",
            "Doc": "21661087841",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": false
        }
        ],
        "Mentions": {
        "FUNDO": false,
        "FIDC": false,
        "Sec": false,
        "Securitizadora": false
        },
        "Resumo": {
        "Processo": "10005704020258260568",
        "Tipo": "EXECUCAO DE TITULO EXTRAJUDICIAL",
        "AssuntoPrincipal": "CONTRATOS BANCARIOS",
        "TipoDaCorte": "CIVEL",
        "Status": "DISTRIBUIDO",
        "Valor": 183695,
        "88": null,
        "DataDaUltimaMovimentacao": "2025-02-12T00:00:00",
        "UltimaMovimentacao": "MANDADO EXPEDIDO MANDADO N: 568.2025/001713-0 SITUACAO: AGUARDANDO CUMPRIMENTO EM 11/02/2025 LOCAL: OFICIAL DE JUSTICA - REGINA MARTA DE NARDI"
        }
    },
    {
        "Number": "50022483820244036127",
        "CourtType": "TRIBUTARIA",
        "Status": "REDISTRIBUIDO",
        "Value": 0,
        "LastMovementDate": "2025-03-06T00:00:00",
        "LastMovement": "REDISTRIBUIDO POR SORTEIO EM RAZAO DE ALTERACAO DA COMPETENCIA DO ORGAO",
        "Summary": "Ação de execução fiscal em trâmite, com valor não especificado.",
        "Parties": [
        {
            "Type": "CLAIMANT",
            "Name": "UNIAO FEDERAL FAZENDA NACIONAL",
            "Doc": "",
            "Polarity": "ACTIVE",
            "IsCNPJConsulta": false
        },
        {
            "Type": "CLAIMED",
            "Name": "3TM DISTRIBUIDORA DE EMBALAGENS LTDA",
            "Doc": "37819100000154",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        }
        ],
        "Mentions": {
        "FUNDO": false,
        "FIDC": false,
        "Sec": false,
        "Securitizadora": false
        },
        "Resumo": {
        "Processo": "50022483820244036127",
        "Tipo": "EXECUCAO FISCAL",
        "AssuntoPrincipal": "DIREITO TRIBUTARIO (14) - REGIMES ESPECIAIS DE TRIBUTACAO (6089) - SIMPLES (6092",
        "TipoDaCorte": "TRIBUTARIA",
        "Status": "REDISTRIBUIDO",
        "Valor": 0,
        "DataDaUltimaMovimentacao": "2025-03-06T00:00:00",
        "UltimaMovimentacao": "REDISTRIBUIDO POR SORTEIO EM RAZAO DE ALTERACAO DA COMPETENCIA DO ORGAO"
        }
    },
    {
        "Number": "10003591520258260435",
        "CourtType": "CIVEL",
        "Status": "ATIVO",
        "Value": 25680,
        "LastMovementDate": "2025-03-19T00:00:00",
        "LastMovement": "CERTIDAO DE PUBLICACAO EXPEDIDA RELACAO: 0200/2025 DATA DA PUBLICACAO: 20/03/2025 NUMERO DO DIARIO: 4166",
        "Summary": "Ação de protesto indevido de título com valor de R$ 25.680,00 em trâmite.",
        "Parties": [
        {
            "Type": "REPORTER",
            "Name": "IOHANA FRIZZARINI EXPOSITO",
            "Doc": "18805004855",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "CLAIMANT",
            "Name": "KOVALIK EMBALAGENS LTDA",
            "Doc": "30999703000136",
            "Polarity": "ACTIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "LAWYER",
            "Name": "FABIO RODRIGO CAMILOTTI MANIAS",
            "Doc": "28945963839",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "CLAIMED",
            "Name": "3TM DISTRIBUIDORA DE EMBALAGENS LTDA",
            "Doc": "37819100000154",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "CLAIMED",
            "Name": "FUNDO DE INVESTIMENTO EM DIREITOS CREDITORIOS DA INDUSTRIA EXODUS INSTITUCIONAL",
            "Doc": "14051028000162",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "CLAIMED",
            "Name": "TRUSTHUB SECURITIZADORA S A",
            "Doc": "02211906000180",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        }
        ],
        "Mentions": {
        "FUNDO": true,
        "FIDC": false,
        "Sec": false,
        "Securitizadora": true
        },
        "Resumo": {
        "Processo": "10003591520258260435",
        "Tipo": "PROCEDIMENTO COMUM",
        "AssuntoPrincipal": "PROTESTO INDEVIDO DE TITULO",
        "TipoDaCorte": "CIVEL",
        "Status": "ATIVO",
        "Valor": 25680,
        "DataDaUltimaMovimentacao": "2025-03-19T00:00:00",
        "UltimaMovimentacao": "CERTIDAO DE PUBLICACAO EXPEDIDA RELACAO: 0200/2025 DATA DA PUBLICACAO: 20/03/2025 NUMERO DO DIARIO: 4166"
        }
    },
    {
        "Number": "08004544920258205106",
        "CourtType": "CIVEL",
        "Status": "DISTRIBUIDO",
        "Value": -1,
        "LastMovementDate": "2025-03-11T00:00:00",
        "LastMovement": "DISTRIBUIDO POR SORTEIO",
        "Summary": "Ação distribuída no Juizado Especial Cível, com pedido de tutela antecipada deferido para suspensão de protesto.",
        "Parties": [
        {
            "Type": "AUTHOR",
            "Name": "PAMELLA FABRICIA NEGREIROS DE MORAIS",
            "Doc": "26309699000160",
            "Polarity": "ACTIVE",
            "IsCNPJConsulta": false
        },
        {
            "Type": "LAWYER",
            "Name": "GEORGE BEZERRA FILGUEIRA FILHO 9640",
            "Doc": "01438032471",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "DEFENDANT",
            "Name": "3TM DISTRIBUIDORA DE EMBALAGENS LTDA",
            "Doc": "37819100000154",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "DEFENDANT",
            "Name": "DOVER SECURITIZADORA S A",
            "Doc": "28057482000135",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "DEFENDANT",
            "Name": "BANCO BRADESCO S A",
            "Doc": "60746948000112",
            "Polarity": "PASSIVE",
            "IsCNPJConsulta": true
        },
        {
            "Type": "LAWYER",
            "Name": "ELIANE ZINI VIANA HENRIQUE",
            "Doc": "22003132848",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        },
        {
            "Type": "LAWYER",
            "Name": "CARLOS AUGUSTO MONTEIRO NASCIMENTO",
            "Doc": "76607810730",
            "Polarity": "NEUTRAL",
            "IsCNPJConsulta": false
        }
        ],
        "Mentions": {
        "FUNDO": false,
        "FIDC": false,
        "Sec": false,
        "Securitizadora": true
        },
        "Resumo": {
        "Processo": "08004544920258205106",
        "Tipo": "PROCEDIMENTO DO JUIZADO ESPECIAL CIVEL",
        "AssuntoPrincipal": "DIREITO DO CONSUMIDOR (1156) - RESPONSABILIDADE DO FORNECEDOR (6220) - INDENIZACAO POR DANO MORAL (7779) - PROTESTO INDEVIDO DE TITULO (7781",
        "TipoDaCorte": "CIVEL",
        "Status": "DISTRIBUIDO",
        "Valor": -1,
        "DataDaUltimaMovimentacao": "2025-03-11T00:00:00",
        "UltimaMovimentacao": "DISTRIBUIDO POR SORTEIO"
        }
    }
    ]
    '''
   
    DadosTeste = json.loads(jsonStr)
    
    return DadosTeste

##################################################################################################
#Dados Bureau Processos
##################################################################################################
def dadosTeste_BureauProcessos():
    jsonStr = '''
    {
        "Result": [
            {
                "MatchKeys": "doc{23271029000103}",
                "BasicData": {
                    "TaxIdNumber": "23271029000103",
                    "TaxIdCountry": "Brazil",
                    "AlternativeIdNumbers": {},
                    "OfficialName": "VST ARTIGOS DO VESTUARIO LTDA",
                    "TradeName": "VST CONFECCOES",
                    "Aliases": {
                        "UnstandardizedRFOfficialName": "VST ARTIGOS DO VESTUARIO LTDA",
                        "UnstandardizedRFTradeName": "VST CONFECCOES"
                    },
                    "NameUniquenessScore": 1,
                    "OfficialNameUniquenessScore": 1,
                    "TradeNameUniquenessScore": 0.33333333,
                    "FoundedDate": "2015-09-14T00:00:00Z",
                    "ClosedDate": "2022-03-10T00:00:00Z",
                    "Age": 9,
                    "IsHeadquarter": true,
                    "HeadquarterState": "SC",
                    "IsConglomerate": false,
                    "TaxIdStatus": "BAIXADA",
                    "TaxIdOrigin": "Receita Federal",
                    "TaxIdStatusDate": "2025-03-07T00:00:00Z",
                    "TaxIdStatusRegistrationDate": "2022-03-10T00:00:00Z",
                    "TaxRegime": "NAO ATIVA",
                    "CompanyType_ReceitaFederal": "ME",
                    "TaxRegimes": {
                        "Simples": false
                    },
                    "Activities": [],
                    "LegalNature": {
                        "Code": "2062",
                        "Activity": "SOCIEDADE EMPRESARIA LIMITADA"
                    },
                    "SpecialSituation": "",
                    "CreationDate": "2015-09-14T00:00:00Z",
                    "LastUpdateDate": "2025-03-07T00:00:00Z",
                    "AdditionalOutputData": {
                        "Capital": "TRINTA MIL REAIS",
                        "CapitalRS": "30000.00",
                        "NIRE": "",
                        "NIRECompanySize": "",
                        "NIREHeadquartersType": "",
                        "NIREHeadquartersCapital": "0",
                        "NIRELastCaptureDate": "0001-01-01T12:00:00Z",
                        "COMEX": "PESSOA NAO HABILITADA A OPERAR NO COMERCIO EXTERIOR",
                        "COMEXLastUpdate": "2020-10-21T12:00:00Z"
                    },
                    "HistoricalData": {
                        "HasChangedTradeName": false,
                        "HasChangedTaxRegime": true,
                        "HistoricalDataEvolution": {
                            "TradeName": [
                                {
                                    "Value": "VST CONFECCOES",
                                    "StartDate": "2015-09-14T00:00:00Z"
                                }
                            ],
                            "TaxRegime": [
                                {
                                    "Value": "NAO ATIVA",
                                    "StartDate": "2022-02-01T00:00:00Z"
                                },
                                {
                                    "Value": "SIMPLES",
                                    "StartDate": "2017-08-01T00:00:00Z",
                                    "EndDate": "2022-02-01T00:00:00Z"
                                },
                                {
                                    "Value": "NAO DEFINIDO",
                                    "StartDate": "2017-03-01T00:00:00Z",
                                    "EndDate": "2017-08-01T00:00:00Z"
                                },
                                {
                                    "Value": "EPP",
                                    "StartDate": "2015-09-14T00:00:00Z",
                                    "EndDate": "2017-03-01T00:00:00Z"
                                }
                            ]
                        }
                    }
                },
                "Lawsuits": {
                    "Lawsuits": [
                        {
                            "Number": "51035637520218240023",
                            "Type": "EXECUCAO FISCAL",
                            "MainSubject": "0312 | DIVIDA ATIVA (EXECUCAO FISCAL), DIREITO TRIBUTARIO",
                            "CourtName": "TJSC",
                            "CourtLevel": "1",
                            "CourtType": "TRIBUTARIA",
                            "CourtDistrict": "FLORIANOPOLIS",
                            "Judge": "JOAO BAPTISTA VIEIRA SELL",
                            "JudgingBody": "1 JUIZO DA UNIDADE REGIONAL DE EXECUCOES FISCAIS MUNICIPAIS DA COMARCA DA CAPITAL",
                            "State": "SC",
                            "Status": "ARQUIVADO",
                            "LawsuitHostService": "OTHER",
                            "InferredCNJSubjectName": "DÍVIDA ATIVA (EXECUÇÃO FISCAL)",
                            "InferredCNJSubjectNumber": 6017,
                            "InferredCNJProcedureTypeName": "EXECUÇÃO FISCAL",
                            "InferredCNJProcedureTypeNumber": 1116,
                            "InferredBroadCNJSubjectName": "DIREITO TRIBUTÁRIO",
                            "InferredBroadCNJSubjectNumber": 14,
                            "OtherSubjects": [
                                "0312",
                                "DIVIDA ATIVA (EXECUCAO FISCAL), DIREITO TRIBUTARIO"
                            ],
                            "NumberOfVolumes": 0,
                            "NumberOfPages": 0,
                            "Value": 752.32,
                            "ResJudicataDate": "2024-09-12T16:42:00",
                            "CloseDate": "2024-09-12T16:42:00",
                            "RedistributionDate": "0001-01-01T00:00:00",
                            "PublicationDate": "0001-01-01T00:00:00",
                            "NoticeDate": "2021-12-15T13:56:00",
                            "LastMovementDate": "2024-09-12T16:42:00",
                            "CaptureDate": "2024-09-19T08:09:11",
                            "LastUpdate": "2024-09-19T08:09:11",
                            "NumberOfParties": 7,
                            "NumberOfUpdates": 18,
                            "LawSuitAge": 1002,
                            "AverageNumberOfUpdatesPerMonth": 0,
                            "ReasonForConcealedData": 0,
                            "Parties": [
                                {
                                    "Doc": "01434874931",
                                    "IsPartyActive": false,
                                    "Name": "GABRIELA SAILON DE SOUZA BENEDET",
                                    "Polarity": "NEUTRAL",
                                    "Type": "REPORTER",
                                    "IsInference": true,
                                    "PartyDetails": {
                                        "SpecificType": "JUIZ(A)"
                                    },
                                    "LastCaptureDate": "2024-04-01T01:43:57"
                                },
                                {
                                    "Doc": "83102491000109",
                                    "IsPartyActive": true,
                                    "Name": "MUNICIPIO DE SCHROEDER SC",
                                    "Polarity": "ACTIVE",
                                    "Type": "CLAIMANT",
                                    "IsInference": false,
                                    "PartyDetails": {
                                        "SpecificType": "EXEQUENTE"
                                    },
                                    "LastCaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Doc": "06269274982",
                                    "IsPartyActive": true,
                                    "Name": "CAMILA RODRIGUES BASTOS",
                                    "Polarity": "NEUTRAL",
                                    "Type": "LAWYER",
                                    "IsInference": true,
                                    "PartyDetails": {
                                        "OAB": "036637",
                                        "State": "SC",
                                        "SpecificType": "ADVOGADO (EXEQUENTE)"
                                    },
                                    "LastCaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Doc": "00439503108",
                                    "IsPartyActive": false,
                                    "Name": "DANIEL DE MELLO MASSIMINO",
                                    "Polarity": "NEUTRAL",
                                    "Type": "LAWYER",
                                    "IsInference": true,
                                    "PartyDetails": {
                                        "OAB": "027807",
                                        "State": "SC",
                                        "SpecificType": "ADVOGADO (EXEQUENTE)"
                                    },
                                    "LastCaptureDate": "2023-02-09T17:15:16"
                                },
                                {
                                    "Doc": "23271029000103",
                                    "IsPartyActive": true,
                                    "Name": "VST ARTIGOS DO VESTUARIO LTDA",
                                    "Polarity": "PASSIVE",
                                    "Type": "CLAIMED",
                                    "IsInference": false,
                                    "PartyDetails": {
                                        "SpecificType": "EXECUTADO"
                                    },
                                    "LastCaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Doc": "05231137901",
                                    "IsPartyActive": true,
                                    "Name": "DIEGO AUGUSTO BAYER",
                                    "Polarity": "NEUTRAL",
                                    "Type": "LAWYER",
                                    "IsInference": true,
                                    "PartyDetails": {
                                        "OAB": "028822",
                                        "State": "MS",
                                        "SpecificType": "ADVOGADO (EXEQUENTE)"
                                    },
                                    "LastCaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Doc": "02871885907",
                                    "IsPartyActive": true,
                                    "Name": "JOAO BAPTISTA VIEIRA SELL",
                                    "Polarity": "NEUTRAL",
                                    "Type": "REPORTER",
                                    "IsInference": true,
                                    "PartyDetails": {
                                        "SpecificType": "JUIZ(A)"
                                    },
                                    "LastCaptureDate": "2024-09-19T08:09:11"
                                }
                            ],
                            "Updates": [
                                {
                                    "Content": "BAIXA DEFINITIVA",
                                    "PublishDate": "2024-09-12T16:42:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "TRANSITADO EM JULGADO",
                                    "PublishDate": "2024-09-12T16:42:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "CIENCIA, COM RENUNCIA AO PRAZO - REFER. AO EVENTO: 13",
                                    "PublishDate": "2024-09-02T16:12:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "CONFIRMADA A INTIMACAO ELETRONICA - REFER. AO EVENTO: 13",
                                    "PublishDate": "2024-08-15T23:59:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "EXPEDIDA/CERTIFICADA A INTIMACAO ELETRONICA - SENTENCAREFER. AO EVENTO 12(EXEQUENTE - MUNICIPIO DE SCHROEDER/SC) PRAZO: 30 DIAS STATUS:FECHADO DATA INICIAL DA CONTAGEM DO PRAZO: 16/08/2024 00:00:00 DATA FINAL: 26/09/2024 23:59:59",
                                    "PublishDate": "2024-08-05T16:02:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "EXTINTO O PROCESSO POR AUSENCIA DAS CONDICOES DA ACAO - TIPO C | ESTADO DE SANTA CATARINA PODER JUDICIARIO UNIDADE REGIONAL DE EXECUCOES FISCAIS MUNICIPAIS DA COMARCA DA CAPITAL RUA PRESIDENTE COUTINHO, 232, SALA 202 - BAIRRO: CENTRO - CEP: 88015-230 - FONE: (48) 3287-7330 - WHATSAPP: (48) 3287-7340 - EMAIL: CAPITAL.REGIONALFISCAL@TJSC.JUS.BR EXECUCAO FISCAL N 5103563-75.2021.8.24.0023/ SC EXEQUENTE : MUNICIPIO DE SCHROEDER/SC EXECUTADO : VST ARTIGOS DO VESTUARIO LTDA SENTENCA RELATORIO TRATA-SE DE EXECUCAO FISCAL DE TRIBUTO MUNICIPAL. O FEITO TRAMITOU SEM A SATISFACAO DO DEBITO OU GARANTIA DO JUIZO E, APOS INTIMACAO DO ENTE MUNICIPAL PARA MANIFESTAR-SE ACERCA DO PROSSEGUIMENTO DO FEITO, OS AUTOS VIERAM CONCLUSOS. FUNDAMENTACAO PRIMEIRAMENTE, DESTACO QUE O SUPREMO TRIBUNAL FEDERAL, AO JULGAR O TEMA N. 1184 EM 19/12/2023, NO AMBITO DO RECURSO EXTRAORDINARIO N. 1.355.208, REL. MINISTRA CARMEN LUCIA, RECONHECEU A LEGITIMIDADE DA EXTINCAO DE EXECUCOES FISCAIS DE BAIXO VALOR PELA FALTA DE INTERESSE PROCESSUAL, EM CONSONANCIA COM O PRINCIPIO CONSTITUCIONAL DA EFICIENCIA ADMINISTRATIVA, RESPEITADA A COMPETENCIA DE CADA ENTE FEDERADO. TAL DECISAO ESTABELECEU QUE O AJUIZAMENTO DE EXECUCAO FISCAL DEVE SER PRECEDIDO DA TENTATIVA DE CONCILIACAO OU SOLUCAO ADMINISTRATIVA, ALEM DO PROTESTO DO TITULO, EXCETO POR MOTIVO DE EFICIENCIA ADMINISTRATIVA. NESSE SENTIDO E O TEOR DA EMENTA DO JULGADO QUE FIXOU A SEGUINTE TESE JURIDICA, DE EFEITO VINCULANTE (CPC, ART. 927, III): 1. E LEGITIMA A EXTINCAO DE EXECUCAO FISCAL DE BAIXO VALOR PELA AUSENCIA DE INTERESSE DE AGIR TENDO EM VISTA O PRINCIPIO CONSTITUCIONAL DA EFICIENCIA ADMINISTRATIVA, RESPEITADA A COMPETENCIA CONSTITUCIONAL DE CADA ENTE FEDERADO. 2. O AJUIZAMENTO DA EXECUCAO FISCAL DEPENDERA DA PREVIA ADOCAO DAS SEGUINTES PROVIDENCIAS: A) TENTATIVA DE CONCILIACAO OU ADOCAO DE SOLUCAO ADMINISTRATIVA; E B) PROTESTO DO TITULO, SALVO POR MOTIVO DE EFICIENCIA ADMINISTRATIVA, COMPROVANDO-SE A INADEQUACAO DA MEDIDA. 3. O TRAMITE DE ACOES DE EXECUCAO FISCAL NAO IMPEDE OS ENTES FEDERADOS DE PEDIREM A SUSPENSAO DO PROCESSO PARA A ADOCAO DAS MEDIDAS PREVISTAS NO ITEM 2, DEVENDO, NESSE CASO, O JUIZ SER COMUNICADO DO PRAZO PARA AS PROVIDENCIAS CABIVEIS. (RECURSO EXTRAORDINARIO N. 1.355.208, REL. MINISTRA CARMEN LUCIA) COMO BEM PONDERADO PELO MINISTRO LUIS ROBERTO BARROSO, NAS DISCUSSOES QUE PERMEARAM O JULGAMENTO QUE REDUNDOU NA FIXACAO DESSA TESE, \"ESSE TEMA ESPECIFICO SE INSERE NO TEMA ESSENCIAL DO SECULO PARA O SISTEMA DE JUSTICA, QUE E UMA BUSCA DE MELHOR EFICIENCIA, COMO UM TODO, DO PODER JUDICIARIO. MELHOR EXECUCAO DE ORCAMENTOS, MELHOR GESTAO DE PROCESSOS E MELHOR DEFINICAO DE PRIORIDADES, NO AMBITO DA ATUACAO JUDICIAL COMO UM TODO.\" A PARTIR DESSE JULGAMENTO E DE FORMA ADICIONAL, O CONSELHO NACIONAL DE JUSTICA, AO APROVAR POR UNANIMIDADE A RESOLUCAO N. 547/2024, REFORCOU A TESE FIRMADA PELO STF, ESTABELECENDO CRITERIOS PARA A EXTINCAO DE EXECUCOES FISCAIS DE VALOR ATE DEZ MIL REAIS, BEM COMO DAQUELAS SEM MOVIMENTACAO HA MAIS DE UM ANO, EM QUE NAO TENHAM SIDO ENCONTRADOS BENS PENHORAVEIS, CITADO OU NAO O EXECUTADO. COLHE-SE DA INTEGRA DO DOCUMENTO: O PRESIDENTE DO CONSELHO NACIONAL DE JUSTICA (CNJ), NO USO DE SUAS ATRIBUICOES LEGAIS E REGIMENTAIS, CONSIDERANDO QUE, SEGUNDO O RELATORIO JUSTICA EM NUMEROS 2023 (ANO-BASE 2022), AS EXECUCOES FISCAIS TEM SIDO APONTADAS COMO O PRINCIPAL FATOR DE MOROSIDADE DO PODER JUDICIARIO, RESPONDENDO POR 34% DO ACERVO PENDENTE, COM TAXA DE CONGESTIONAMENTO DE 88% E TEMPO MEDIO DE TRAMITACAO DE 6 ANOS E 7 MESES ATE A BAIXA; CONSIDERANDO O JULGAMENTO, EM 19/12/2023, PELO PLENARIO DO SUPREMO TRIBUNAL FEDERAL, DO RECURSO EXTRAORDINARIO N 1.355.208, REL. MIN. CARMEN LUCIA, EM REGIME DE REPERCUSSAO GERAL (TEMA 1184); CONSIDERANDO QUE, NO REFERIDO PRECEDENTE, FICOU DECIDIDO QUE: 1. E LEGITIMA A EXTINCAO DE EXECUCAO FISCAL DE BAIXO VALOR PELA AUSENCIA DE INTERESSE DE AGIR TENDO EM VISTA O PRINCIPIO CONSTITUCIONAL DA EFICIENCIA ADMINISTRATIVA, RESPEITADA A COMPETENCIA CONSTITUCIONAL DE CADA ENTE FEDERADO. 2. O AJUIZAMENTO DA EXECUCAO FISCAL DEPENDERA DA PREVIA ADOCAO DAS SEGUINTES PROVIDENCIAS: A) TENTATIVA DE CONCILIACAO OU ADOCAO DE SOLUCAO ADMINISTRATIVA; E B) PROTESTO DO TITULO, SALVO POR MOTIVO DE EFICIENCIA ADMINISTRATIVA, COMPROVANDO-SE A INADEQUACAO DA MEDIDA. 3. O TRAMITE DE ACOES DE EXECUCAO FISCAL NAO IMPEDE OS ENTES FEDERADOS DE PEDIREM A SUSPENSAO DO PROCESSO PARA A ADOCAO DAS MEDIDAS PREVISTAS NO ITEM 2, DEVENDO, NESSE CASO, O JUIZ SER COMUNICADO DO PRAZO PARA AS PROVIDENCIAS CABIVEIS; CONSIDERANDO O EXPOSTO NAS NOTAS TECNICAS N 06/2023 E 08/2023, AMBAS DO NUCLEO DE PROCESSOS ESTRUTURAIS E COMPLEXOS DO STF, CITADAS NO JULGADO ACIMA, SEGUNDO AS QUAIS O CUSTO MINIMO DE UMA EXECUCAO FISCAL, COM BASE NO VALOR DA MAO DE OBRA, E DE R$ 9.277,00 (NOVE MIL, DUZENTOS E SETENTA E SETE REAIS), E QUE O PROTESTO DE CERTIDOES DE DIVIDA ATIVA COSTUMA SER MAIS EFICAZ QUE O AJUIZAMENTO DE EXECUCOES FISCAIS; CONSIDERANDO QUE, SEGUNDO LEVANTAMENTO DO CNJ TAMBEM CITADO NO JULGAMENTO, ESTIMA-SE QUE MAIS DA METADE (52,3%) DAS EXECUCOES FISCAIS TEM VALOR DE AJUIZAMENTO ABAIXO DE R$ 10.000,00 (DEZ MIL REAIS); CONSIDERANDO A INTERPRETACAO DO STJ (TEMA 566 DOS RECURSOS ESPECIAIS REPETITIVOS), VALIDADA PELO STF (TEMA 390 DA REPERCUSSAO GERAL) SOBRE O TERMO INICIAL DO PRAZO PRESCRICIONAL APOS A PROPOSITURA DA ACAO; CONSIDERANDO A DECISAO TOMADA PELO PLENARIO DO CNJ NO JULGAMENTO DO ATO NORMATIVO N 0000732-68.2024.2.00.0000, NA 1 SESSAO ORDINARIA, REALIZADA EM 20 DE FEVEREIRO DE 2024; RESOLVE: ART. 1 E LEGITIMA A EXTINCAO DE EXECUCAO FISCAL DE BAIXO VALOR PELA AUSENCIA DE INTERESSE DE AGIR, TENDO EM VISTA O PRINCIPIO CONSTITUCIONAL DA EFICIENCIA ADMINISTRATIVA, RESPEITADA A COMPETENCIA CONSTITUCIONAL DE CADA ENTE FEDERADO.  1 DEVERAO SER EXTINTAS AS EXECUCOES FISCAIS DE VALOR INFERIOR A R$ 10.000,00 (DEZ MIL REAIS) QUANDO DO AJUIZAMENTO, EM QUE NAO HAJA MOVIMENTACAO UTIL HA MAIS DE UM ANO SEM CITACAO DO EXECUTADO OU, AINDA QUE CITADO, NAO TENHAM SIDO LOCALIZADOS BENS PENHORAVEIS.  2 PARA AFERICAO DO VALOR PREVISTO NO  1, EM CADA CASO CONCRETO, DEVERAO SER SOMADOS OS VALORES DE EXECUCOES QUE ESTEJAM APENSADAS E PROPOSTAS EM FACE DO MESMO EXECUTADO.  3 O DISPOSTO NO  1 NAO IMPEDE NOVA PROPOSITURA DA EXECUCAO FISCAL SE FOREM ENCONTRADOS BENS DO EXECUTADO, DESDE QUE NAO CONSUMADA A PRESCRICAO.  4 NA HIPOTESE DO  3, O PRAZO PRESCRICIONAL PARA NOVA PROPOSITURA TERA COMO TERMO INICIAL UM ANO APOS A DATA DA CIENCIA DA FAZENDA PUBLICA A RESPEITO DA NAO LOCALIZACAO DO DEVEDOR OU DA INEXISTENCIA DE BENS PENHORAVEIS NO PRIMEIRO AJUIZAMENTO.  5 A FAZENDA PUBLICA PODERA REQUERER NOS AUTOS A NAO APLICACAO, POR ATE 90 (NOVENTA) DIAS, DO  1 DESTE ARTIGO, CASO DEMONSTRE QUE, DENTRO DESSE PRAZO, PODERA LOCALIZAR BENS DO DEVEDOR. ART. 2 O AJUIZAMENTO DE EXECUCAO FISCAL DEPENDERA DE PREVIA TENTATIVA DE CONCILIACAO OU ADOCAO DE SOLUCAO ADMINISTRATIVA.  1 A TENTATIVA DE CONCILIACAO PODE SER SATISFEITA, EXEMPLIFICATIVAMENTE, PELA EXISTENCIA DE LEI GERAL DE PARCELAMENTO OU OFERECIMENTO DE ALGUM TIPO DE VANTAGEM NA VIA ADMINISTRATIVA, COMO REDUCAO OU EXTINCAO DE JUROS OU MULTAS, OU OPORTUNIDADE CONCRETA DE TRANSACAO NA QUAL O EXECUTADO, EM TESE, SE ENQUADRE.  2 A NOTIFICACAO DO EXECUTADO PARA PAGAMENTO ANTES DO AJUIZAMENTO DA EXECUCAO FISCAL CONFIGURA ADOCAO DE SOLUCAO ADMINISTRATIVA.  3 PRESUME-SE CUMPRIDO O DISPOSTO NOS  1 E 2 QUANDO A PROVIDENCIA ESTIVER PREVISTA EM ATO NORMATIVO DO ENTE EXEQUENTE. ART. 3 O AJUIZAMENTO DA EXECUCAO FISCAL DEPENDERA, AINDA, DE PREVIO PROTESTO DO TITULO, SALVO POR MOTIVO DE EFICIENCIA ADMINISTRATIVA, COMPROVANDO-SE A INADEQUACAO DA MEDIDA. PARAGRAFO UNICO. PODE SER DISPENSADA A EXIGENCIA DO PROTESTO NAS SEGUINTES HIPOTESES, SEM PREJUIZO DE OUTRAS, CONFORME ANALISE DO JUIZ NO CASO CONCRETO: I  COMUNICACAO DA INSCRICAO EM DIVIDA ATIVA AOS ORGAOS QUE OPERAM BANCOS DE DADOS E CADASTROS RELATIVOS A CONSUMIDORES E AOS SERVICOS DE PROTECAO AO CREDITO E CONGENERES (LEI N 10.522/2002, ART. 20-B,  3, I); II  EXISTENCIA DA AVERBACAO, INCLUSIVE POR MEIO ELETRONICO, DA CERTIDAO DE DIVIDA ATIVA NOS ORGAOS DE REGISTRO DE BENS E DIREITOS SUJEITOS A ARRESTO OU PENHORA (LEI N 10.522/2002, ART. 20-B,  3, II); OU III  INDICACAO, NO ATO DE AJUIZAMENTO DA EXECUCAO FISCAL, DE BENS OU DIREITOS PENHORAVEIS DE TITULARIDADE DO EXECUTADO. ART. 4 OS CARTORIOS DE NOTAS E DE REGISTRO DE IMOVEIS DEVERAO COMUNICAR AS RESPECTIVAS PREFEITURAS, EM PERIODICIDADE NAO SUPERIOR A 60 (SESSENTA) DIAS, TODAS AS MUDANCAS NA TITULARIDADE DE IMOVEIS REALIZADAS NO PERIODO, A FIM DE PERMITIR A ATUALIZACAO CADASTRAL DOS CONTRIBUINTES DAS FAZENDAS MUNICIPAIS. ART. 5 ESTA RESOLUCAO ENTRA EM VIGOR NA DATA DA SUA PUBLICACAO\". CONSIDERANDO TAIS DIRETRIZES, O GABINETE DA PRESIDENCIA E A CORREGEDORIA GERAL DE JUSTICA DESTE TRIBUNAL DE JUSTICA EMITIRAM A ORIENTACAO CONJUNTA GP/CGJ N. 01/2024, RECOMENDANDO A EXTINCAO DE EXECUCOES FISCAIS DE BAIXO VALOR E PRESCRITAS, BEM COMO DAQUELAS COM VALOR INFERIOR A R$ 10.000,00 (DEZ MIL REAIS) POR EXECUTADO, EM CASOS DE AUSENCIA DE MOVIMENTACAO PROCESSUAL UTIL HA MAIS DE UM ANO SEM CITACAO DO EXECUTADO OU, MESMO CITADO, DE INEXISTENCIA DE BENS PENHORAVEIS, IN VERBIS : ART. 1 RECOMENDA-SE QUE OS PROCESSOS DE EXECUCAO FISCAL EM TRAMITE NO PODER JUDICIARIO DE SANTA CATARINA CONSIDEREM O TEMA N. 1.184 DO SUPREMO TRIBUNAL FEDERAL E A RESOLUCAO N. 547 DE 22 DE FEVEREIRO DE 2024 DO CONSELHO NACIONAL DE JUSTICA, CONFORME AS DEFINICOES DESTA ORIENTACAO CONJUNTA. ART. 2 RECOMENDA-SE AOS JUIZES COM COMPETENCIA EM EXECUCAO FISCAL A EXTINCAO DOS PROCESSOS DE EXECUCAO FISCAL: I  DE BAIXO VALOR, RESPEITADO O VALOR MINIMO DEFINIDO POR CADA ENTE FEDERADO; II  PRESCRITOS; III  COM VALOR INFERIOR A R$ 10.000,00 (DEZ MIL REAIS) POR EXECUTADO NO MOMENTO DO AJUIZAMENTO, EM QUE: A) NAO HAJA MOVIMENTACAO PROCESSUAL UTIL HA MAIS DE UM ANO SEM CITACAO DO EXECUTADO; OU B) AINDA QUE CITADO, NAO TENHAM SIDO LOCALIZADOS BENS PENHORAVEIS.  1 SUGERE-SE QUE AS SENTENCAS DE EXTINCAO SEJAM PRECEDIDAS DE PREVIA INTIMACAO DAS PARTES EXEQUENTES.  2 NA HIPOTESE DE INEXISTENCIA DE LEGISLACAO PROPRIA OU DE VALOR DESPROPORCIONALMENTE BAIXO, PODE SER CONSIDERADA LEGITIMA A EXTINCAO DA ACAO OU O INDEFERIMENTO DA PETICAO INICIAL, DE ACORDO COM O INCISO I DO CAPUT DESTE ARTIGO, COM VALORES INFERIORES A R$ 2.800,00 (DOIS MIL E OITOCENTOS REAIS).  3 NA HIPOTESE DO INCISO III DO CAPUT DESTE ARTIGO, A FAZENDA PUBLICA INTERESSADA PODERA REQUERER NOS AUTOS A NAO APLICACAO, POR ATE 90 (NOVENTA) DIAS, DA EXTINCAO DA EXECUCAO FISCAL, DESDE QUE DEMONSTRE QUE, DENTRE DESTE PRAZO, PODERA LOCALIZAR BENS DO DEVEDOR. INDUVIDOSO QUE AS MEDIDAS DE SANEAMENTO RECOMENDADAS IMPLICAM EM UM CONTRIBUTIVO SIGNIFICATIVO PARA A BOA GESTAO DO SISTEMA DE JUSTICA COMO UM TODO, EVITANDO QUE SE DE PROSSEGUIMENTO A EXECUCOES FISCAIS CONSIDERADAS DE VALOR ANTIECONOMICO E RESERVANDO A ACAO DE EXECUCAO FISCAL PARA OS CASOS DE VALORES EXPRESSIVOS E DESDE QUE DEMONSTRADO O INSUCESSO DAS MEDIDAS. NO PRESENTE CASO, VERIFICO QUE O VALOR DA EXECUCAO FISCAL EM QUESTAO NAO JUSTIFICA A MANUTENCAO DO PROCESSO JUDICIAL, CONFORME OS CRITERIOS ESTABELECIDOS NAS NORMATIVAS MENCIONADAS, QUEDANDO-SE ABAIXO, INCLUSIVE, DE 50 ORTNS, SENDO INCABIVEL O RECURSO DE APELACAO, A TEOR DO ART. 34 DA LEI DE EXECUCAO FISCAL. NESSE CONTEXTO, A CONTINUIDADE DA EXECUCAO FISCAL NAO SE MOSTRA ECONOMICAMENTE JUSTIFICADA A LUZ DOS PRINCIPIOS DA EFICIENCIA ADMINISTRATIVA E DA ECONOMICIDADE (CF, ARTS. 37, CAPUT E 70, CAPUT ). PORTANTO, A EXTINCAO DO PROCESSO POR FALTA DE INTERESSE PROCESSUAL E JUSTIFICAVEL, CONSIDERANDO A EXISTENCIA DE OUTRA VIA E A RELACAO ENTRE CUSTO OPERACIONAL E BENEFICIO ECONOMICO DO PROSSEGUIMENTO DO FEITO. E IMPORTANTE RESSALTAR QUE O ENCERRAMENTO DESTA EXECUCAO FISCAL NAO RESULTA NA EXTINCAO DO CREDITO TRIBUTARIO, MAS SIM NA OTIMIZACAO E RACIONALIZACAO DOS MEIOS DE SUA SATISFACAO. DISPOSITIVO DIANTE DO EXPOSTO, JULGO EXTINTO O PROCESSO SEM RESOLUCAO DO MERITO, NOS TERMOS DOS ARTIGOS 485, INCISO VI, E 927, III, DO CODIGO DE PROCESSO CIVIL; ARTS. 1,  1, DA RESOLUCAO CNJ N. 547/2024 E ART. 2 DA ORIENTACAO CONJUNTA GP/CGJ N. 01/2024. NO CASO DE EXISTENCIA DE ALGUMA RESTRICAO, A MESMA DEVERA SER LEVANTADA. EVENTUAIS VALORES DEVERAO SER REVERTIDOS EM FAVOR DA PARTE CREDORA. SEM CUSTAS E HONORARIOS. PUBLIQUE-SE. REGISTRE-SE. INTIMEM-SE. APOS O TRANSITO EM JULGADO E NAO HAVENDO MAIS QUESTOES PENDENTES OU PROVIDENCIAS A SEREM CUMPRIDAS, PROCEDA-SE AO ARQUIVAMENTO DO PROCESSO, COM AS BAIXAS PERTINENTES. DOCUMENTO ELETRONICO ASSINADO POR CLEUSA MARIA CARDOSO, JUIZA DE DIREITO , NA FORMA DO ARTIGO 1, INCISO III, DA LEI 11.419, DE 19 DE DEZEMBRO DE 2006. A CONFERENCIA DA AUTENTICIDADE DO DOCUMENTO ESTA DISPONIVEL NO ENDERECO ELETRONICO HTTPS://EPROC1G.TJSC.JUS.BR/EPROC/EXTERNO_CONTROLADOR.PHP?ACAO=CONSULTA_AUTENTICIDADE_DOCUMENTOS, MEDIANTE O PREENCHIMENTO DO CODIGO VERIFICADOR 310063205590V1 E DO CODIGO CRC B3507D12 . INFORMACOES ADICIONAIS DA ASSINATURA: SIGNATARIO (A): CLEUSA MARIA CARDOSO DATA E HORA: 5/8/2024, AS 16:2:16 5103563-75.2021.8.24.0023 310063205590 .V1",
                                    "PublishDate": "2024-08-05T16:02:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "CONCLUSOS PARA JULGAMENTO",
                                    "PublishDate": "2024-08-05T15:37:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "PEDIDO DE EXTINCAO DO PROCESSO - REFER. AO EVENTO: 8",
                                    "PublishDate": "2024-08-05T10:31:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "CONFIRMADA A INTIMACAO ELETRONICA - REFER. AO EVENTO: 8",
                                    "PublishDate": "2024-07-16T23:59:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "EXPEDIDA/CERTIFICADA A INTIMACAO ELETRONICAREFER. AO EVENTO 7(EXEQUENTE - MUNICIPIO DE SCHROEDER/SC) PRAZO: 14 DIAS STATUS:AGUARD. ABERTURA",
                                    "PublishDate": "2024-07-06T05:30:00",
                                    "CaptureDate": "2024-07-10T19:59:33"
                                },
                                {
                                    "Content": "ATO ORDINATORIO PRATICADO | ESTADO DE SANTA CATARINA PODER JUDICIARIO UNIDADE REGIONAL DE EXECUCOES FISCAIS MUNICIPAIS DA COMARCA DA CAPITAL RUA PRESIDENTE COUTINHO, 232, SALA 202 - BAIRRO: CENTRO - CEP: 88015-230 - FONE: (48) 3287-7330 - WHATSAPP: (48) 3287-7340 - EMAIL: CAPITAL.REGIONALFISCAL@TJSC.JUS.BR EXECUCAO FISCAL N 5103563-75.2021.8.24.0023/ SC EXEQUENTE : MUNICIPIO DE SCHROEDER/SC EXECUTADO : VST ARTIGOS DO VESTUARIO LTDA ATO ORDINATORIO CONSIDERANDO O ENTENDIMENTO FIRMADO PELO STF NO TEMA N. 1.184, AS MEDIDAS INSTITUIDAS PELO CNJ NA RESOLUCAO N. 547/2024 E A ORIENTACAO CONJUNTA GP/CGJ N. 01/24; CONSIDERANDO QUE O PRESENTE PROCESSO, EM TESE, PODE SER ENQUADRADO NA HIPOTESE DE VALOR ANTIECONOMICO, INCLUSIVE NAO SUPERIOR A 50 ORTNS, QUANDO DO AJUIZAMENTO; FICA INTIMADA A PARTE CREDORA DA SITUACAO RETRATADA, PELO PRAZO DE 14 (QUATORZE) DIAS, A TEOR DO ART. 10 E 218,  1, DO CPC, QUANTO A POSSIVEL EXTINCAO DO PROCESSO, SEM RESOLUCAO DO MERITO. DOCUMENTO ELETRONICO AUTOMATIZADO PELA REGRA DE SISTEMA , NA FORMA DO ART. 1,  2., INC. III, DA LEI 11.419/2006 E DA RESOLUCAO CONJUNTA GP/CGJ N. 05/2018. A CONFERENCIA DA AUTENTICIDADE DO DOCUMENTO ESTA DISPONIVEL NO ENDERECO ELETRONICO HTTPS://EPROC1G.TJSC.JUS.BR/EPROC/EXTERNO_CONTROLADOR.PHP?ACAO=CONSULTA_AUTENTICIDADE_DOCUMENTOS, MEDIANTE O PREENCHIMENTO DO CODIGO VERIFICADOR 310061795590V1 E O CODIGO CRC 1BD78E9C . INFORMACOES ADICIONAIS DA ASSINATURA: RESPONSAVEL PELA REGRA DE AUTOMATIZACAO: EDUARDO ALEXANDRE DOS SANTOS DATA E HORA: 6/7/2024, AS 5:30:48 5103563-75.2021.8.24.0023 310061795590 .V1",
                                    "PublishDate": "2024-07-06T05:30:00",
                                    "CaptureDate": "2024-07-10T19:59:33"
                                },
                                {
                                    "Content": "EXPEDIDA/CERTIFICADA A INTIMACAO ELETRONICAREFER. AO EVENTO 7(EXEQUENTE - MUNICIPIO DE SCHROEDER/SC) PRAZO: 14 DIAS STATUS:FECHADO DATA INICIAL DA CONTAGEM DO PRAZO: 17/07/2024 00:00:00 DATA FINAL: 05/08/2024 23:59:59",
                                    "PublishDate": "2024-07-06T05:30:00",
                                    "CaptureDate": "2024-09-19T08:09:11"
                                },
                                {
                                    "Content": "CIENCIA, COM RENUNCIA AO PRAZO - REFER. AO EVENTO: 4",
                                    "PublishDate": "2022-03-09T11:23:00",
                                    "CaptureDate": "2022-10-23T11:23:14"
                                },
                                {
                                    "Content": "CONFIRMADA A INTIMACAO ELETRONICA - REFER. AO EVENTO: 4",
                                    "PublishDate": "2022-03-07T23:59:00",
                                    "CaptureDate": "2022-10-23T11:23:14"
                                },
                                {
                                    "Content": "EXPEDIDA/CERTIFICADA A INTIMACAO ELETRONICA - DESPACHO/DECISAOREFER. AO EVENTO 3(EXEQUENTE - MUNICIPIO DE SCHROEDER/SC) PRAZO: 90 DIAS STATUS:FECHADO DATA INICIAL DA CONTAGEM DO PRAZO: 08/03/2022 00:00:00 DATA FINAL: 15/07/2022 23:59:59",
                                    "PublishDate": "2022-02-25T16:44:00",
                                    "CaptureDate": "2022-10-23T11:23:14"
                                },
                                {
                                    "Content": "DECISAO INTERLOCUTORIA | PODER JUDICIARIO JUSTICA ESTADUAL TRIBUNAL DE JUSTICA DO ESTADO DE SANTA CATARINA UNIDADE REGIONAL DE EXECUCOES FISCAIS MUNICIPAIS E ESTADUAIS DA COMARCA DE FLORIANOPOLIS RUA PRESIDENTE COUTINHO, 232, SALA 202 - BAIRRO: CENTRO - CEP: 88015-230 - FONE: (48) 3287-7330 - WHATSAPP: (48) 3287-7340 - EMAIL: CAPITAL.REGIONALFISCAL@TJSC.JUS.BR EXECUCAO FISCAL N 5103563-75.2021.8.24.0023/ SC EXEQUENTE : MUNICIPIO DE SCHROEDER/SC EXECUTADO : VST ARTIGOS DO VESTUARIO LTDA DESPACHO/DECISAO 1. CONSTATO QUE O VALOR EXECUTADO E INFERIOR A 1 SALARIO MINIMO VIGENTE A EPOCA DA CONSTITUICAO DO DEBITO. NESSE SENTIDO, A LEI ESTADUAL N 14.266, DE 21/12/2007 DETERMINA QUE AS EXECUCOES FISCAIS COM VALOR INFERIOR A 1 (UM) SALARIO MINIMO DEVERIAM SER SUSPENSAS, COM A SUBSEQUENTE INTIMACAO DO PROCURADOR DA FAZENDA PUBLICA PARA MANIFESTACAO, NOS MOLDES ELENCADOS NO ART. 2. TAL LEGISLACAO FOI REGULAMENTADA PELA RESOLUCAO N. 2/2008, DO CONSELHO DA MAGISTRATURA DO TRIBUNAL DE JUSTICA, RESTANDO ASSENTADO QUE A MANIFESTACAO DO CREDOR DEVERA OBRIGATORIAMENTE LIMITAR-SE A UMA DAS TRES POSSIBILIDADES INDICADAS NO ART. 2 DA LEI ESTADUAL N. 14.266/08, QUAIS SEJAM: A) REQUERER A REUNIAO DE ACOES; B) RECONHECER A FALTA DE INTERESSE DE AGIR E PEDIR A EXTINCAO; OU C) REQUERER O PROSSEGUIMENTO DA ACAO. CONSTA AINDA DA REFERIDA RESOLUCAO QUE, DECORRIDO O PRAZO SEM QUALQUER PRONUNCIAMENTO, O PROCESSO SERA EXTINTO PELA FALTA DE INTERESSE DE AGIR. NAO BASTASSEM A LEI E A RESOLUCAO, A MATERIA VOLTOU A SER DEBATIDA NO EGREGIO TRIBUNAL DE JUSTICA CATARINENSE, SENDO OBJETO DA SUMULA 22, COM O SEGUINTE TEOR: SUMULA 22. A DESPROPORCAO ENTRE A DESPESA PUBLICA REALIZADA PARA A PROPOSITURA E TRAMITACAO DA EXECUCAO FISCAL, QUANDO O CREDITO TRIBUTARIO FOR INFERIOR A UM SALARIO MINIMO, ACARRETA A SUA EXTINCAO POR AUSENCIA DE INTERESSE DE AGIR, SEM PREJUIZO DO PROTESTO DA CERTIDAO DE DIVIDA ATIVA (PROV. CGJ/SC N. 67/99) E DA RENOVACAO DO PLEITO SE A REUNIAO COM OUTROS DEBITOS CONTEMPORANEOS OU POSTERIORES JUSTIFICAR A DEMANDA. ENTRETANTO, RECENTEMENTE O TRIBUNAL DE JUSTICA DE SANTA CATARINA ADMITIU RECURSOS EXTRAORDINARIOS 1 COMO RECURSOS REPRESENTATIVOS DE CONTROVERSIA REPETITIVA, A SEREM ENCAMINHADOS AO SUPREMO TRIBUNAL FEDERAL PARA FINS DE AFETACAO PARA JULGAMENTO PELA SISTEMATICA DA REPERCUSSAO GERAL, CADASTRADOS COMO TEMA GRUPO DE REPRESENTATIVOS N. 13, PROPONDO A REVISAO DA INTERPRETACAO CONFERIDA AO TEMA 109/STF: \"ADOCAO PELO PODER JUDICIARIO DE CRITERIOS NORMATIVOS ESTADUAIS COMO FUNDAMENTO PARA EXTINGUIR ACOES DE EXECUCAO FISCAL AJUIZADAS PELO MUNICIPIO\". NAS RESPECTIVAS DECISOES FOI DETERMINADA  A SUSPENSAO DE TODOS OS PROCESSOS PENDENTES, INDIVIDUAIS OU COLETIVOS, QUE ENVOLVAM IDENTICA QUESTAO DE DIREITO, QUAL SEJA, O TEMA 109/STF, PARA POSSIVEL REEXAME DA TESE, EM TRAMITACAO NO PRIMEIRO GRAU DE JURISDICAO DESTE ESTADO E NESTE TRIBUNAL DE JUSTICA DE SANTA CATARINA, INCLUSIVE OS DEMAIS RECURSOS EM TRAMITE NESTA 2 VICE-PRESIDENCIA, ATE ULTERIOR DELIBERACAO DA CORTE SUPREMA. CONVEM RESSALVAR QUE A PRESENTE DECISAO NAO IMPOSSIBILITA A APRECIACAO DE PEDIDOS DE CONCESSAO DE TUTELA PROVISORIA DE URGENCIA OU DE EVIDENCIA.\" (DECISAO DE ADMISSIBILIDADE DISPONIBILIZADA EM 07.10.2021) 2. PELO EXPOSTO, INTIME-SE O EXEQUENTE PARA MANIFESTAR-SE EM 90 DIAS, DEVENDO ATENTAR-SE TAMBEM ACERCA DE EVENTUAL EXISTENCIA DE LEI MUNICIPAL DISPONDO SOBRE A QUESTAO. 2.A. CASO REQUERIDO, FICA AUTORIZADO DESDE JA O APENSAMENTO DESTE A OUTROS FEITOS, DESDE QUE TODOS TRAMITEM NESTA UNIDADE, HAJA IDENTIDADE DE PARTES E OS PROCESSOS ESTEJAM NA MESMA FASE PROCESSUAL, NOS TERMOS DO ART. 28, CAPUT E PARAGRAFO UNICO, DA LEI 6.830/1980. SENDO REALIZADO O APENSAMENTO, TODOS OS ATOS SERAO EXPEDIDOS NO PROCESSO MAIS ANTIGO, ENGLOBANDO AS INFORMACOES DAS DEMAIS EXECUCOES E RESPECTIVAS CDAS, CERTIFICANDO-SE ESTE FATO NOS PROCESSOS APENSADOS QUE FICARAO SUSPENSOS (ORIENTACAO CGJ NO 18, DE 21/07/2008). CERTIFIQUE-SE QUANTO AS EVENTUAIS PENHORAS EXISTENTES EM TODOS OS AUTOS, INSERINDO A INFORMACAO NO FEITO MAIS ANTIGO, COM COPIAS DOS RESPECTIVOS TERMOS. EM CASO DE PAGAMENTO OU LIQUIDACAO DA DIVIDA QUE ENVOLVA TODAS AS EXECUCOES, PROCEDA-SE A REABERTURA DOS PROCESSOS PARA PROLACAO DA SENTENCA INDIVIDUALMENTE. 2.B. REQUERIDO O ANDAMENTO DO FEITO SEM APENSAMENTO OU SILENTE O ENTE PUBLICO, FICA DETERMINADA A SUSPENSAO DO FEITO, NOS TERMOS INDICADOS ACIMA. DOCUMENTO ELETRONICO ASSINADO POR GABRIELA SAILON DE SOUZA BENEDET, JUIZA DE DIREITO , NA FORMA DO ARTIGO 1, INCISO III, DA LEI 11.419, DE 19 DE DEZEMBRO DE 2006. A CONFERENCIA DA AUTENTICIDADE DO DOCUMENTO ESTA DISPONIVEL NO ENDERECO ELETRONICO HTTPS://EPROC1G.TJSC.JUS.BR/EPROC/EXTERNO_CONTROLADOR.PHP?ACAO=CONSULTA_AUTENTICIDADE_DOCUMENTOS, MEDIANTE O PREENCHIMENTO DO CODIGO VERIFICADOR 310024657651V1 E DO CODIGO CRC 1F830CCE . INFORMACOES ADICIONAIS DA ASSINATURA: SIGNATARIO (A): GABRIELA SAILON DE SOUZA BENEDET DATA E HORA: 25/2/2022, AS 16:44:39 5103563-75.2021.8.24.0023 310024657651 .V1",
                                    "PublishDate": "2022-02-25T16:44:00",
                                    "CaptureDate": "2022-10-23T11:23:14"
                                },
                                {
                                    "Content": "CONCLUSOS PARA DESPACHO",
                                    "PublishDate": "2022-02-25T15:56:00",
                                    "CaptureDate": "2022-10-23T11:23:18"
                                },
                                {
                                    "Content": "DISTRIBUIDO POR SORTEIO (FNSUREF01)",
                                    "PublishDate": "2021-12-15T13:56:00",
                                    "CaptureDate": "2022-10-23T11:23:18"
                                }
                            ],
                            "Petitions": [],
                            "Decisions": [
                                {
                                    "DecisionContent": "JULGO EXTINTO O PROCESSO SEM RESOLUCAO DO MERITO, NOS TERMOS DOS ARTIGOS 485, INCISO VI, E 927, III, DO CODIGO DE PROCESSO CIVIL; ARTS. 1,  1, DA RESOLUCAO CNJ N. 547/2024 E ART. 2 DA ORIENTACAO CONJUNTA GP/CGJ N. 01/2024.",
                                    "DecisionDate": "2024-08-05T16:02:00"
                                }
                            ]
                        }
                    ],
                    "TotalLawsuits": 1,
                    "TotalLawsuitsAsAuthor": 0,
                    "TotalLawsuitsAsDefendant": 1,
                    "TotalLawsuitsAsOther": 0,
                    "FirstLawsuitDate": "2021-12-15T13:56:00",
                    "LastLawsuitDate": "2021-12-15T13:56:00",
                    "Last30DaysLawsuits": 0,
                    "Last90DaysLawsuits": 0,
                    "Last180DaysLawsuits": 0,
                    "Last365DaysLawsuits": 0
                }
            }
        ],
        "QueryId": "e37aca31-b681-4175-9825-21ab6233e018",
        "ElapsedMilliseconds": 290,
        "QueryDate": "2025-04-02T14:16:59.3385815Z",
        "Status": {
            "basic_data": [
                {
                    "Code": 0,
                    "Message": "OK"
                }
            ],
            "processes": [
                {
                    "Code": 0,
                    "Message": "OK"
                }
            ]
        },
        "Evidences": {}
    }
    '''
   
    DadosTeste = json.loads(jsonStr)
    
    return DadosTeste

