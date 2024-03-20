import streamlit as st
def cal(a,b,op="+"):
    match (op):
        case '+' : return a +b
        case '-': return  a-b
        case '/': return a/b
        case '*': return a*b
        case '**' : return a**b

#main
st.title('150 rupee ka calculator')        
st.markdown("sasta sundar tikau")
c1,c2,c3 = st.columns(3)
num1 = c1.number_input("enter the first number")        
num2 = c2.number_input('enter the second number')        
action = c3.selectbox('enter the operation you want',['+','-','/','*','**'])
try:
    result = cal(num1,num2,action)
    st.success(f"result:{result}")
except Exception as e:
   st.error(f"error occured:{e}")        