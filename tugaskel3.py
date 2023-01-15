import streamlit as st

st.title('Ini adalah aplikasi penentuan pH suatu larutan')

NamaLarutan=st.text_input('Nama Larutan yang akan dicari pH')

st.write('Masukan jenis larutan dengan format "asam kuat" "asam lemah" "basa kuat" ataupun "basa lemah" jika format yang dimasukan salah maka web tidak akan bekerja silahkan isi dengan format yang sesuai')

Jenislarutan=st.text_input('Jenis larutan')

if Jenislarutan =="asam kuat":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=0
    val = st.number_input(f'Masukan valensi larutan',format='%.'+str(jumlah_digit1)+'f')
    H=cons*val
    import numpy as np
    pH= -1 * np.log10(H)
    st.write('pH larutan',NamaLarutan,'adalah',pH)
    
elif Jenislarutan == "basa kuat":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=0
    val = st.number_input(f'Masukan valensi larutan',format='%.'+str(jumlah_digit1)+'f')
    OH=cons*val 
    import numpy as np
    pOH= -1 * np.log10(OH)
    pH=14-pOH
    st.write('pH larutan',NamaLarutan,'adalah',pH)
    
elif Jenislarutan == "asam lemah":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=6
    ka = st.number_input(f'Masukan ka dari larutan',format='%.'+str(jumlah_digit1)+'f')
    a = cons * ka
    import numpy as np
    H = np.sqrt(a)
    pH= -1 * np.log10(H)
    st.write('pH larutan',NamaLarutan,'adalah',pH)
    
elif Jenislarutan == "basa lemah":
    jumlah_digit=4
    cons = st.number_input(f'Masukan consentrasi larutan dalam Molaritas (M)',format='%.'+str(jumlah_digit)+'f')
    jumlah_digit1=6
    kb = st.number_input(f'Masukan kb dari larutan',format='%.'+str(jumlah_digit1)+'f')
    a = cons * kb
    import numpy as np
    OH = np.sqrt(a)
    pOH= -1 * np.log10(OH) 
    pOH= -1 * np.log10(OH)
    pH=14-pOH
    st.write('pH larutan',NamaLarutan,'adalah',pH)
    
    
    
    
    
    
    
    
    
