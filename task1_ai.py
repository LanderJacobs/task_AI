from simpleai.search import CspProblem, backtrack
import streamlit as st

# moet hier staan anders doet het vreemd
def try_solve():
    word_list = [word1, word2, solution]
    # variables
    letters = tuple(set([str(x) for x in str().join(word_list)]))
    if(len(letters) > 9):
        return "long"
    # values
    values = {x: list(range(0,10)) for x in letters}
        # Zorg ervoor dat de letters op de eerste plaats geen 0 kunnen zijn
    for letter in letters:
        for word in word_list:
            if letter == word[0]:
                values[letter] = list(range(1,10))
    # constraints
        # constraint dat de som moet kloppen
    def check_sum(variables, values):
        sum_words = 0
        for word in word_list[:-1]:
            sum_words += find_amount(word, values)
        return sum_words == find_amount(word_list[len(word_list)-1], values)

    def find_amount(word, values):
        word_to_sum = ""
        for part in word:
            for number,letter in enumerate(letters):
                if letter == part:
                    word_to_sum += str(values[number])
        return int(word_to_sum)
        # constraint verschillende getallen
    def different_numbers(variables, values):
        return len(values) == len(set(values))
    # constraints
    constraints = [
        (letters, check_sum),
        (letters, different_numbers)
    ]

    problem = CspProblem(letters, values, constraints)
    output = backtrack(problem)

    if output == None:
        return output
    else:
        return [str(find_amount(x, [output[y] for y in letters])) for x in word_list]

st.title("Cryptarithmetic Puzzle solver")
st.subheader("van Lander Jacobs")
word1 = st.text_input(label="word 1", placeholder="odd")
word2 = st.text_input(label="word 2", placeholder="odd")
solution = st.text_input(label="solution", placeholder="even")

if st.button(label="Solve it"):
    if(word1 != "" or word2 != "" or solution != ""):
        answer = try_solve()
        if answer == None:
            st.text("We Weren't able to solve this one")
        elif answer == "long":
            st.text("There were more than 9 characters, this doesn't make it possible to be solved")
        else:
            st.text(word1 + " + " + word2 + " = " + solution)
            st.text(answer[0] + " + " + answer[1] + " = " + answer[2])
    else:
        st.text("You forgot to fill in a word!")

