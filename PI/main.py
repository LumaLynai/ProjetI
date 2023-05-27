import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, Bidirectional, Activation
from datetime import datetime, date
from io import StringIO
pd.options.mode.chained_assignment = None
import streamlit as st
from modulo import *
import plotly.express as px
import plotly.graph_objects as go


with open ("C:\\Users\\PI\\style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


st.markdown("<h1 style='text-align:center;font-size:80px; color:#def9fd; margin:0em 0em;'>INDICA &#128200;</h1>", unsafe_allow_html=True)
st.markdown("<hr style= ' background-color:#B6F9FD; padding:0.01rem; width: 20vw; margin: 0em 0em 5em 0em;'>",unsafe_allow_html=True)


opcao = st.sidebar.selectbox('Empresas:',['NAN','3R Petroleum', '3tentos', 'Ânima Educação', 'Adolpho Lindenberg', 'Adolpho Lindenberg', 'Aeris Energy', 'AES Brasil', 
'AES Tietê Energia', 'AES Tietê Energia', 'Afluente T', 'AgroGalaxy', 'Alfa Financeira', 'Alfa Financeira', 
'Alfa Holdings', 'Alfa Holdings', 'Alfa Holdings', 'Alfa Investimento', 'Alfa Investimento', 'Aliansce Sonae', 
'Aliperti', 'Alliar', 'Allied', 'Alpargatas', 'Alpargatas', 'Alper', 'Alphaville', 'Alupar', 'Alupar', 'Ambev', 
'Ambipar', 'Americanas', 'Ampla Energia', 'Arezzo', 'Armac', 'Assaí', 'Atma', 'ATOM', 'Azevedo & Travassos', 
'Azevedo & Travassos', 'Azul', 'B3', 'Bahema', 'Banco ABC Brasil', 'Banco BMG', 'Banco Bradesco', 'Banco Bradesco', 
'Banco BTG Pactual', 'Banco BTG Pactual', 'Banco da Amazônia', 'Banco de Brasília', 'Banco de Brasília', 
'Banco do Brasil', 'Banco do Nordeste', 'Banco Inter', 'Banco Inter', 'Banco Mercantil de Investimentos', 
'Banco Mercantil de Investimentos', 'Banco Mercantil do Brasil', 'Banco Mercantil do Brasil', 
'Banco Modal', 'Banco Modal', 'Banco Pan', 'Banco Santander', 'Banco Santander', 'Banese', 'Banese', 
'Banestes', 'Banestes', 'Banpará', 'Banrisul', 'Banrisul', 'Banrisul', 'Bardella', 'Bardella', 'Baumer', 
'Baumer', 'BB Seguridade', 'BBRK3', 'Bemobi', 'Biomm', 'Biosev', 'BKBR3', 'Blau Farmacêutica', 'Blue Tech Solutions', 
'Blue Tech Solutions', 'Boa Safra Sementes', 'Boa Vista', 'Bombril', 'BR Properties', 'Bradespar', 'Bradespar', 
'Brasil Brokers', 'BrasilAgro', 'Braskem', 'Braskem', 'Braskem', 'BRDT3', 'BRF', 'Brisanet', 'BRMalls', 'BTOW3', 
'C&A', 'Caixa Seguridade', 'Cambuci', 'Camil Alimentos', 'CARD3', 'Carrefour Brasil', 'CASAN', 'CASAN', 'CBA', 'CCPR3', 
'CEB', 'CEB', 'CEB', 'Cedro Têxtil', 'Cedro Têxtil', 'CEEE D', 'CEEE D', 'CEEE GT', 'CEEE GT', 'Celesc', 'Celesc', 
'CELGPAR', 'CELPE', 'CELPE', 'CELPE', 'Cemepe', 'Cemepe', 'CEMIG', 'CEMIG', 'CESP', 'CESP', 'CESP', 
'Cia. de Seg. Aliança da Bahia', 'Cia. de Seg. Aliança da Bahia', 'Cielo', 'ClearSale', 'CNTO3', 'COELBA', 'COELBA', 
'Coelce', 'Coelce', 'Coelce', 'Cogna', 'Comgás', 'Comgás', 'Consórcio Alfa', 'Consórcio Alfa', 'Consórcio Alfa', 
'Consórcio Alfa', 'Consórcio Alfa', 'Consórcio Alfa', 'Consórcio Alfa', 'Conservas Oderich', 'Construtora Tenda', 
'COPASA', 'Copel', 'Copel', 'Copel', 'Corrêa Ribeiro', 'Cosan', 'COSERN', 'COSERN', 'COSERN', 'Coteminas', 'Coteminas',
'CPFL Energia', 'CR2', 'Cruzeiro do Sul Educacional', 'CSN Mineração', 'CSU Cardsystem', 'Cury', 'CVC', 'Cyrela', 
'D1000 Varejo Farma', 'Döhler', 'Döhler', 'Dasa', 'Desktop', 'Dexco', 'Dexxos', 'Dexxos', 'Dimed', 'Dimed', 
'Direcional', 'DMFN3', 'Dommo Energia', 'Dotz', 'Dtcom', 'DTEX3', 'EcoRodovias', 'EDP Brasil', 'Electro Aço Altona', 
'Electro Aço Altona', 'Elektro', 'Elektro', 'Eletrobras', 'Eletrobras', 'Eletrobras', 'Eletromidia', 'Eletropar', 
'EMAE', 'EMAE', 'Embpar', 'Embraer', 'Enauta', 'Encorpar', 'Encorpar', 'Energisa MT', 'Energisa MT', 'Energisa', 
'Energisa', 'Eneva', 'Engie', 'Enjoei', 'EPAR3', 'Equatorial Energia Pará', 'Equatorial Energia Pará', 
'Equatorial Energia Pará', 'Equatorial Energia Pará', 'Equatorial Energia', 'Equatorial Maranhão', 'Espaçolaser', 
'Estapar', 'Estrela', 'Estrela', 'Eternit', 'Eucatex', 'Eucatex', 'Even', 'Excelsior', 'EZTEC', 'FCA', 'Ferbasa', 
'Ferbasa', 'Fertilizantes Heringer', 'Finansinos', 'Fleury', 'Focus Energia', 'Fras-le', 'Gafisa', 
'General Shopping & Outlets', 'Gerdau', 'Gerdau', 'Getnet', 'Getnet', 'GetNinjas', 'GOL', 'GPCP3', 'GPCP4', 'GPS',
'Grazziotin','Grazziotin', 'Grendene', 'Grupo CCR', 'Grupo Mateus', 'Grupo Pão de Açúcar', 'Grupo SBF', 
'Grupo Soma', 'Grupo Vamos', 'Guararapes', 'Habitasul', 'Haga', 'Haga', 'Hapvida', 'HBR Realty', 'Helbor', 
'Hercules', 'Hercules', 'Hering', 'Hermes Pardini', 'Hidrovias do Brasil', 'Hotéis Othon', 'Hypera', 'IGB Eletrônica', 
'IGTA3', 'Iguatemi', 'Iguatemi', 'IMC Alimentação', 'Indústrias ROMI', 'Inepar', 'Inepar', 'Infracommerce', 
'Intelbras', 'Investimentos Bemge', 'Investimentos Bemge', 'Iochpe-Maxion', 'Irani', 'IRB Brasil RE', 'Itaú Unibanco', 
'Itaú Unibanco', 'Itaúsa', 'Itaúsa', 'Jalles Machado', 'JBDU3', 'JBDU4', 'JBS', 'Jereissati Participações', 
'Jereissati Participações', 'JHSF', 'João Fortes', 'Josapar', 'Josapar', 'JPSA3', 'JSL', 'Karsten', 'Karsten', 
'Kepler Weber', 'Klabin', 'Klabin', 'Kora Saúde', 'Lavvi Incorporadora', 'LE LIS BLANC', 'Light', 'Linx', 'LLIS3', 
'Localiza', 'Locamerica', 'Locaweb', 'LOG CP', 'Log-In', 'Lojas Americanas', 'Lojas Americanas', 'Lojas Marisa', 
'Lojas Quero-Quero', 'Lojas Renner', 'Lopes', 'Lupatech', 'M. Dias Branco', 'Méliuz', 'Magazine Luiza ', 
'Mahle Metal Leve', 'Mangels', 'Mangels', 'Marcopolo', 'Marcopolo', 'Marfrig', 'Mater Dei', 'Melhoramentos', 
'Melhoramentos', 'Melnick', 'Mercantil do Brasil Financeira', 'Mercantil do Brasil Financeira', 'Metalúrgica Gerdau',
'Metalúrgica Gerdau', 'Metalúrgica Riosulense', 'Metalfrio', 'Metalgráfica Iguaçu', 'Metalgráfica Iguaçu', 'METISA', 
'METISA', 'Mills', 'Minasmáquinas', 'Minerva', 'Minupar', 'Mitre Realty', 'MMX Mineração', 'Mobly', 'Monark', 
'Monteiro Aranha', 'Mosaico', 'Moura Dubeux', 'Movida', 'MRS Logística', 'MRS Logística', 'MRS Logística', 
'MRV', 'Multilaser', 'Multiplan', 'Mundial', 'Natura', 'Naturgy (CEG)', 'Neoenergia', 'Neogrid', 'Nordon', 
'NotreDame Intermédica', 'OceanPact', 'Odontoprev', 'Oi', 'Oi', 'Omega Geração', 'Oncoclínicas', 'Orizon', 
'OSX Brasil', 'Ourofino Saúde Animal', 'Padtec', 'Pague Menos', 'Panatlântica', 'Panatlântica', 'Paranapanema', 
'Participações Aliança da Bahia', 'Participações Aliança da Bahia', 'PDG Realty', 'Petrobras', 'Petrobras', 
'PetroRecôncavo', 'PetroRio', 'Pettenati', 'Pettenati', 'Petz', 'PINE', 'Plano&Plano', 'Plascar', 'Pomi Frutas', 
'Porto Seguro', 'Portobello', 'Positivo', 'Priner', 'Profarma', 'Qualicorp', 'Raízen', 'RaiaDrogasil', 'Randon', 
'Randon', 'Recrusul', 'Recrusul', "Rede D'Or", 'Rede Energia', 'Refinaria de Manguinhos', 'Renova Energia', 
'Renova Energia', 'Rio Paranapanema Energia', 'Rio Paranapanema Energia', 'RNI', 'Rossi Residencial', 'Rumo', 
'São Carlos', 'São Martinho', 'São Paulo Turismo', 'São Paulo Turismo', 'São Paulo Turismo', 'Sabesp', 'Sanepar', 
'Sanepar', 'Sansuy', 'Sansuy', 'Sansuy', 'Santanense', 'Santanense', 'Santanense', 'Santos Brasil', 'Saraiva', 
'Saraiva', 'Schulz', 'Schulz', 'Sequoia Logística', 'Ser Educacional', 'Siderúrgica Nacional', 'Simpar', 'Sinqia', 
'SLC Agrícola', 'Smart Fit', 'Smiles', 'Sondotécnica', 'Sondotécnica', 'Sondotécnica', 'Springs', 'SulAmérica', 
'SulAmérica', 'Suzano', 'SYN', 'Taesa', 'Taesa', 'Taurus', 'Taurus', 'Technos', 'Tecnisa', 'Tecnosolo', 'Tecnosolo', 
'Tegma', 'Teka', 'Teka', 'Tekno', 'Tekno', 'Telebras', 'Telebras', 'Terra Santa', 'Terra Santa', 'TIM', 'Time For Fun', 
'Totvs', 'Track & Field', 'Traders Club', 'Transmissão Paulista', 'Transmissão Paulista', 'Trevisa', 'Trevisa', 'Trisul',
'Triunfo', 'Tronox Pigmentos', 'Tronox Pigmentos', 'Tronox Pigmentos', 'Tupy', 'Ultrapar', 'Unicasa', 'Unifique', 'Unipar',
'Unipar', 'Unipar', 'Usiminas', 'Usiminas', 'Usiminas', 'Vale', 'Valid', 'Via', 'Vibra Energia', 'Vittia', 'Vivara',
'Viveo', 'Viver', 'Vivo', 'Vulcabras', 'VVAR3', 'WDC Networks', 'WEG', 'Westwing', 'Wetzel', 'Wetzel', 'Whirlpool', 
'Whirlpool', 'Wilson Sons', 'Wiz Soluções', 'WIZS3', 'WLM', 'WLM', 'YDUQS', 'Zamp'])


dic = (
        {'NAN':' ','3R Petroleum': 'RRRP3', '3tentos': 'TTEN3', 'Ânima Educação': 'ANIM3', 'Adolpho Lindenberg': 'CALI4',
 'Aeris Energy': 'AERI3', 'AES Brasil': 'AESB3', 'AES Tietê Energia': 'TIET4', 'Afluente T': 'AFLT3', 
 'AgroGalaxy': 'AGXY3', 'Alfa Financeira': 'CRIV4', 'Alfa Holdings': 'RPAD6', 'Alfa Investimento': 'BRIV4',
 'Aliansce Sonae': 'ALSO3', 'Aliperti': 'APTI4', 'Alliar': 'AALR3', 'Allied': 'ALLD3', 'Alpargatas': 'ALPA4',
 'Alper': 'APER3', 'Alphaville': 'AVLL3', 'Alupar': 'ALUP4', 'Ambev': 'ABEV3', 'Ambipar': 'AMBP3','Americanas': 'AMER3',
 'Ampla Energia': 'CBEE3', 'Arezzo': 'ARZZ3', 'Armac': 'ARML3', 'Assaí': 'ASAI3', 'Atma': 'ATMP3', 'ATOM': 'ATOM3', 
 'Azevedo & Travassos': 'AZEV4', 'Azul': 'AZUL4', 'B3': 'B3SA3', 'Bahema': 'BAHI3', 'Banco ABC Brasil': 'ABCB4',
 'Banco BMG': 'BMGB4', 'Banco Bradesco': 'BBDC4', 'Banco BTG Pactual': 'BPAC5', 'Banco da Amazônia': 'BAZA3', 
 'Banco de Brasília': 'BSLI4', 'Banco do Brasil': 'BBAS3', 'Banco do Nordeste': 'BNBR3', 'Banco Inter': 'BIDI4', 
 'Banco Mercantil de Investimentos': 'BMIN4', 'Banco Mercantil do Brasil': 'BMEB4', 'Banco Modal': 'MODL4', 
 'Banco Pan': 'BPAN4', 'Banco Santander': 'SANB4', 'Banese': 'BGIP4', 'Banestes': 'BEES4', 'Banpará': 'BPAR3', 
 'Banrisul': 'BRSR6', 'Bardella': 'BDLL4', 'Baumer': 'BALM4', 'BB Seguridade': 'BBSE3', 'BBRK3': 'BBRK3', 
 'Bemobi': 'BMOB3', 'Biomm': 'BIOM3', 'Biosev': 'BSEV3', 'BKBR3': 'BKBR3', 'Blau Farmacêutica': 'BLAU3', 
 'Blue Tech Solutions': 'BLUT4', 'Boa Safra Sementes': 'SOJA3', 'Boa Vista': 'BOAS3', 'Bombril': 'BOBR4', 
 'BR Properties': 'BRPR3', 'Bradespar': 'BRAP4', 'Brasil Brokers': 'NEXP3', 'BrasilAgro': 'AGRO3', 'Braskem': 'BRKM6', 
 'BRDT3': 'BRDT3', 'BRF': 'BRFS3', 'Brisanet': 'BRIT3', 'BRMalls': 'BRML3', 'BTOW3': 'BTOW3', 'C&A': 'CEAB3', 
 'Caixa Seguridade': 'CXSE3', 'Cambuci': 'CAMB3', 'Camil Alimentos': 'CAML3', 'CARD3': 'CARD3', 
 'Carrefour Brasil': 'CRFB3', 'CASAN': 'CASN4', 'CBA': 'CBAV3', 'CCPR3': 'CCPR3', 'CEB': 'CEBR6', 
 'Cedro Têxtil': 'CEDO4', 'CEEE D': 'CEED4', 'CEEE GT': 'EEEL4', 'Celesc': 'CLSC4', 'CELGPAR': 'GPAR3', 
 'CELPE': 'CEPE6', 'Cemepe': 'MAPT4', 'CEMIG': 'CMIG4', 'CESP': 'CESP6', 'Cia. de Seg. Aliança da Bahia': 'CSAB4', 
 'Cielo': 'CIEL3', 'ClearSale': 'CLSA3', 'CNTO3': 'CNTO3', 'COELBA': 'CEEB5', 'Coelce': 'COCE6', 'Cogna': 'COGN3', 
 'Comgás': 'CGAS5', 'Consórcio Alfa': 'BRGE8', 'Conservas Oderich': 'ODER4', 'Construtora Tenda': 'TEND3', 
 'COPASA': 'CSMG3', 'Copel': 'CPLE6', 'Corrêa Ribeiro': 'CORR4', 'Cosan': 'CSAN3', 'COSERN': 'CSRN6', 
 'Coteminas': 'CTNM4', 'CPFL Energia': 'CPFE3', 'CR2': 'CRDE3', 'Cruzeiro do Sul Educacional': 'CSED3', 
 'CSN Mineração': 'CMIN3', 'CSU Cardsystem': 'CSUD3', 'Cury': 'CURY3', 'CVC': 'CVCB3', 'Cyrela': 'CYRE3', 
 'D1000 Varejo Farma': 'DMVF3', 'Döhler': 'DOHL4', 'Dasa': 'DASA3', 'Desktop': 'DESK3', 'Dexco': 'DXCO3', 
 'Dexxos': 'DEXP4', 'Dimed': 'PNVL4', 'Direcional': 'DIRR3', 'DMFN3': 'DMFN3', 'Dommo Energia': 'DMMO3', 
 'Dotz': 'DOTZ3', 'Dtcom': 'DTCY3', 'DTEX3': 'DTEX3', 'EcoRodovias': 'ECOR3', 'EDP Brasil': 'ENBR3', 
 'Electro Aço Altona': 'EALT4', 'Elektro': 'EKTR4', 'Eletrobras': 'ELET6', 'Eletromidia': 'ELMD3', 
 'Eletropar': 'LIPR3', 'EMAE': 'EMAE4', 'Embpar': 'BTTL3', 'Embraer': 'EMBR3', 'Enauta': 'ENAT3', 
 'Encorpar': 'ECPR4', 'Energisa MT': 'ENMT4', 'Energisa': 'ENGI4', 'Eneva': 'ENEV3', 'Engie': 'EGIE3', 
 'Enjoei': 'ENJU3', 'EPAR3': 'EPAR3', 'Equatorial Energia Pará': 'EQPA7', 'Equatorial Energia': 'EQTL3', 
 'Equatorial Maranhão': 'EQMA3B', 'Espaçolaser': 'ESPA3', 'Estapar': 'ALPK3', 'Estrela': 'ESTR4', 'Eternit': 
 'ETER3', 'Eucatex': 'EUCA4', 'Even': 'EVEN3', 'Excelsior': 'BAUH4', 'EZTEC': 'EZTC3', 'FCA': 'VSPT3', 
 'Ferbasa': 'FESA4', 'Fertilizantes Heringer': 'FHER3', 'Finansinos': 'FNCN3', 'Fleury': 'FLRY3', 
 'Focus Energia': 'POWE3', 'Fras-le': 'FRAS3', 'Gafisa': 'GFSA3', 'General Shopping & Outlets': 'GSHP3', 
 'Gerdau': 'GGBR4', 'Getnet': 'GETT4', 'GetNinjas': 'NINJ3', 'GOL': 'GOLL4', 'GPCP3': 'GPCP3', 'GPCP4': 'GPCP4', 
 'GPS': 'GGPS3', 'Grazziotin': 'CGRA4', 'Grendene': 'GRND3', 'Grupo CCR': 'CCRO3', 'Grupo Mateus': 'GMAT3', 
  'Grupo Pão de Açúcar': 'PCAR3', 'Grupo SBF': 'SBFG3', 'Grupo Soma': 'SOMA3', 'Grupo Vamos': 'VAMO3', 
  'Guararapes': 'GUAR3', 'Habitasul': 'HBTS5', 'Haga': 'HAGA4', 'Hapvida': 'HAPV3', 'HBR Realty': 'HBRE3', 
  'Helbor': 'HBOR3', 'Hercules': 'HETA4', 'Hering': 'HGTX3', 'Hermes Pardini': 'PARD3', 'Hidrovias do Brasil': 'HBSA3', 
  'Hotéis Othon': 'HOOT4', 'Hypera': 'HYPE3', 'IGB Eletrônica': 'IGBR3', 'IGTA3': 'IGTA3', 'Iguatemi': 'IGTI4', 
  'IMC Alimentação': 'MEAL3', 'Indústrias ROMI': 'ROMI3', 'Inepar': 'INEP4', 'Infracommerce': 'IFCM3', 
  'Intelbras': 'INTB3', 'Investimentos Bemge': 'FIGE4', 'Iochpe-Maxion': 'MYPK3', 'Irani': 'RANI3', 
  'IRB Brasil RE': 'IRBR3', 'Itaú Unibanco': 'ITUB4', 'Itaúsa': 'ITSA4', 'Jalles Machado': 'JALL3', 
  'JBDU3': 'JBDU3', 'JBDU4': 'JBDU4', 'JBS': 'JBSS3', 'Jereissati Participações': 'IGTI4', 'JHSF': 'JHSF3', 
  'João Fortes': 'JFEN3', 'Josapar': 'JOPA4', 'JPSA3': 'JPSA3', 'JSL': 'JSLG3', 'Karsten': 'CTKA4', 
  'Kepler Weber': 'KEPL3', 'Klabin': 'KLBN4', 'Kora Saúde': 'KRSA3', 'Lavvi Incorporadora': 'LAVV3', 
  'LE LIS BLANC': 'VSTE3', 'Light': 'LIGT3', 'Linx': 'LINX3', 'LLIS3': 'LLIS3', 'Localiza': 'RENT3', 
  'Locamerica': 'LCAM3', 'Locaweb': 'LWSA3', 'LOG CP': 'LOGG3', 'Log-In': 'LOGN3', 'Lojas Americanas': 'LAME4', 
  'Lojas Marisa': 'AMAR3', 'Lojas Quero-Quero': 'LJQQ3', 'Lojas Renner': 'LREN3', 'Lopes': 'LPSB3', 'Lupatech': 'LUPA3', 
  'M. Dias Branco': 'MDIA3', 'Méliuz': 'CASH3', 'Magazine Luiza ': 'MGLU3', 'Mahle Metal Leve': 'LEVE3', 
  'Mangels': 'MGEL4', 'Marcopolo': 'POMO4', 'Marfrig': 'MRFG3', 'Mater Dei': 'MATD3', 'Melhoramentos': 'MSPA4', 
  'Melnick': 'MELK3', 'Mercantil do Brasil Financeira': 'MERC4', 'Metalúrgica Gerdau': 'GOAU4', 
  'Metalúrgica Riosulense': 'RSUL4', 'Metalfrio': 'FRIO3', 'Metalgráfica Iguaçu': 'MTIG4', 'METISA': 'MTSA4', 
  'Mills': 'MILS3', 'Minasmáquinas': 'MMAQ4', 'Minerva': 'BEEF3', 'Minupar': 'MNPR3', 'Mitre Realty': 'MTRE3', 
  'MMX Mineração': 'MMXM3', 'Mobly': 'MBLY3', 'Monark': 'BMKS3', 'Monteiro Aranha': 'MOAR3', 'Mosaico': 'MOSI3', 
  'Moura Dubeux': 'MDNE3', 'Movida': 'MOVI3', 'MRS Logística': 'MRSA6B', 'MRV': 'MRVE3', 'Multilaser': 'MLAS3', 
  'Multiplan': 'MULT3', 'Mundial': 'MNDL3', 'Natura': 'NTCO3', 'Naturgy (CEG)': 'CEGR3', 'Neoenergia': 'NEOE3',
  'Neogrid': 'NGRD3', 'Nordon': 'NORD3', 'NotreDame Intermédica': 'GNDI3', 'OceanPact': 'OPCT3', 'Odontoprev': 'ODPV3', 
  'Oi': 'OIBR4', 'Omega Geração': 'OMGE3', 'Oncoclínicas': 'ONCO3', 'Orizon': 'ORVR3', 'OSX Brasil': 'OSXB3', 
  'Ourofino Saúde Animal': 'OFSA3', 'Padtec': 'PDTC3', 'Pague Menos': 'PGMN3', 'Panatlântica': 'PATI4', 
  'Paranapanema': 'PMAM3', 'Participações Aliança da Bahia': 'PEAB4', 'PDG Realty': 'PDGR3', 'Petrobras': 'PETR4', 
  'PetroRecôncavo': 'RECV3', 'PetroRio': 'PRIO3', 'Pettenati': 'PTNT4', 'Petz': 'PETZ3', 'PINE': 'PINE4', 
  'Positivo': 'POSI3', 'Priner': 'PRNR3', 'Profarma': 'PFRM3', 'Qualicorp': 'QUAL3', 'Raízen': 'RAIZ4', 
  'RaiaDrogasil': 'RADL3', 'Randon': 'RAPT4', 'Recrusul': 'RCSL4', "Rede D'Or": 'RDOR3', 'Rede Energia': 'REDE3', 
  'Refinaria de Manguinhos': 'RPMG3', 'Renova Energia': 'RNEW4', 'Rio Paranapanema Energia': 'GEPA4', 'RNI': 'RDNI3', 
  'Rossi Residencial': 'RSID3', 'Rumo': 'RAIL3', 'São Carlos': 'SCAR3', 'São Martinho': 'SMTO3', 
  'São Paulo Turismo': 'AHEB6', 'Sabesp': 'SBSP3', 'Sanepar': 'SAPR4', 'Sansuy': 'SNSY6', 'Santanense': 'CTSA8', 
  'Santos Brasil': 'STBP3', 'Saraiva': 'SLED4', 'Schulz': 'SHUL4', 'Sequoia Logística': 'SEQL3', 
  'Ser Educacional': 'SEER3', 'Siderúrgica Nacional': 'CSNA3', 'Simpar': 'SIMH3', 'Sinqia': 'SQIA3', 
  'SLC Agrícola': 'SLCE3', 'Smart Fit': 'SMFT3', 'Smiles': 'SMLS3', 'Sondotécnica': 'SOND6', 'Springs': 'SGPS3', 
  'SulAmérica': 'SULA4', 'Suzano': 'SUZB3', 'SYN': 'SYNE3', 'Taesa': 'TAEE4', 'Taurus': 'TASA4', 'Technos': 'TECN3', 
  'Tecnisa': 'TCSA3', 'Tecnosolo': 'TCNO4', 'Tegma': 'TGMA3', 'Teka': 'TEKA4', 'Tekno': 'TKNO4', 'Telebras': 'TELB4', 
  'Terra Santa': 'TESA3', 'TIM': 'TIMS3', 'Time For Fun': 'SHOW3', 'Totvs': 'TOTS3', 'Track & Field': 'TFCO4', 
  'Traders Club': 'TRAD3', 'Transmissão Paulista': 'TRPL4', 'Trevisa': 'LUXM4', 'Trisul': 'TRIS3', 'Triunfo': 'TPIS3',
  'Tronox Pigmentos': 'CRPG6', 'Tupy': 'TUPY3', 'Ultrapar': 'UGPA3', 'Unicasa': 'UCAS3', 'Unifique': 'FIQE3', 
  'Unipar': 'UNIP6', 'Usiminas': 'USIM6', 'Vale': 'VALE3', 'Valid': 'VLID3', 'Via': 'VIIA3', 
  'Vibra Energia': 'VBBR3', 'Vittia': 'VITT3', 'Vivara': 'VIVA3', 'Viveo': 'VVEO3', 'Viver': 'VIVR3', 
  'Vivo': 'VIVT3', 'Vulcabras': 'VULC3', 'VVAR3': 'VVAR3', 'WDC Networks': 'LVTC3', 'WEG': 'WEGE3', 
  'Westwing': 'WEST3', 'Wetzel': 'MWET4', 'Whirlpool': 'WHRL4', 'Wilson Sons': 'PORT3', 'Wiz Soluções': 'WIZC3', 
  'WIZS3': 'WIZS3', 'WLM': 'WLMM4', 'YDUQS': 'YDUQ3', 'Zamp': 'ZAMP3'})

t = dic[opcao]

ticker = t

if opcao == 'NAN':
    st.markdown("Este Web Site se dedica a ser uma ferramenta  para  tomada de decisão de compra e venda de ações\
        listadas na B3, utilizando indicadores técnicos como  MACD, Bandas de Bollinger e  Média\
      Móvel Exponencial.  Assim como o desenvolvimento do modelo de machine learning trazendo a projeção de valor.")
    st.markdown('**_Os dados apresentados devem ser usados como indicadores, sendo responsabilidade do usuário avaliar acontecimentos externos e tomada de decisão._**')

   
if opcao != 'NAN':
    st.sidebar.write(" Ticker: ",ticker)
    def link():
        https = 'https://www.alphavantage.co/query?'
        funcao = "function=TIME_SERIES_DAILY_ADJUSTED&symbol="
        em = ticker
        local = ".SAO"
        chave = "&apikey="
        chaveA = "QQK22AN0DB0HF956"
        periodo= "&outputsize=full"
        tipo = "&datatype=csv"
        url = https+funcao+em+local+chave+chaveA+periodo+tipo
        return url
    
    url=requests.get(link())
    df = pd.read_csv(StringIO(url.text))
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%Y-%m-%d')
    df1 = df.copy()
    df1.drop(['dividend_amount','split_coefficient'],axis=1,inplace=True)
    tabela = df1.copy()
    tabela.rename(columns={'timestamp':'Data','open':'Abertura','high':'Maxima','low':'Minimo','close':'Fechamento','adjusted_close':'Fechamento Ajustado'},inplace=True)

    cs = tabela
    
  

    csv = conversor(cs)

    st.sidebar.download_button(
    label="_Download Historico_",
    data=csv,
    file_name='Historico.csv',
    mime='text/csv',
    )
    

    
   
    df_tabela = tabela.copy() 
    
    df_tabela['Data'] = df_tabela['Data'].dt.strftime('%d/%m/%Y')
    df_tabela[['Abertura','Maxima','Fechamento' ,'Minimo','Fechamento Ajustado']]=df_tabela[['Abertura','Maxima', 'Fechamento','Minimo','Fechamento Ajustado']].applymap(cifra)
    
    st.markdown("<h6 style='text-align:center;font-size:20px;margin: 0em 3em 0em 0em;'>HISTORICO</h6>", unsafe_allow_html=True)
    st.dataframe(df_tabela.style\
   .set_properties(**{'background-color':'rgba(42,68,65,50%)', 'color':'#d5e9ea'})\
   .format(precision=2, thousands=".", decimal=","))

    df_graf = tabela.copy() 
    df_graf.set_index(pd.DatetimeIndex(df_graf['Data']))

    st.markdown("<h6 style='text-align:center;font-size:20px;margin: 3em 0em 0em 0em;'>HISTORICO</h6>", unsafe_allow_html=True)
    h = go.Figure(data=[go.Ohlc(x=df_graf['Data'],open=df_graf['Abertura'], 
        high=df_graf['Maxima'],low=df_graf['Minimo'],
       close=df_graf['Fechamento'],increasing_line_color= '#6AFFFF', decreasing_line_color= '#A7A7A7') ])
    h.update_layout(yaxis_title='R$')
    st.plotly_chart(h)
    
    
    #Calculo do MACD
    st.markdown("<h2 style='text-align:center;font-size:34px; color:#60b4ff; margin-top:7rem;'>MACD</h2>", unsafe_allow_html=True)
    st.markdown("Moving Average Convergence-Divergence (MACD) utilizado para analisar tendências de alta e baixa e auxiliando\
        a identificação de quebra de tendências, indicando períodos de venda e compra. ")
   
    
    df_MACD = tabela.head(120)
    MER = tabela['Fechamento'].ewm(span=12).mean()
    MEL = tabela['Fechamento'].ewm(span=26).mean()
    MACD = MER - MEL
    sinal = MACD.ewm(span=9).mean()

    df_MACD['MACD'] = MACD
    df_MACD['sinal'] = sinal

    df_MACD['flag'] = ''
    df_MACD['PreComp'] = np.nan
    df_MACD['PreVen'] = np.nan


    for i in range(1, len(df_MACD.sinal)):
        if df_MACD['MACD'][i] > df_MACD['sinal'][i]:
            if df_MACD['flag'][i-1] == 'c':
                df_MACD['flag'][i] = 'c'
            else:
                df_MACD['flag'][i] = 'c'
                df_MACD['PreComp'][i] = df_MACD['Fechamento'][i]
        elif df_MACD['MACD'][i] < df_MACD['sinal'][i]:
            if df_MACD['flag'][i-1] == 'v':
                df_MACD['flag'][i] = 'v'
            else:
                df_MACD['flag'][i] = 'v'
                df_MACD['PreVen'][i] = df_MACD['Fechamento'][i]

    
    gmac = go.Figure()
    gmac.update_layout(yaxis_title='R$')
    gmac.add_trace(go.Scatter(x=df_MACD['Data'], y=df_MACD['Fechamento'],
               name='Valor de fechamento', line_color='#f2ce89'))
    gmac.add_trace(go.Scatter(x=df_MACD['Data'], y=df_MACD['PreComp'],
               name='Compra', mode='markers', marker=dict(color='#CDFD88', size=12,)))
    gmac.add_trace(go.Scatter(x=df_MACD['Data'], y=df_MACD['PreVen'],
               name='Venda', mode='markers', marker=dict(color='#fd7956', size=12,)))
    st.plotly_chart(gmac)
    

    # Calculo de Bollinger 
    st.markdown("<h2 style='text-align:center;font-size:34px; color:#60b4ff; margin-top:7rem;'>Bandas de Bollinger</h2>", unsafe_allow_html=True)
    st.markdown("Bandas de Bollinger  auxiliam na  identificação de pontos de reversão e tendências, como a volatilidade do mercado.")
    

    df_BB = df_MACD.copy()
    df_BB['MMS20'] = df_BB['Fechamento'].rolling(window=20).mean()
    df_BB['DevPad'] = df_BB['Fechamento'].rolling(window=20).std()
    df_BB['BandSup'] = df_BB['MMS20'] + (df_BB['DevPad']*2)
    df_BB['BandInf'] = df_BB['MMS20'] - (df_BB['DevPad']*2)
    df_BB['BandSup'] = df_BB['BandSup'].apply(format)
    df_BB['BandInf'] = df_BB['BandInf'].apply(format)
    
    graf_BB = go.Candlestick(x=df_BB['Data'], open=df_BB['Abertura'], high=df_BB['Maxima'],
    low=df_BB['Minimo'],close=df_BB['Fechamento'],increasing_line_color= '#6AFFFF', decreasing_line_color= '#A7A7A7')
    BS = go.Scatter(x=df_BB['Data'], y=df_BB['BandSup'], mode='lines', line_color='#CDFD88', name= 'Banda Superios')
    BI = go.Scatter(x=df_BB['Data'], y=df_BB['BandInf'], mode='lines', line_color='#fd7956', name= 'Banda Inferior') 
    BB = go.Figure(data=[graf_BB])
    BB.update_layout(yaxis_title='R$')
    BB.add_trace(BS)
    BB.add_trace(BI)

    st.plotly_chart(BB)
    

    # Calculo Media Movel Exponencial
    st.markdown("<h2 style='text-align:center;font-size:34px; color:#60b4ff; margin-top:7rem;'>MME</h2>", unsafe_allow_html=True)
    st.markdown("Média Móvel Exponencial (MME) auxilia a observar de forma mais clara a tendência do mercado.")
    
    ME = st.selectbox('Intervalo ', ['7, 21 e 42 dias', '31, 61, 121 dias', '100, 150 e 300 dias'])

    
    media = tabela.head(300)

    if ME == '7, 21 e 42 dias':
        media['MME7'] = tabela['Fechamento'].ewm(span=(7), adjust=True,).mean()
        media['MME7'] = media['MME7'].apply(format)

        media['MME21'] = tabela['Fechamento'].ewm(span=(21), adjust=True,).mean()
        media['MME21'] = media['MME21'].apply(format)
        
        media['MME42'] = tabela['Fechamento'].ewm(span=(42), adjust=True,).mean()
        media['MME42'] = media['MME42'].apply(format)
        
        graf_E = go.Candlestick(x=media['Data'], open=media['Abertura'],high=media['Maxima'], low=media['Minimo'],
                close=media['Fechamento'],increasing_line_color= '#6AFFFF', decreasing_line_color= '#A7A7A7')
        ME7 = go.Scatter(x=media['Data'], y=media['MME7'], mode='lines',
                     line_color='#FF53FF', name='Media Movel Exponencial 7 dias')
        ME42 = go.Scatter(x=media['Data'], y=media['MME42'], mode='lines',
                      line_color='#8EB5E1', name='Media Movel Exponencial 42 dias')
        ME21 = go.Scatter(x=media['Data'], y=media['MME21'], mode='lines',
                      line_color='#fdf149', name='Media Movel Exponencial 21 dias')
        fig = go.Figure(data=[graf_E])
        fig.update_layout(yaxis_title='R$')
        fig.add_trace(ME7)
        fig.add_trace(ME42)
        fig.add_trace(ME21)
        st.plotly_chart(fig)
    elif ME == '31, 61, 121 dias':
        media['MME31'] = tabela['Fechamento'].ewm(span=31).mean()
        media['MME31'] = media['MME31'].apply(format)
        
        media['MME61'] = tabela['Fechamento'].ewm(span=61).mean()
        media['MME61'] = media['MME61'].apply(format)
        
        media['MME121'] = tabela['Fechamento'].ewm(span=121).mean()
        media['MME121'] = media['MME121'].apply(format)
        graf_E = go.Candlestick(x=media['Data'], open=media['Abertura'], high=media['Maxima'], low=media['Minimo'],
            close=media['Fechamento'],increasing_line_color= '#6AFFFF', decreasing_line_color= '#A7A7A7')
        ME31 = go.Scatter(x=media['Data'], y=media['MME31'], mode='lines', line_color='#FF53FF', name= 'Media Movel Exponencial 31 dias')
        ME61 = go.Scatter(x=media['Data'], y=media['MME61'], mode='lines', line_color='#8EB5E1', name= 'Media Movel Exponencial 61 dias') 
        ME121 = go.Scatter(x=media['Data'], y=media['MME121'], mode='lines', line_color='#fdf149', name= 'Media Movel Exponencial 121 dias') 
        fig = go.Figure(data=[graf_E])
        fig.update_layout(yaxis_title='R$')
        fig.add_trace(ME31)
        fig.add_trace(ME61)
        fig.add_trace(ME121)
        st.plotly_chart(fig)
    else:
        media['MME100'] = tabela['Fechamento'].ewm(span=100).mean()
        media['MME100'] = media['MME100'].apply(format)
        
        media['MME150'] = tabela['Fechamento'].ewm(span=150).mean()
        media['MME150'] = media['MME150'].apply(format)
        
        media['MME300'] = tabela['Fechamento'].ewm(span=300).mean()
        media['MME300'] = media['MME300'].apply(format)
        
        graf_E = go.Candlestick(x=media['Data'], open=media['Abertura'], high=media['Maxima'], low=media['Minimo'],
            close=media['Fechamento'],increasing_line_color= '#6AFFFF', decreasing_line_color= '#A7A7A7')
        ME100 = go.Scatter(x=media['Data'], y=media['MME100'], mode='lines', line_color='#FF53FF', name= 'Media Movel Exponencial 100 dias')
        ME150 = go.Scatter(x=media['Data'], y=media['MME150'], mode='lines', line_color='#8EB5E1', name= 'Media Movel Exponencial 150 dias') 
        ME300 = go.Scatter(x=media['Data'], y=media['MME300'], mode='lines', line_color='#fdf149', name= 'Media Movel Exponencial 300 dias') 
        fig = go.Figure(data=[graf_E])
        fig.update_layout(yaxis_title='R$')
        fig.add_trace(ME100)
        fig.add_trace(ME150)
        fig.add_trace(ME300)
        st.plotly_chart(fig)
    
   
    # treinamento 
    
    st.markdown("<h2 style='text-align:center;font-size:34px; color:#60b4ff; margin-top:7rem;'>Modelo de Machine learning</h2>", unsafe_allow_html=True)
    rs = st.button("_Rodar Modelo_")
    carg = st.progress(0)
    if rs == False:
        st.markdown('Este modelo de Machine learning foi desenvolvido como um indicador de tendência. Atendo-se como uma ferramenta.')
        
    if rs == True:
        with st.spinner('Wait for it...'):
            for i in range (1):
                
                df3 = tabela.copy()
                df3 = df3.set_index(pd.DatetimeIndex(df3['Data'].values))
                df3.drop(['Data', 'Abertura', 'Maxima','Minimo', 'volume','Fechamento Ajustado'],axis=1,inplace=True)

                qtd_linha = len(df3)
                qtd_treino = round(0.7 * qtd_linha)
                qtd_teste = qtd_linha - qtd_treino
                escala = StandardScaler()
                df_escala = escala.fit_transform(df3)
                
                carg.progress(i + 20)
                
                treino = df_escala[0:qtd_treino]
                teste = df_escala[qtd_treino:qtd_treino+qtd_teste]
                
                
                step = 31
                treino_x, treino_y = dc(treino, step)
                teste_x, teste_y = dc(teste, step)

                treino_x = treino_x.reshape(treino_x.shape[0], treino_x.shape[1], 1)
                teste_x = teste_x.reshape(teste_x.shape[0], teste_x.shape[1], 1)

                m = Sequential()
                m.add(Bidirectional(LSTM(120, return_sequences=True), input_shape=(step, 1)))
                m.add(Activation('elu'))
                m.add(Bidirectional(LSTM(120, return_sequences=True)))
                m.add(LSTM(60))
                m.add(Dense(1))
                m.compile(optimizer="adam", loss="mse")
                
                carg.progress(i + 30)
                
                validar = m.fit(treino_x, treino_y, validation_data=(teste_x, teste_y), batch_size=10, epochs=20 , verbose=2)
                
                pv = m.predict(teste_x)
                pv = escala.inverse_transform(pv)
                
                

                tamanho_test = df3.head(120)
                tam = len(tamanho_test)
                vetor = escala.fit_transform(tamanho_test)
                v = df_escala[0:tam]
                dia_input_steps = tam - step
                input_steps = v[dia_input_steps:]
                input_steps = np.array(input_steps).reshape(1, -1)
                lista_output_steps = list(input_steps)
                lista_output_steps = lista_output_steps[0].tolist()
                
                carg.progress(i+99)
                
                pred_output = []
                i = 0
                n_future = 20
                dois = 0
                contador = 0 
                while contador < 2:
                    
                    while (i < n_future):
                        if (len(lista_output_steps) > step):
                            input_steps = np.array(lista_output_steps[1:])
                            input_steps = input_steps.reshape(1, -1)
                            input_steps = input_steps.reshape(1, step, 1)
                            pred = m.predict(input_steps, verbose=0)
                            lista_output_steps.extend(pred[0].tolist())
                            lista_output_steps = lista_output_steps[1:]
                            pred_output.extend(pred.tolist())
                            i = i+1
                        else:
                            input_steps = input_steps.reshape((1, step, 1))
                            pred = m.predict(input_steps, verbose=0)
                            lista_output_steps.extend(pred[0].tolist())
                            pred_output.extend(pred.tolist())
                            i = i+1
                    contador = contador + 1
                
                
                
                prev = escala.inverse_transform(pred_output)
                prev = np.array(prev).reshape(1, -1)
                lista_output_prev = list(prev)
                lista_output_prev = prev[0].tolist()
                
                
                data = pd.to_datetime(tabela['Data'])
                previsao_data = pd.date_range(list(data)[0] + pd.DateOffset(1), periods=20, freq='b').tolist()
                data_previsao = []
                
                
                for i in previsao_data:
                    data_previsao.append(i.date())
                
                
                  
                df_previsao = pd.DataFrame({'Data': np.array(data_previsao), 'Previsao': lista_output_prev})
                df_previsao['Previsao'] = df_previsao['Previsao'].apply(format)
                
                
                
                
                graf_prev = px.line(df_previsao,x='Data', y='Previsao',color_discrete_sequence=['#f2ce89'],title='Previsão de fechamento',
                labels={'Data':'Data','Previsao':'R$'},markers=True,height=600, width=800)
                
                st.plotly_chart(graf_prev)
                
