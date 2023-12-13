import streamlit as st

def find_greatest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title('Find the Greatest Number')

    num1 = st.number_input('Enter first number:')
    num2 = st.number_input('Enter second number:')
    num3 = st.number_input('Enter third number:')

    if st.button('Find Greatest'):
        greatest = find_greatest_number(num1, num2, num3)
        st.success(f'The greatest number is: {greatest}')

if __name__ == '__main__':
    main()
