import streamlit as st
import pandas as pd
import numpy as np

st.title('Simulador do Partnership 2023 - Líder')
st.caption("Use este simulador para calcular quanto de premiação você poderá receber ao final do ano. Importante frisar que a premiação é calculada em cima de valores preenchidos por você, devem ser considerados como uma aproximação.")


aai=st.number_input("Quanto Assessores premiados?",format="%.0f")

inc=st.number_input("Incremento total do ano da Filial",format="%.0f")
inc2="{:,.0f}".format(inc) 
inc2 = inc2.replace(",",".")
st.caption(f"Incremento total Selecionada: R$ {inc2}")

fat=st.number_input("Faturamento total do ano da Filial",format="%.0f")
fat2="{:,.0f}".format(fat) 
fat2 = fat2.replace(",",".")
st.caption(f"Faturamento total Selecionada: R$ {fat2}")

prem=st.number_input("Premiação total dos Assessores da Filial",format="%.0f")
prem2="{:,.0f}".format(prem) 
prem2 = prem2.replace(",",".")
st.caption(f"Premiação total Selecionada: R$ {prem2}")


if st.button("Calcular Premiação"):

    #Calculando premiação
    if aai< 3:

        tx = 0
        if inc >= 300000000:
            incp = 60000
        elif inc >= 200000000 and inc < 300000000:
            incp = 40000
        elif inc >= 100000000 and inc < 200000000:
            incp = 20000
        elif inc < 100000000:
            incp = 0    
            
        if fat >= 4000000:
            fatp = 80000
        elif fat >= 3000000 and fat < 4000000:
            fatp = 60000
        elif fat >= 2000000 and fat < 3000000:
            fatp = 40000
        elif fat < 2000000:
            fatp = 0    

        premf = (fatp+incp)

    elif aai>=3:

        if aai >= 9:
            tx = 0.5
        elif aai >= 5 and aai < 9:
            tx = 0.25
        elif aai >= 3 and aai < 5:
            tx = 0.10
        elif aai < 3:
            tx = 0    

        if inc >= 300000000:
            incp = 0.2
        elif inc >= 200000000 and inc < 300000000:
            incp = 0.1
        elif inc >= 100000000 and inc < 200000000:
            incp = 0.05
        elif inc < 100000000:
            incp = 0    
            
        if fat >= 4000000:
            fatp = 0.3
        elif fat >= 3000000 and fat < 4000000:
            fatp = 0.2
        elif fat >= 2000000 and fat < 3000000:
            fatp = 0.1
        elif fat < 2000000:
            fatp = 0    

        premf = (prem*tx)
        fatp = premf*fatp
        incp = premf*incp
        
        premf = (incp)+(fatp)+premf

    premf="{:,.0f}".format(premf) 
    premf = premf.replace(",",".")
    
    incp="{:,.0f}".format(incp) 
    incp = incp.replace(",",".")
    
    fatp="{:,.0f}".format(fatp) 
    fatp = fatp.replace(",",".")
        
    valores = [["Premiação Faturamento",fatp],["Premiação Incremento",incp],["% de Premiação do AAI",tx],["Premiaão Final",premf]]
    df = pd.DataFrame(valores,columns=['KPI','R$ em Ações'])

    st.caption(f"Premiações mostradas abaixo estão em Reais por ações da Companhia.")
    st.dataframe(df) 

    