st = "Print every word in this sentence that has an even number of letters"
st = st.split()
for x in st:
    if len(x)%2==0:
        print("Even!")
    else:
        print(x)