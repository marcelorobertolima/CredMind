# utils.py
import hashlib
import time
import random
import xmltodict
import json
import xml.etree.ElementTree as ET

##########################################################################################
#Gera os ids
##########################################################################################
def GeraIDs():
    length=20

    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(length))
    
    # Converte o timestamp atual em string e em seguida para bytes
    timestamp_bytes = f"{time.time()}".encode('utf-8')
    
    # Converte a sequência de dígitos aleatórios para bytes
    random_digits_bytes = random_digits.encode('utf-8')
    
    # Junta os bytes da sequência de dígitos aleatórios com os bytes do timestamp
    unique_string = timestamp_bytes + random_digits_bytes

    hash_object = hashlib.sha256(unique_string)
    
    return hash_object.hexdigest()[:64]

##########################################################################################
#Converte o XML da NFe para json de uma URL
##########################################################################################
def convertXMLFromURL(conteudoXML):
    xml_tree = ET.ElementTree(ET.fromstring(conteudoXML))
    root = xml_tree.getroot()
    to_string  = ET.tostring(root, encoding='UTF-8', method='xml')

    xml_to_dict = xmltodict.parse(to_string, attr_prefix='')

    jsonNFE = json.loads(json.dumps(xml_to_dict).replace("ns0:",""))

    return jsonNFE

##########################################################################################
#Converte o XML da NFe para json de um diretório
##########################################################################################
def convertXMLFromArq(caminho_arquivo_xml):
    # Parse do XML usando ElementTree
    xml_doc_path = caminho_arquivo_xml

    xml_tree = ET.parse(xml_doc_path)

    root = xml_tree.getroot()
    to_string  = ET.tostring(root, encoding='UTF-8', method='xml')

    xml_to_dict = xmltodict.parse(to_string, attr_prefix='')

    jsonNFE = json.loads(json.dumps(xml_to_dict).replace("ns0:",""))

    return jsonNFE

